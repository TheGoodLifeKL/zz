from socket import *
import re
import multiprocessing
import time
#import dynamic.mini_frame
import sys

class WSGIServer(object):
    def __init__(self,port,app,static_path):
        # 创建套接字
        self.tcp_server_socket = socket(AF_INET, SOCK_STREAM) 
        self.tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定
        self.tcp_server_socket.bind(("", port))
        # 变被动
        self.tcp_server_socket.listen(128)
        self.application = app
        self.static_path = static_path

    def server_client(self, client_socket):
        # 新的套接字收发数据
        # 1. 接收客户端的请求
        request = client_socket.recv(1024).decode("utf-8")
        request_lines = request.splitlines()
        #print(request)
        #print("*"*30)
        print("")
        print(">"*30)
        print(request_lines)
        
        ret = re.match(r"[^/]+([^\s]*)", request_lines[0])
        file_name = ""

        if ret:
            file_name = ret.group(1)
            print("="*20, file_name)
            if file_name == "/":
                file_name ="/index.html"




        # 2. 返回http数据给客户端
        # 如果不是以.py结尾 即为静态资源
        if not file_name.endswith(".py"):
            try:
                f = open(self.static_path + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "----file not found----"
                client_socket.send(response.encode("utf-8"))

            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 Ok\r\n"
                response += "\r\n"

                client_socket.send(response.encode("utf-8"))
                client_socket.send(html_content)
        else:
            # 如果为.py结尾即为动态请求
            # body = mini_frame.login()
            env = dict()

            env['PATH_INFO'] = file_name
            #{"PATH_INFO":"/index.py"}
            #body = dynamic.mini_frame.application(env, self.set_response_header)
            body = self.application(env, self.set_response_header)
            response = "HTTP/1.1 %s ok\r\n" %self.status
            for temp in self .headers:
                response += "%s:%s\r\n" % (temp[0],temp[1])
            response += "\r\n"
            response += body
            client_socket.send(response.encode("utf-8"))


        client_socket.close()
    def set_response_header(self, status, headers):
        self.status = status
        self.headers = headers
    def run_forever(self):
        while True:
            # 等待客户端链接
            client_socket, client_socket_addr = self.tcp_server_socket.accept()
            

            # 为这个客户端服务
            p = multiprocessing.Process(target=self.server_client, args=(client_socket,))
            p.start()
            client_socket.close()
        self.tcp_server_socket.close()
def main():
    """控制整体,创建一个web服务器对象,然后调用这个对象的run_forever方法"""
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except Exception as f:
            print("端口输入错误...")
            return

    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 8080 mini_frame:application")
        return


    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 8080 mini_frame:application")
        return
    with open("./web_server.conf") as f:
        conf_info = eval(f.read())
    sys.path.append(conf_info["dynamic_path"])

    frame = __import__ (frame_name)
    app = getattr(frame, app_name)



    wsgi_server = WSGIServer(port, app, conf_info["static_path"])
    wsgi_server.run_forever()




if __name__ == "__main__":
    main()
