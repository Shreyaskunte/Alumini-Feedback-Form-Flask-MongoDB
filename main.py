import json
from flask import Flask, request, jsonify,render_template
from flask_mongoengine import MongoEngine
import requests



app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
 'db': 'alumini_interaction',
'host': 'localhost',
'port': 27017
}

db = MongoEngine()
db.init_app(app)


class Alumini(db.Document):
 name = db.StringField()
 dob = db.DateField()
 yop=db.StringField()
 dept = db.StringField()
 email = db.EmailField()
 number=db.IntField()
 prsntorg=db.StringField()
 desig=db.StringField()
 option1=db.StringField()
 option2=db.StringField()
 option3=db.StringField()
 option4=db.StringField()
 option5=db.StringField()
 option6=db.StringField()
 option7=db.StringField()
 option8=db.StringField()
 option9=db.StringField()
 option10=db.StringField()
 option11=db.StringField()
 option12=db.StringField()
 def to_json(self):
    return {"name": self.name,
    "dob":self.dob,
    "yop": self.yop,
    "dept":self.dept,
    "email":self.email,
    "number":self.number,
    "prsntorg":self.prsntorg,
    "desig":self.desig,
    "option1":self.option1,
    "option2":self.option2,
    "option3":self.option3,
    "option4":self.option4,
    "option5":self.option5,
    "option6":self.option6,
    "option7":self.option7,
    "option8":self.option8,
    "option9":self.option9,
    "option10":self.option10,
    "option11":self.option11,
    "option12":self.option12}

@app.route('/', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    c = Alumini(name=record['name'],
    dob=record['dob'],
    yop=record['yop'],
    dept=record['dept'],
    email=record['email'],
    number=record['number'],
    prsntorg=record['prsntorg'],
    desig=record['desig'],
    option1=record['option1'],
    option2=record['option2'],
    option3=record['option3'],
    option4=record['option4'],
    option5=record['option5'],
    option6=record['option6'],
    option7=record['option7'],
    option8=record['option8'],
    option9=record['option9'],
    option10=record['option10'],
    option11=record['option11'],
    option12=record['option12'])
    c.save()
    return jsonify(c.to_json())

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=="GET":
        return render_template("contact.html")
    else:
        x={
        "name":request.form['name'],
        "dob":request.form['dob'],
        "yop":request.form['yop'],
        "dept":request.form['dept'],
        "email":request.form['email'],
        "number":int(request.form['number']),
        "prsntorg":request.form['prsntorg'],
        "desig":request.form['desig'],
        "option1":request.form['option1'],
        "option2":request.form['option2'],
        "option3":request.form['option3'],
        "option4":request.form['option4'],
        "option5":request.form['option5'],
        "option6":request.form['option6'],
        "option7":request.form['option7'],
        "option8":request.form['option8'],
        "option9":request.form['option9'],
        "option10":request.form['option10'],
        "option11":request.form['option11'],
        "option12":request.form['option12']}
        x=json.dumps(x)
        response = requests.post(url="http://127.0.0.1:5000/",data=x)
        return render_template("formsuccess.html")

@app.route('/', methods=['DELETE'])
def delete_record():
 record = json.loads(request.data)
 c = Alumini.objects(name=record['name']).first()
 if not c:
    return jsonify({'error': 'data not found'})
 else:
    c.delete()
    return jsonify(c.to_json())

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    c = Alumini.objects(name=name)
    if not c:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(c.to_json())

@app.route('/delete',methods=['GET','POST'])
def delete():
 if request.method=="GET":
    return render_template("delete.html")
 else:
    x={
    "name":request.form['name'],
    }
    x=json.dumps(x)
    response = requests.delete(url="http://127.0.0.1:5000/",data=x)
    return render_template("deletesuccess.html")


@app.route('/display',methods=['GET','POST'])
def find():
 if request.method=="GET":
    return render_template("display.html")
 else:
    name=request.form['name']
    response = requests.get(url="http://127.0.0.1:5000/",params={"name":name})
    loaded_json = json.loads(response.json())
    str1="<table border><tr><th>Name</th><th>1.</th><th>2.</th><th>3.</th><th>4.</th><th>5.</th><th>6.</th><th>7.</th><th>8.</th><th>9.</th><th>10.</th><th>11.</th><th>12.</th></tr>"
    for x in loaded_json:
     str1+="<tr><td>"+x['name']+"</td>"+"<td>"+x['option1']+"</td><td>"+x['option2']+"</td>"+"<td>"+x['option3']+"</td>"+"<td>"+x['option4']+"</td>"+"<td>"+x['option5']+"</td>"+"<td>"+x['option6']+"</td>"+"<td>"+x['option7']+"</td>"+"<td>"+x['option8']+"</td>"+"<td>"+x['option9']+"</td>"+"<td>"+x['option10']+"</td>"+"<td>"+x['option11']+"</td>"+"<td>"+x['option12']+"</td>"
     print(loaded_json)
     return str1
    
if __name__ == '__main__':
    app.run(debug = True)