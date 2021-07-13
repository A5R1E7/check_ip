from flask import Flask, render_template, request, send_file,redirect,url_for, Response, redirect, jsonify
from  flask_accept  import  accept 

app = Flask(__name__,static_folder="static", template_folder="templates")
import sys
import os
import socket

IPList=[]

@app.route('/')
def hello():
    return "Strona testowa"
@app.route('/ip')
@accept('text/html')
def ip():
    h_name = socket.gethostname()
    IP_address = socket.gethostbyname(h_name)
    IPList.append(IP_address)
    return "Twój adres IP:  " + IP_address

@ip.support('application/json')
def ip_json():
    h_name = socket.gethostname()
    IP_address = socket.gethostbyname(h_name)
    IPList.append(IP_address)
    return "Twój adres IP:  " + IP_address


@app.route('/ip/list')
@accept('text/html')
def test():
    return jsonify(Lista = IPList)

@test.support('application/json')
def test_json():
    return jsonify(Lista = IPList)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
