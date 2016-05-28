from flask import (
    Flask, send_from_directory, 
    redirect, request, render_template)
import socket
import os
import json


app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return redirect("/index.html")

@app.route('/static/<path:path>')
def todos_app(path):
    return send_from_directory('static', path)

@app.route('/data', methods=['POST'])
def upload():
    print request.data
    with open('data/%s.json' % get_client_name(), 'w') as f:
        f.write(str(request.data))
    return '"success"'

@app.route('/view')
def view():
    client_files = os.listdir('data')
    clients = [os.path.splitext(c)[0] for c in client_files]
    return render_template('view_all.tmpl', clients=clients)

@app.route('/view/<path:client>')
def view_client(client):
    with open('data/%s.json' % client, 'r') as client_data:    
        tasks = json.load(client_data)
    return render_template('view_one.tmpl', name=client, tasks=tasks)

def get_client_name():
   return socket.gethostbyaddr(request.remote_addr)[0]

app.run(host="localhost", port=5000)
