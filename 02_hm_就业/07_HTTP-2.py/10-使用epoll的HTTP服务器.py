from socket import *
import re
import select
def service_client(new_socket, request):
    #request = new_socket.recv(1024)
    request_lines = request.splitlines()
    print("")
    print(">"*30)
    print(request_lines)
    ret = re.match(r"[^/]+(/[^\s]*)", request_lines[0])
    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"        
    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FUND\r\n"
        response += "\r\n"
        response += "-----file not found-----"
    else:
        # 返回header
        html_content = f.read()
        f.close()
        response_body = html_content 
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)
    #new_socket.close()
def main():
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll()
        # 默认堵塞,直到os监测到数据到来,通过时间通知解堵塞 [(fd, event)]
        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                new_socket, new_socket_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket 
            elif event == select.EPOLLIN:
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    tcp_server_socket.close()
if __name__ == "__main__":
    main()
