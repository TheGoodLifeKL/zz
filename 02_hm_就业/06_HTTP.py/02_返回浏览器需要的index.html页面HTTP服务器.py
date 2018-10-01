from socket import *
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
        request = client_socket.recv(1028)
        print(request)
        print("*"*30)
        # 2. 返回http数据给客户端
        # 2.1 返回head
        reponse = "HTTP/1.1 200 Ok\r\n"
        reponse += "\r\n"
        # 2.2 返回body
        #reponse += "<h1>kofopjopjpo</h1>"
        with open("./html/index.html") as f:
            htmi_content = f.read()
        reponse += htmi_content

        client_socket.send(reponse.encode("utf-8"))
        client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
