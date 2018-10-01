from socket import *
import re
#def server_client(client_socket):
def main():
    # 创建套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM) 
    tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定
    tcp_server_socket.bind(("", 8080))
    # 变被动
    tcp_server_socket.listen(128)
    while True:
        # 等待客户端链接
        client_socket, client_socket_addr = tcp_server_socket.accept()
        # 新的套接字收发数据
        # 1. 接收客户端的请求
        request = client_socket.recv(1024).decode("utf-8")
        request_lines = request.splitlines()
        #print(request)
        #print("*"*30)
        print("")
        print(">"*30)
        print(request_lines)
        
        ret = re.match(r"[^/]+(/[^\s]*)", request_lines[0])

        if ret:
            file_name = ret.group(1)
            print("="*20, file_name)


        # 2. 返回http数据给客户端
        # 2.1 返回head
        reponse = "HTTP/1.1 200 Ok\r\n"
        reponse += "\r\n"
        # 2.2 返回body
        #reponse += "<h1>kofopjopjpo</h1>"
        with open("./html" + file_name, "rb") as f:
            print(f)
            html_content = f.read()

        client_socket.send(reponse.encode("utf-8"))
        client_socket.send(html_content)
        client_socket.close()
#        server_client(client_socket)
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
