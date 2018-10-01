from socket import *
import re
def service_client(new_socket, request):
    #request = new_socket.recv(1024)
    request_lines = request.splitlines()
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
    client_socket_list = list()
    while True:
        try:
            new_socket, new_socket_addr = tcp_server_socket.accept()
        except:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except:
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    tcp_server_socket.close()
if __name__ == "__main__":
    main()
