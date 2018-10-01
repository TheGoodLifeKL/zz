from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client

class FDFSStorage(Storage):
    '''fast dfs 文件存储类'''
    def _open(self,name,mode='rb'):
        '''打开文件时使用'''
        pass

    def _save(self,name,content):
        '''打开文件时使用'''
        # name你要上传的文件名字
        # content 包含你要上传文件的file 对象
        client = Fdfs_client('./utils/fdfs/client.conf')
        res = client.upload_appender_by_buffer(content.read())

        if res.get('Status') != 'upload successed':
            raise Exception('上传文件到fastdfs失败')

        # 获取返回的文件ID
        filename = res.get('Remote file_id')

        return filename

    def exists(self, name):
        '''Django判断文件名是否可用'''
        return False