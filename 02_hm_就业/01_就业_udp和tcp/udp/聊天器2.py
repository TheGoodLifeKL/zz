from socket import *
def send_data(udp_socket):
    msg = input("请输入要发送的内容:")
    ip = input("请输入ip:")
    port = int(input("请输入端口:"))
    send_msg = udp_socket.sendto(msg.encode("utf-8"),(ip,port))
    
def recv_data(udp_socket):
    recv_msg = udp_socket.recvfrom(1024)
    msg = recv_msg[0].decode("utf-8") 
    addr = recv_msg[1]
    print("%s:%s"% (str(addr),msg))

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(("",3333))
    while True:
        print("*"*20)
        print("")
        print("1. 发送数据")
        print("2. 接收数据")
        print("")
        print("*"*20)
        option = input("请输入选项:")
        if option == "1":
            send_data(udp_socket)
        elif option == "2":
            recv_data(udp_socket)
        else:
            print("你的输入有误，请重新输入")

if __name__ == "__main__":
    main()
