from socket import *
def main():
    # 1. 创建套接字
    tcp_client_socket = socket(AF_INET,SOCK_STREAM)
    # 2. 链接服务端
    tcp_client_socket.connect(("192.168.28.125",8080))
    # 3. 发送/接收数据
    send_data = input("请输入要发送的内容：")
    tcp_client_socket.send(send_data.encode("utf-8"))
    # 4. 关闭套接字
    tcp_client_socket.close()

if __name__ == "__main__":
    main()
