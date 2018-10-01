import socket

def main():
    # 创建一个套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定本地信息
    localaddr = ("",3333)
    udp_socket.bind(localaddr)
    while True:
        # 接收数据
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        # 打印数据
        print("%s:%s"% (str(send_addr),recv_msg.decode("gbk")))
    udp_socket.close()        
if __name__ == "__main__":
    main()
