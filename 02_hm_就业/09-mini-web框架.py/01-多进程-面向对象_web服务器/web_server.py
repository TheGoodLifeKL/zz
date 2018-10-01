from socket import *
import re
import multiprocessing

class WSGIServer(object):
    def __init__(self):
        # 创建套接字
        self.tcp_server_socket = socket(AF_INET, SOCK_STREAM) 
        self.tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定
        self.tcp_server_socket.bind(("", 8080))
        # 变被动
        self.tcp_server_socket.listen(128)

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
        # 2.1 返回head
        reponse = "HTTP/1.1 200 Ok\r\n"
        reponse += "\r\n"
        # 2.2 返回body
        #reponse += "<h1>kofopjopjpo</h1>"
        try:
            f = open("./html" + file_name, "rb")
        except:
            reponse = "HTTP/1.1 404 NOT FOUND\r\n"
            reponse += "\r\n"
            reponse += "----file not found----"
            client_socket.send(reponse.encode("utf-8"))

        else:
            html_content = f.read()
            f.close()
        #with open("./html/" + file_name, "rb") as f:
        #    print(f)
        #    html_content = f.read()

        client_socket.send(reponse.encode("utf-8"))
        client_socket.send(html_content)
        client_socket.close()
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
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()



if __name__ == "__main__":
    main()
