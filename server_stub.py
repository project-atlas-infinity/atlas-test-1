# server_stub.py - tiny HTTP server stub (Python 2)
import BaseHTTPServer
import json

class SimpleHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        data = {'path': self.path, 'method': 'GET'}
        body = json.dumps(data)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def run(port=8000):
    server = BaseHTTPServer.HTTPServer(('', port), SimpleHandler)
    print "Serving on port %s..." % port
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print "\nShutting down"
        server.server_close()

if __name__ == '__main__':
    run(8000)
