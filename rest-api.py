from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    
    string = request.args.get('string')
    print(string)
    string = request.args.get('responseType')
    print(string)

    
    
    return "OK 200"

app.run()
