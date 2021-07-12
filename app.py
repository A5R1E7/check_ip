from flask import Flask, render_template, request, send_file,redirect,url_for, Response, redirect, jsonify

from flask_accept import accept

app = Flask(__name__,static_folder="static", template_folder="templates")
import sys
import os
import socket

payload = {}
headers = {header: accept (yaml, json, text, html)}
print(response.text.encode('utf8'))
response = requests.get(localhost, headers=headers)
IPList=[]
@app.route('/ip')
def ip():
    h_name = socket.gethostname()
    IP_address = socket.gethostbyname(h_name)
    IPList.append(IP_address)
    return "Twój adres IP:  " + IP_address

@app.route('/ip/list')
def test_json():
    return jsonify(Lista= IPList)

@app.route('/')
@accept ('text/html') 
def hello():
    return "Strona testowa"
r = requests.get('https://github.com/A5R1E7/check_ip.git', auth=('A5R1E7', 'Divingvatt1'))
r.status_code
r.headers['application/json']
r.encoding
r.text
r.json()
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
