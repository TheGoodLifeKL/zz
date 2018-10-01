from django.http import HttpResponse

class BlockIPSMiddleware(object):
    EXCLUDE_IPS = ['192.168.21.71']
    def process_view(self,request,view_func,*args,**kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')


class TestMiddleware(object):
    def __init__(self):
        print('---init---')
    def process_request(self,request):
        print('---process_request---')
    def process_view(self,request,view_func,*args,**kwargs):
        print('---process_view---')
    def process_response(self,request,response):
        print('---process_response---')
        return response