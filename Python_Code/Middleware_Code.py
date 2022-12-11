import random
import flask
from flask import Flask,request,render_template,url_for,flash,session,redirect
from Flask-session
import pyodbc
from datetime import timedelta

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'static'
app.config['SECRET_KEY'] = "secret_key"
app.permanent_session_lifetime = timedelta(minutes=5)

image_loc = app.config['UPLOADED_IMAGES_DEST']+'/'


def Database_Connection():
    server = 'tcp:avadb01.database.windows.net'
    database ='AVA_DB_1'
    username ='SAadmin'
    password ='Dublin@098'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    return connection.cursor()


def prod_Dataentry(handler,Prod_ID,Prod_Name,V_ID,Man_date,Prod_Size,Prod_Quantity,Description,bin_data):
    handler.execute("INSERT INTO Product(Prod_ID,Prod_Name,Man_date,Prod_Size,Prod_Quantity,Description) VALUES(?,?,?,?,?,?)",Prod_ID,Prod_Name,V_ID,Man_date,Prod_Size,Prod_Quantity,Description)


@app.route("/", methods=['GET', 'POST'])
@app.route("/Guest", methods=['GET', 'POST'])
def homepage():
    session[username] = "guest"
    prod_ids = []
    prod_names = []
    prod_descs = []
    image_list = []
    cursor = Database_Connection()
    cursor.execute("SELECT prod_id,prod_name,prod_description from Product ORDER BY prod_id DESC")
    all_prods = cursor.fetchall()
    if len(all_prods) % 3 == 0:
        row_length = len(all_prods)/3
    else:
        row_length = (len(all_prods)/3)+1
    for value in range(len(all_prods)):
        prod_ids.append(all_prods[value][0])
        prod_names.append(all_prods[value][1])
        prod_descs.append(all_prods[value][2])

    cursor.execute("SELECT Prod_Image from Prod_Images")
    image_val = cursor.fetchall()
    for value in range(len(image_val)):
        filename = "image_"+str(value)+".png"
        image_new_loc = image_loc + filename
        image_list.append(image_new_loc)
        with open(image_new_loc, "wb") as f:
            f.write(image_val[value][0])
    return render_template("h.html", row_length=int(row_length) , prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image=url_for('static', filename=image_list))


@app.route("/Home", methods=['GET', 'POST'])
def user_home():
    prod_ids = []
    prod_names = []
    prod_descs = []
    image_list = []
    cursor = Database_Connection()
    cursor.execute("SELECT prod_id,prod_name,prod_description from Product ORDER BY prod_id DESC")
    all_prods = cursor.fetchall()
    if len(all_prods) % 3 == 0:
        row_length = len(all_prods) / 3
    else:
        row_length = (len(all_prods) / 3) + 1
    for value in range(len(all_prods)):
        prod_ids.append(all_prods[value][0])
        prod_names.append(all_prods[value][1])
        prod_descs.append(all_prods[value][2])

    cursor.execute("SELECT Prod_Image from Prod_Images")
    image_val = cursor.fetchall()
    for value in range(len(image_val)):
        filename = "image_" + str(value) + ".png"
        image_new_loc = image_loc + filename
        image_list.append(image_new_loc)
        with open(image_new_loc, "wb") as f:
            f.write(image_val[value][0])
    return render_template("index.html", row_length=int(row_length), prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image=url_for('static', filename=image_list))

@app.route("/Login", methods=['GET', 'POST'])
def loginpage():
    login_ids = {'admin':'password'}
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['pwd']
        if username in login_ids:
            if password == login_ids[username]:
                session[username] = username
                return redirect("/Home")
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



@app.route("/Products", methods=['GET', 'POST'])
def products():
    image_loc = app.config['UPLOADED_IMAGES_DEST']+'/'
    if request.method == "POST":
        Prod_ID = request.form['Prod_ID']
        Prod_Name = request.form['Prod_Name']
        Man_date = request.form['Man_date']
        Prod_Size = request.form['Dimensions']
        Quantity = request.form['Quantity']
        Description = request.form['Description']
        files = request.files['Images']
        file_name = files.filename
        with open(image_loc+file_name, 'rb') as f:
            bin_data = f.read()
        handler = Database_Connection()
        prod_Dataentry(handler,Prod_ID,Prod_Name,V_ID,Man_date,Prod_Size,Quantity,Description,bin_data)
        return render_template('Form.html',Prod_ID=Prod_ID,Prod_Name=Prod_Name,Man_date=Man_date,Prod_Size=Prod_Size,Prod_Quantity=Prod_Quantity,Description=Description,image=url_for('static',filename=file_name))
    else:
        return render_template('Form.html')


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
#     return c


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # Remove Host and Port after testing

