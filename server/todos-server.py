from flask import Flask, send_from_directory, redirect, request
import socket

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return redirect("/index.html")

@app.route('/<path:path>')
def todos_app(path):
    return send_from_directory('js', path)

@app.route('/data', methods=['POST'])
def upload():
    print request.data
    with open('data/%s.json' % get_client_name(), 'w') as f:
        f.write(str(request.data))
    return '"success"'

@app.route('/view')
def view():
    pass

def get_client_name():
   return socket.gethostbyaddr(request.remote_addr)[0]

app.run(port=80)
