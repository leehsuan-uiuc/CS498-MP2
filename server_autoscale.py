from flask import request, jsonify, Flask
app = Flask(__name__)

@app.route('/', methods=['POST'])
# Once receive the POST request, your server program should create a separate process for running "stress_cpu.py
def run_stress_cpu():
    import subprocess
    import sys
    subprocess.Popen([sys.executable, "stress_cpu.py"])
    return jsonify({'message': 'OK'})

@app.route('/', methods=['GET'])
# Your server program should return the private IP address of the EC2 instance. In Python, you can import socket and use socket.gethostname() to get the IP address. 
def get():
    import socket
    return socket.gethostname()


@app.route('/ping', methods=['GET'])
#  HTTP GET "/ping" to return "pong"
def ping():
    return "pong"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)