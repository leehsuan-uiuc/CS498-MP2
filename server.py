from flask import request, jsonify, Flask
app = Flask(__name__)
number = 0
# HTTP POST "/" with JSON body {"num": 100} where 100 can be any integer.
@app.route('/', methods=['POST'])
def index():
    global number
    number = request.json['num']
    return jsonify({'message': 'OK'})
# HTTP GET "/" to return the current number
#  return the integer seed value in string format. The response body for the above case will be: "100"
@app.route('/', methods=['GET'])
def get():
    return str(number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
