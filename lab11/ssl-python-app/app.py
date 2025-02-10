from flask import Flask
import ssl

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is a secure SSL/TLS Flask server!'

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain('/certs/cert.pem', '/certs/key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context)