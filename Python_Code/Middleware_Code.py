from flask import Flask
import pyodbc


app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
    return("Hello World!") #indent this line

server = 'tcp:avadb01.database.windows.net'
database ='AVA_DB_1'
username ='SAadmin'
password ='Dublin@098'
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = connection.cursor()
cursor.execute("INSERT INTO Vendor (v_id,v_name) VALUES('4','rajeev');")
connection.commit()

cursor.execute("SELECT * FROM Vendor;")
for row in cursor.fetchall():
    print(row)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # indent this line

