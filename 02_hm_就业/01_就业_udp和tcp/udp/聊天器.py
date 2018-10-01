from socket import *
def send_data(udp_socket):
    send_msg = input("请输入发送的内容:")
    send_ip = input("请输入接收方的ip:")
    #send_ip = "192.168.28.101"
    send_port = int(input("请输入接收方port:"))
    msg = udp_socket.sendto(send_msg.encode("utf-8"),(send_ip,send_port))
    #udp_socket.close()

def recv_data(udp_socket):
    
    msg = udp_socket.recvfrom(1024)
    recv_msg = msg[0].decode("gbk")
    recv_addr = msg[1]
    print("%s:%s"% (str(recv_addr),recv_msg))

    
def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    #udp_socket.bind(("192.168.28.126",3333))
    udp_socket.bind(("",3333))

    while True:
        print("="*20)
        print("")
        print("1. 发送数据")
        print("2. 接收数据")
        print("3. 退出系统")
        print("")
        print("="*20)
        option = input("请输入选项:")
        if option == "1":
            send_data(udp_socket)
        elif option == "2":
            recv_data(udp_socket)
        elif option == "3":
            break
        else:
            print("输入有误,请重新输入")
    udp_socket.close()
if __name__ == "__main__":
    main()
