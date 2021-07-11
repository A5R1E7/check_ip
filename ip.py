from flask import Flask, jsonify
import socket
app = Flask(__name__)
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
def hello():
    return 'Strona główna'
if __name__=='__main__':
    app.run(debug=True, port=8000)
