from socket import *
import re
import multiprocessing
def server_client(client_socket):
    # 新的套接字收发数据
    # 1. 接收客户端的请求
    request = client_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    #print(request)
    #print("*"*30)
    print("")
    print(">"*30)
    print(request_lines)
    
    ret = re.match(r"[^/]+([^\s]*)", request_lines[0])
    file_name = ""

    if ret:
        file_name = ret.group(1)
        print("="*20, file_name)
        if file_name == "/":
            file_name ="/index.html"




    # 2. 返回http数据给客户端
    # 2.1 返回head
    reponse = "HTTP/1.1 200 Ok\r\n"
    reponse += "\r\n"
    # 2.2 返回body
    #reponse += "<h1>kofopjopjpo</h1>"
    try:
        f = open("./html" + file_name, "rb")
    except:
        reponse = "HTTP/1.1 404 NOT FOUND\r\n"
        reponse += "\r\n"
        reponse += "----file not found----"
        client_socket.send(reponse.encode("utf-8"))

    else:
        html_content = f.read()
        f.close()
    #with open("./html/" + file_name, "rb") as f:
    #    print(f)
    #    html_content = f.read()

    client_socket.send(reponse.encode("utf-8"))
    client_socket.send(html_content)
    client_socket.close()
def main():
    # 创建套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM) 
    tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定
    tcp_server_socket.bind(("", 8080))
    # 变被动
    tcp_server_socket.listen(128)
    while True:
        # 等待客户端链接
        client_socket, client_socket_addr = tcp_server_socket.accept()
        

        # 为这个客户端服务
        p = multiprocessing.Process(target=server_client, args=(client_socket,))
        p.start()
        client_socket.close()
    tcp_server_socket.close()
if __name__ == "__main__":
    main()
