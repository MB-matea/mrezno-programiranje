from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Matea Beslic " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()