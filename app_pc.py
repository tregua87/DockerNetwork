#!/usr/bin/python3
import sys
import socket
from flask import Flask, request

app = Flask(__name__)

if len(sys.argv) != 2:
    print("usage: {0} <logfile>".format(sys.argv[0]))
    exit(0)

peerips = sys.argv[1]

@app.route('/add')
def add():
    global peerips
    # ip = request.args.get('peer-ip')
    ip = request.remote_addr
    if ip:
        with open(peerips, 'a') as l:
            l.write(ip + "\n")
        return "done"
    return "miss peer-ip"

app.run(debug=True, port=2222, host='0.0.0.0')

