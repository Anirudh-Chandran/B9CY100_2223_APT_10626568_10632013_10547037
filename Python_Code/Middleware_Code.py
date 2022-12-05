import flask
from flask import Flask,request,render_template,url_for
import os
import pyodbc

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'static'


@app.route("/")#URL leading to method
def index():  # Name of the method
    return render_template("index.html")


@app.route("/submission", methods=['GET', 'POST'])
def submission():
    image_loc = app.config['UPLOADED_IMAGES_DEST']+'/'
    if request.method == "POST":
        fname = request.form['fname']
        files = request.files['photo']
        file_name = files.filename
        files.save(image_loc + file_name)
        with open(image_loc+file_name, 'rb') as f:
            bin_data = f.read()
        Database_Connection(fname,bin_data)
        image_val = Data_Retrieval(fname)
        image = "image.jpg"
        image_new_loc = image_loc + image
        with open(image_new_loc,"wb") as f:
            f.write(image_val[1])
        data = image_val[0]
        return render_template('submission.html',data=data)
    else:
        return render_template('submission.html')

def Database_Connection(img_id,binary_value):
    server = 'tcp:avadb01.database.windows.net'
    database ='AVA_DB_1'
    username ='SAadmin'
    password ='Dublin@098'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    cursor = connection.cursor()
    command = "INSERT INTO Prod_Images(img_id,prod_image) VALUES(?,?)"
    cursor.execute(command,img_id,binary_value)
    cursor.commit()

def Data_Retrieval(filename):
    server = 'tcp:avadb01.database.windows.net'
    database = 'AVA_DB_1'
    username = 'SAadmin'
    password = 'Dublin@098'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=yes;UID=' + username + ';PWD=' + password)
    cursor = connection.cursor()
    cursor.execute("SELECT ?,prod_image from Prod_Images",filename)
    image_value = cursor.fetchone()
    c=[]
    for values in image_value:
        c.append(values)
    return c


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # Remove Host and Port after testing

