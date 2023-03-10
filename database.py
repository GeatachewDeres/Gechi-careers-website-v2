from sqlalchemy import create_engine,text 
import os
db_connections_string = os.environ["DB_SECRET_STRING"]
engine = create_engine(db_connections_string,connect_args={
  "ssl":{
    "ssl_ca" : "/etc/ssl/cert.pem" }
})

def load_job_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select *from jobs"))
    result_list = []
    for row in result.all():
     result_list.append(list(row))
  return result_list
def load_jobs_from_db(id):
  with engine.connect() as connection:
    result = connection.execute(
    text("select *from jobs where id =id"))
    #text("select *from jobs where id =:val*, val=id"))
    rows = result.all()
    if len(rows) == 0:
         return None
    else:
         return list(rows[0])
 
def upload_application_to_db(data):
  with engine.connect() as connection:
   connection.execute(text ("INSERT INTO jappliactions(fname, mname) values ('data.fname', 'data.mname')" 
           ))
      
     


# """ query = text ("INSERT INTO jappliactions(fname, mname) values (:fname, :mname)" )
     # connection.execute(query, fname=data['fname'], mname=data['mname']) print("print result 
     # type:",type(result))  
   # result_all= result.all()
   # print("print result.all type:",type(result_all)) 
   # print(" value of result all ", result_all)
    #first_row = result_all[0]
    #print(" type of first value  ", type(first_row))
    #first_result_value = dict(result_all[0])
    #print(" type of dic value  ", type(first_result_value)) 
  # for row in result:
       # print("username:", row["title"]) """