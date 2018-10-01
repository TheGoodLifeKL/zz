from socket import *

def main():
    # 1. 创建套接字
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)
    # 2. 绑定本地信息
    #sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    tcp_server_socket.bind(("",8080))
    # 3. 监听 （listen）主动变被动
    tcp_server_socket.listen(128)
    # 4. accept等待客户端的链接 返回新的套接字对象和客户的地址
    client_socket,client_addr = tcp_server_socket.accept()
    # 5. 收发数据
    recv_data = client_socket.recv(1024)
    print(recv_data.decode("utf-8"))
    client_socket.send("我很好，你呢".encode("utf-8"))
    # 6. 关闭套接字
    client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
