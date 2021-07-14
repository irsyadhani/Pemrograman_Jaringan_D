import socketserver
from http.server import SimpleHTTPRequestHandler
import requests

PORT = 9097 # port serve reverse proxy
hostname = 'localhost:8080'

class ReverseProxy(SimpleHTTPRequestHandler):
    def do_GET(self):
        url = 'http://{}{}'.format(hostname, self.path)
        self.send_response(200)
        self.end_headers()
        response = requests.get(url, verify=False)
        self.wfile.write(response.content)

httpd = socketserver.ForkingTCPServer(('', PORT), ReverseProxy)
print ("Reverse proxy pada port", str(PORT))
httpd.serve_forever()