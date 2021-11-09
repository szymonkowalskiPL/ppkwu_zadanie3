from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    string = request.args.get('string')
    responseType = int(request.args.get('responseType'))
    print(string, responseType)
    
    print("send req to API 2")
    link = 'http://127.0.0.1:5000/checkstring?string='+string
    result = requests.post(link)
    data = result.json()
    print(data)

    returnData=data
    
    if responseType==1:
         print("txt reponse")
         returnData="Lowercase: "+str(data["lower_case"])+"\n"+"Uppercase: "+str(data["upper_case"])+"\n"
         
    elif responseType==2:
        print("json reponse")
        returnData=data
    elif responseType==3:
        print("xml response")
    elif responseType==4:
        print("csv response")

    return returnData

app.run(host="localhost", port=8000, debug=False)
