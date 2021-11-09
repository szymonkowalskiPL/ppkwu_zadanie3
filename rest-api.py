from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    string = request.args.get('string')
    responsType = request.args.get('responseType')
    requests.get('http://127.0.0.1:5000/checkstring?string='+string).content
    
    return "OK 200"

app.run(host="localhost", port=8000, debug=False)
