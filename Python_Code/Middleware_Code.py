import flask
from flask import Flask,request,render_template,url_for,flash
import os
import pyodbc

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'static'
app.config['SECRET_KEY'] = "secret_key"


@app.route("/")
@app.route("/guest")
def homepage():
    return render_template("Homepage.html")


@app.route("/Home", methods=['GET', 'POST'])
def user_home():
    return render_template("Homepage.html")


@app.route("/Login", methods=['GET', 'POST'])
def loginpage():
    login_ids = {'admin':'password'}
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['pwd']
        if username in login_ids:
            if password == login_ids[username]:
                return render_template("Homepage.html")
            else:
                message = 'PASSWORD is incorrect'
                flash(message)
                return render_template("Login.html")
        else:
            flash('NO Username found, Please register...')
            return render_template("Login.html")
    else:
        return render_template("Login.html")

@app.route("/Register",methods=['GET', 'POST'])
def register():
    return render_template("Register.html")

# @app.route("/submission", methods=['GET', 'POST'])
# def submission():
#     image_loc = app.config['UPLOADED_IMAGES_DEST']+'/'
#     if request.method == "POST":
#         fname = request.form['fname']
#         files = request.files['photo']
#         file_name = files.filename
#         files.save(image_loc + file_name)
#         with open(image_loc+file_name, 'rb') as f:
#             bin_data = f.read()
#         Database_Connection(fname,bin_data)
#         image_val = Data_Retrieval(fname)
#         image = file_name
#         image_new_loc = image_loc + image
#         with open(image_new_loc,"wb") as f:
#             f.write(image_val[1])
#         data = image_val[0]
#         return render_template('submission.html',data=data,image=url_for('static',filename=file_name))
#     else:
#         return render_template('submission.html')
#
# def Database_Connection(img_id,binary_value):
#     server = 'tcp:avadb01.database.windows.net'
#     database ='AVA_DB_1'
#     username ='SAadmin'
#     password ='Dublin@098'
#     connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
#     cursor = connection.cursor()
#     command = "INSERT INTO Prod_Images(img_id,prod_image) VALUES(?,?)"
#     cursor.execute(command,img_id,binary_value)
#     cursor.commit()
#
# def Data_Retrieval(img_id):
#     server = 'tcp:avadb01.database.windows.net'
#     database = 'AVA_DB_1'
#     username = 'SAadmin'
#     password = 'Dublin@098'
#     connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=yes;UID=' + username + ';PWD=' + password)
#     cursor = connection.cursor()
#     cursor.execute("SELECT ?,prod_image from Prod_Images ",img_id)
#     image_value = cursor.fetchone()
#     c = []
#     for values in image_value:
#         c.append(values)
#     return c


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # Remove Host and Port after testing

