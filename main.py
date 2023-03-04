from  flask import Flask, render_template,jsonify 
from database import load_job_from_db
ap= Flask(__name__)
JOBS  = [{'id':1,
        'title':'sytem analist',
        'location':'bahirdar, Ethiopia',
        'salary':'br. 300000 '},
         {'id':2,
        'title':'Data scientist',
        'location':'AA, Ethiopia',
        'salary':'br. 600000 '},
        {'id':3,
        'title':'Backend Developer',
        'location':'Sanfrasisco, US',
        'salary':'$. 500000 '}]

@ap.route("/")
def hello_world():
  jobdb=load_job_from_db()
  return render_template('home.html', jobfl=jobdb)
 # return("hello Gechi")
@ap.route("/Api/jobs")
def  list_jobs():
    jobdb=load_job_from_db()
    return jsonify(jobdb)  
if __name__== "__main__": 
# print("hi every body. i am inside main")
  ap.run(host = '0.0.0.0', debug=True)