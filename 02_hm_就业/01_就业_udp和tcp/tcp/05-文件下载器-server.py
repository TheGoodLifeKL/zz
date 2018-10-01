from socket import *

def main():
    # 创建套接字
    tcp_server_socket = socket(AF_INET,SOCK_STREAM)
    # 绑定本地信息
    tcp_server_socket.bind(("192.168.28.85",8000))
    # 使用listen变主动链接为被动
    tcp_server_socket.listen(128)
    while True:
        # 等待接收客户端的链接
        client_socket,client_addr = tcp_server_socket.accept()
        # 接收客户端发送的数据
        recv_data = client_socket.recv(1024)
        print("客户端要下载的文件名是:%s" % recv_data.decode("utf-8"))
        # 打开文件，读取数据
        content = None
        try:
            f = open(recv_data,"rb")
            content = f.read()
            f.close()
        except:
            print("没有要下载的文件%s" % recv_data.decode("utf-8"))
        # 发送文件中的数据给客户端
        if content:
            client_socket.send(content)


        # 关闭套接字
        client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
