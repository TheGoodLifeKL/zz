from socket import *
def main():
    # 创建套接字
    tcp_client_socket = socket(AF_INET,SOCK_STREAM)
    # 链接服务器
    tcp_client_socket.connect(("192.168.28.85",8000))
    # 输入要下载的文件名
    file_name = input("请输入要下载的文件名:")
    # 发送文件名给服务器
    tcp_client_socket.send(file_name.encode("utf-8"))
    # 接收服务器返回的文件信息
    recv_data = tcp_client_socket.recv(1024)
    # 在客户端创建一个文件保存接收到的文件
    if recv_data:
        with open("[接收]"+file_name, "wb") as f:
            f.write(recv_data)
    # f = open("recv_data","wb")
    # f.write(recv_data)
    # f.close()
    # 关闭套接字
    tcp_client_socket.close()

if __name__ == "__main__":
    main()
