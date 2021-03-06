from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from goods.models import GoodsType,IndexGoodsBanner,IndexPromotionBanner,GoodsSKU, IndexTypeGoodsBanner
from django_redis import get_redis_connection
from order.models import OrderGoods
from django.core.paginator import Paginator
# Create your views here.

class IndexView(View):
    '''首页'''
    def get(self,request):
        '''显示首页'''
        # 获取商品的种类信息
        types = GoodsType.objects.all()
        #　获取首页轮播图
        goods_banners = IndexGoodsBanner.objects.all().order_by('index')
        # 获取首页活动页面
        promotion_banners = IndexPromotionBanner.objects.all().order_by('index')
        # 获取分类商品展示信息
        for type in types:
            # 获取type种类首页商品分类的图片展示信息
            image_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=1).order_by('index')
            # 获取type种类首页商品分类的文字展示信息
            title_banners = IndexTypeGoodsBanner.objects.filter(type=type,display_type=0).order_by('index')

            # 动态给type添加属性,分别保存首页分类商品的图片账时信息和文字展示信息
            type.image_banners = image_banners
            type.title_banners = title_banners

        # 获取购物车中商品的数目
        user = request.user
        cart_count = 0
        if user.is_authenticated():
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d'%user.id
            cart_count = conn.hlen(cart_key)
        # 组织模板上下文
        context = {'types':types,
                   'goods_banners':goods_banners,
                   'promotion_banners':promotion_banners,
                   'cart_count':cart_count}
        return render(request,'index.html',context)

class DetailView(View):
    '''详情页'''
    def get(self,request,goods_id):
        '''显示详情页'''
        try:
            sku = GoodsSKU.objects.get(id=goods_id)
        except GoodsSKU.DoesNotExist:
            # 商品不存在
            return redirect(reverse('goods:index'))
        # 获取商品的分类信息
        types = GoodsType.objects.all()

        # 获取商品的评论信息
        sku_orders = OrderGoods.objects.filter(sku=sku).exclude(comment='')

        # 获取新品信息
        new_skus = GoodsSKU.objects.filter(type=sku.type).order_by('-create_time')[:2]

        # 获取同一个SPU的其它规格商品
        same_spu_skus = GoodsSKU.objects.filter(goods=sku.goods).exclude(id=goods_id)

        # 获取购物车中商品的数目
        user = request.user
        cart_count = 0
        if user.is_authenticated():
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d'%user.id
            cart_count = conn.hlen(cart_key)

            # 添加用户历史浏览记录
            conn = get_redis_connection('default')
            history_key = 'history_%d'%user.id
            conn.lrem(history_key,0,goods_id)
            conn.lpush(history_key,goods_id)
            # 至保存最新浏览的５条数据
            conn.ltrim(history_key,0,4)

        # 组织模板上下文
        context = {'sku':sku,'types':types,
                   'sku_orders':sku_orders,
                   'new_skus':new_skus,
                   'same_spu_skus':same_spu_skus,
                   'cart_count':cart_count}
        return render(request,'detail.html',context)

class ListView(View):
    '''列表页'''
    def get(self,request,type_id,page):
        # 显示列表页面
        # 获取种类信息
        try:
            type = GoodsType.objects.get(id=type_id)
        except GoodsType.DoesNotExist:
            # 种类不存在
            return redirect(reverse('goods:index'))

        # 获取商品的分类信息
        types = GoodsType.objects.all()

        # 获取分类商品的信息
        # 获取排序的方式
        #　sort=default 按照默认ｉｄ排序
        # sort= price 价格
        # sort=hot 销量
        sort = request.GET.get('sort')
        if sort == 'price':
            skus = GoodsSKU.objects.filter(type=type).order_by('price')
        elif sort == 'hot':
            skus = GoodsSKU.objects.filter(type=type).order_by('-sales')
        else:
            sort = 'default'
            skus = GoodsSKU.objects.filter(type=type).order_by('-id')

        # 对数据进行分页
        paginator = Paginator(skus,1)

        # 获取第ｐａｇｅ页的内容
        try :
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1
        # 获取第ｐａｇｅ页的ｐａｇｅ对象
        skus_page = paginator.page(page)


        # 获取新品信息
        new_skus = GoodsSKU.objects.filter(type=type).order_by('-create_time')[:2]

        # 获取购物车中商品的数目
        user = request.user
        cart_count = 0
        if user.is_authenticated():
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d'%user.id
            cart_count = conn.hlen(cart_key)

        # 组织模板上下文
        context = {'type':type,'types':types,
                   'skus_page':skus_page,
                   'new_skus':new_skus,
                   'cart_count':cart_count,
                   'sort':sort}
        return render(request,'list.html',context)






