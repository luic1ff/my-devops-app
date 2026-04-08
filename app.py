from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello World!')

server = HTTPServer(('0.0.0.0', 8080), Handler)
print('Server running on port 8080')
server.serve_forever()