import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON():
    jsonStr = request.get_json()
    # print(jsonStr)
    jsonObj = json.loads(jsonStr)
    response = ""
    l1 = list(map(int,jsonObj['temp1'].split(",")))
    l2 = list(map(int, jsonObj['temp2'].split(",")))
    if len(l1) > len(l2):
        m = len(l1)
        temp = l1[:]
        s = "l1"
    else:
        m = len(l2)
        temp = l2[:]
        s = "l2"
    mi = min(len(l1),len(l2))
    for i in range(mi):
        response +="<b> "+ str(l1[i])+" "+ str(l2[(len(l2)-i-1)])+ "<br>"
    if s == "l1":
        for i in range(m-mi):
            response += "<b> " + str(temp[mi+i])+"<br>"
    elif s == "l2":
        for i in range(m-mi):
            response += "<b> "+str(temp[mi-i-2])+"<br>"
    return response
  
    
    	    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
