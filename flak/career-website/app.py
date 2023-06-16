from flask import Flask,render_template,jsonify
import logging

logging.basicConfig(filename="app.log" , level=  logging.DEBUG, format='%(asctime)s %(message)s')
app= Flask(__name__)

jOBs= [
    {   'id': 1,
        'title':'data analyst',
        'location':'howrah',
        'salary': 'rs 15lac'
    } ,
    {
        'id': 2,
        'title':'data science',
        'location':'howrah',
        'salary': 'rs 10lac'
    },
    {
        'id': 3,
        'title':'web dev',
        'location ':'delhi',
        'salary'  : 'rs 100lac'
    },


]

@app.route("/")
def hello():
    return render_template('home.html',job=jOBs,company ='carear')

@app.route("/jOBs")
def list_jobs():
    return jsonify(jOBs)

if __name__=='__main__':
    app.run(host='0.0.0.0' ,debug=True)