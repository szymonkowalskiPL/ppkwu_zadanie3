from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    
    string = request.args.get('string')
    print(string)
    responseType = request.args.get('responseType')
    print(responseType)

    
    
    return "OK 200"

app.run(host="localhost", port=8000, debug=True)
