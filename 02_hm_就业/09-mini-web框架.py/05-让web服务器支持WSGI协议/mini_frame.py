def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])
    return 'Hello World!哈哈哈'