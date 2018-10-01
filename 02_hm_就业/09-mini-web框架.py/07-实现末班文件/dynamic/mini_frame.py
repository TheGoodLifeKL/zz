def index():
    #return "这是主页"
    with open("./templates/index.html") as f:
        content = f.read()
    return content
def center():
    #return "这是登陆页面"
    with open("./templates/center.html") as f:
        content = f.read()
    return content
    

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])
    file_name = env["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return "hello world! 你好世界!"
