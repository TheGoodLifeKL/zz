from socket import *
import time
def server_for_new_socket(client_socket_list):
    for new_socket in client_socket_list:
        try:
            recv_data = new_socket.recv(1024).decode("utf-8")
            print(recv_data)
        except:
            print("----客户端没有发送数据----")
        else:
            if recv_data:
                print("----客户端发送数据----")
            else:
                # 客户端close,recv返回
                new_socket.close()
                client_socket_list.remove(new_socket)
                print("----客户端已经关闭----")


def main():
    # 创建套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM) 
    # 设置为非堵塞
    tcp_server_socket.setblocking(False)
    # 绑定
    tcp_server_socket.bind(("", 8080))

    # 变为被动
    tcp_server_socket.listen(128)
    client_socket_list =list()
    while True:
        time.sleep(1)
        # 等待客户端链接
        try:
            new_socket, new_socket_adr = tcp_server_socket.accept()
        except:
            print("----没有人链接----")
        else:
            print("---有一个新的客户端链接----")
            new_socket.setblocking(False) # 设置为费堵塞
            client_socket_list.append(new_socket)
        # 为新的套接字服务
        server_for_new_socket(client_socket_list)



if __name__ =="__main__":
    main()

