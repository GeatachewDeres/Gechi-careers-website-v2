from  flask import Flask, render_template,jsonify 
ap= Flask(__name__)
JOBS  = [{'id':1,
        'title':'sytem analist',
        'location':'bahirdar, Ethiopia',
        'Salary':'br. 300000 '},
         {'id':2,
        'title':'Data scientist',
        'location':'AA, Ethiopia',
        'Salary':'br. 600000 '},
        {'id':3,
        'title':'Backend Developer',
        'location':'Sanfrasisco, US',
        'Salary':'$. 500000 '}]
@ap.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)
 # return("hello Gechi")
@ap.route("/Api/jobs")
def  list_jobs():
    return jsonify(JOBS)  
if __name__== "__main__": 
# print("hi every body. i am inside main")
  ap.run(host = '0.0.0.0', debug=True)