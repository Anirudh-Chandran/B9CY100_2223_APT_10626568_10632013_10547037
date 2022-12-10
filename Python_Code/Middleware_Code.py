import random
import flask
from flask import Flask,request,render_template,url_for,flash,session,redirect
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


@app.route("/")
@app.route("/guest")
def homepage():
    return render_template("h.html")


@app.route("/Home", methods=['GET', 'POST'])
def user_home():
    cursor = Database_Connection()
    cursor.execute("SELECT prod_id,prod_name,prod_description from Product")
    all_prods = cursor.fetchall()
    cursor.execute("Select prod_image from prod_images")
    prod_id1 = all_prods[0][0]
    prod_name1 = all_prods[0][1]
    prod_desc1 = all_prods[0][2]
    prod_id2 = all_prods[1][0]
    prod_name2 = all_prods[1][1]
    prod_desc2 = all_prods[1][2]
    cursor.execute("SELECT prod_image from Prod_Images where prod_id=? or prod_id = ?",prod_id1,prod_id2)
    image_val = cursor.fetchall()
    filename="image.png"
    image_new_loc = image_loc + filename
    with open(image_new_loc,"wb") as f:
        f.write(image_val[0][0])
    prod_ids = [prod_id1,prod_id2]
    return render_template("h.html",prod_ids_len=len(prod_ids),prod_ids=prod_ids,prod_name1=prod_name1,prod_name2=prod_name2,prod_desc1=prod_desc1,prod_desc2=prod_desc2,image=url_for('static',filename=filename))


@app.route("/Login", methods=['GET', 'POST'])
def loginpage():
    login_ids = {'admin':'password'}
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['pwd']
        if username in login_ids:
            if password == login_ids[username]:
                session[username]=username
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

