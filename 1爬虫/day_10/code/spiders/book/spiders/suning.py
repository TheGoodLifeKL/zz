# -*- coding: utf-8 -*-
import scrapy
import re,json
from copy import deepcopy


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com','suning.cn']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # 分组 第一次
        b_cate_list = response.xpath("//div[@class='menu-item']")
        # print(b_cate_list)
        for i,b_cate in enumerate(b_cate_list):
            b_cate_name = b_cate.xpath(".//a/text()").extract_first()
            b_cate_href = b_cate.xpath(".//a/@href").extract_first()
            print(b_cate_name,b_cate_href)

            # 第二次
            m_cate_list = response.xpath("//div[@class='menu-sub'][%d]/div[@class='submenu-left']/p"% (i+1))
            # print(s_cate_list)
            for m_cate in m_cate_list:
                m_cate_name = m_cate.xpath("./a/text()").extract_first()
                m_cate_href = m_cate.xpath("./a/@href").extract_first()
                print(m_cate_name,m_cate_href)

                s_cate_list = m_cate.xpath("./following-sibling::ul[1]//a")
                for s_cate in s_cate_list:
                    s_cate_name = s_cate.xpath("./text()").extract_first()
                    s_cate_href = s_cate.xpath("./@href").extract_first()
                    print(s_cate_name,s_cate_href)
                    cate = {
                        "b_cate_name":b_cate_name,"b_cate_href":b_cate_href,
                        "m_cate_name":m_cate_name,"m_cate_href":m_cate_href,
                        "s_cate_name":s_cate_name,"s_cate_href":s_cate_href
                    }
                    yield scrapy.Request(
                        s_cate_href,
                        callback=self.parse_list,
                        meta={"cate":cate}
                    )

    def parse_list(self,response):
        # 分组
        li_list = response.xpath("//div[@id='filter-results']//li")
        # print(li_list)
        # print("*"*30)
        for li in li_list:
            item = {}
            item.update(response.meta["cate"])
            item["title"] = li.xpath(".//p[@class='sell-point']/a/text()").extract_first()
            item["href"] = li.xpath(".//p[@class='sell-point']/a[@class='sellPoint']/@href").extract_first()
            item["img"] = response.urljoin(li.xpath(".//div[@class='img-block']//img/@src2").extract_first())
            item["shopid"],item["prodid"] = re.findall(r'\/\/product.suning.com\/(\d+)\/(\d+).html',item["href"])[0]
            # print(item["shopid"],item["prodid"])
            yield scrapy.Request(
                "https://ds.suning.cn/ds/generalForTile/000000000%s__2_%s-010-2-0070121210-1--.json" % (
                item["prodid"], item["shopid"]),
                callback=self.parse_price,
                meta={"item": deepcopy(item)}
            )
            # print("https://ds.suning.cn/ds/generalForTile/000000000%s__2_%s-010-2-0070121210-1--.jsonp" % (
            #     item["prodid"], item["shopid"]))
            # print(item)
        # 下一页
        # 当前页 https://list.suning.com/1-262669-0.html
        if len(re.findall(r'\/\/list.suning.com/\d+-(\d+)-(\d+).html', response.url))>0:
            current_cate, current_page = re.findall(r'\/\/list.suning.com/\d+-(\d+)-(\d+).html', response.url)[0]
            # print(re.findall(r'https://list.suning.com/\d+-(\d+)-(\d+).html', response.url))
            current_page = int(current_page)
            current_cate = int(current_cate)
            # print(current_cate, current_page)
            # 总数量 <input type="hidden" value="3712" id="totalCount">
            total = int(response.xpath('//input[@id="totalCount"]/@value').extract_first())
            if (current_page + 1) * 60 < total:
                # print("+"*100)
                yield scrapy.Request(
                    "https://list.suning.com/1-%s-%d.html" % (current_cate, current_page + 1),
                    callback=self.parse_list,
                    meta={"cate": response.meta["cate"]}
                )
                # print("*"*100)

    def parse_price(self,response):
        # print("-"*100)
        item = response.meta["item"]
        data = json.loads(response.body.decode())
        item["price"] = data["rs"][0]["price"]
        # print(item["price"])
        yield scrapy.Request(
            response.urljoin(item["href"]),
            callback=self.parse_detail,
            meta={"item": item}
        )

    def parse_detail(self,response):
        item = response.meta["item"]
        item["author"] = response.xpath('.//span[text()="作者："]/../text()').extract_first()
        print(item)


