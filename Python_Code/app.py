from flask import Flask,request,render_template,url_for,flash,session,redirect
from flask_session import Session
import pyodbc
from datetime import timedelta

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'static'
app.config['SESSION_TYPE'] = "filesystem"
app.config['SECRET_KEY'] = "secret_key"
Session(app)
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
    session['uname']=None
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
        cursor.execute("SELECT Prod_Image from Prod_Images WHERE prod_id=?", all_prods[value][0])
        image_val = cursor.fetchval()
        if image_val is not None:
            filename = "image_" + str(value) + ".png"
            image_new_loc = image_loc + filename
            image_list.append(image_new_loc)
            with open(image_new_loc, "wb") as f:
                f.write(image_val)
        else:
            image_list.append(image_loc + "images/blank.png")
    print(image_list)
    return render_template("homepage.html", row_length=int(row_length) , prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image_list=image_list)


@app.route("/Home", methods=['GET', 'POST'])
def user_home():
    if session.get('uname'):
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
    else:
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
        return render_template("user_homepage.html", row_length=int(row_length), prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image=url_for('static', filename=image_list))


@app.route("/Login", methods=['GET', 'POST'])
def loginpage():
    login_ids = {'admin':'password'}
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['pwd']
        if username in login_ids:
            if password == login_ids[username]:
                session['uname'] = username
                return redirect("/Home")
            else:
                message = 'PASSWORD is incorrect'
                flash(message)
                return render_template("login.html")
        else:
            flash('NO Username found, Please register...')
            return render_template("Login.html")
    else:
        return render_template("login.html")


@app.route("/Register",methods=['GET', 'POST'])
def register():
    
    return render_template("registration.html")


@app.route("/Products",methods=['GET', 'POST'])
def products():
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
        cursor.execute("SELECT Prod_Image from Prod_Images where prod_id = ?",all_prods[value][0])
        image_val = cursor.fetchval()
        if image_val is not None:
            filename = "image_" + str(value) + ".png"
            image_new_loc = image_loc + filename
            image_list.append(image_new_loc)
            with open(image_new_loc, "wb") as f:
                f.write(image_val)
        else:
            image_list.append(image_loc + "images/blank.png")
    return render_template("products.html", row_length=int(row_length), prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image_list=image_list)


@app.route("/New_Products", methods=['GET', 'POST'])
def new_products():
    image_loc = app.config['UPLOADED_IMAGES_DEST']+'/'
    if request.method == "POST" and session.get('uname'):
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
        return render_template('Forms.html',Prod_ID=Prod_ID,Prod_Name=Prod_Name,Man_date=Man_date,Prod_Size=Prod_Size,Prod_Quantity=Prod_Quantity,Description=Description,image=url_for('static',filename=file_name))
    else:
        return redirect('/Login')


@app.route("/OnDemandRequest",methods = ['GET', 'POST'])
def On_Demand_Request():
    if session.get('uname'):
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
        return render_template("on_demand_request.html", row_length=int(row_length), prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image=url_for('static', filename=image_list))
    else:
        return redirect("/Login")


@app.route("/AboutUs")
def about_us():
    return render_template("about_us.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # Remove Host and Port after testing

