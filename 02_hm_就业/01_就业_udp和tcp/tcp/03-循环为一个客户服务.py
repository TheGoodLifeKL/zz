from socket import *

def main():
        # 1. 创建套接字
        tcp_server_socket = socket(AF_INET,SOCK_STREAM)
        # 2. 绑定本地信息
        tcp_server_socket.bind(("",3456))
        # 3. 监听 （listen）主动变被动
        tcp_server_socket.listen(128)
        while True:
            print("等待一个客户端到来....")
            # 4. accept等待客户端的链接 返回新的套接字对象和客户的地址
            client_socket,client_addr = tcp_server_socket.accept()
            print("一个客户端已经到来%s" % str(client_addr))
            while True:
                # 5. 收发数据
                recv_data = client_socket.recv(1024)
                print(recv_data.decode("utf-8"))
                # 如果recv解堵塞，有2种方式:
                # 1. 客户端发送过来数据
                # 2. 客户端关闭
                if recv_data:
                    client_socket.send("我很好，你呢".encode("utf-8"))
                else:
                    break
            # 6. 关闭套接字
            client_socket.close()
            print("已经为这个客户端服务完毕...")
        tcp_server_socket.close()

if __name__ == "__main__":
    main()
