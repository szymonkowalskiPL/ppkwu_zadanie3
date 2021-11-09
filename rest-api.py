from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    string = request.args.get('string')
    responsType = request.args.get('responseType')
    link = 'http://127.0.0.1:5000/checkstring?string='+string
    print(link)
    requests.post(link).content
    
    return "OK 200"

app.run(host="localhost", port=8000, debug=False)
