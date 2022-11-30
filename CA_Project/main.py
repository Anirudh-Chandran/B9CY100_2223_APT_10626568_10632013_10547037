import pyodbc
import flask

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