def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'hello from vercel python']
