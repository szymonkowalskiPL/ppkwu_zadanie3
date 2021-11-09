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
    result = requests.post(link)
    data = result.json()

    if responsType==1:
         print("txt reponse")
    elif responsType==2:
        print("json reponse")
    elif responsType==3:
        print("xml response")
    elif responsType==4:
        print("csv response")

    return "ok"

app.run(host="localhost", port=8000, debug=False)
