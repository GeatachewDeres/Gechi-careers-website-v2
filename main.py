from  flask import Flask
ap= Flask(__name__)
@ap.route("/")
def hello_world():
  return("hello Gechi")
if __name__== "__main__": 
# print("hi every body. i am inside main")
  ap.run(host = '0.0.0.0', debug=True)