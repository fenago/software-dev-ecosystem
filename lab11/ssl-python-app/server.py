import http.server
import ssl

server_address = ('localhost', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap the socket with SSL
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile='/certs/key.pem',
    certfile='/certs/cert.pem',
    server_side=True
)

print('Serving on https://localhost:4443')
httpd.serve_forever()