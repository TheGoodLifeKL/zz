import socket
def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        send_data = input("请输入要发送发送的内容:")
        #退出
        if send_data == "exit":
            break
        #发送数据
        udp_socket.sendto(send_data.encode("utf-8"),("192.168.28.101",8080))
    udp_socket.close()        
if __name__ == "__main__":
    main()
