from flask import Flask,request,render_template,url_for,flash,session,redirect
from flask_session import Session
import pyodbc
from datetime import timedelta
import string
import xml.etree.ElementTree as x

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'static'
app.config['SESSION_TYPE'] = "filesystem"
app.config['SECRET_KEY'] = "secret_key"
Session(app)
app.permanent_session_lifetime = timedelta(minutes=5)

image_loc = app.config['UPLOADED_IMAGES_DEST']+'/'

login_ids = {'admin':'password'}


def Database_Connection():
    server = 'tcp:avadb01.database.windows.net'
    database ='AVA_DB_1'
    username ='SAadmin'
    password ='Dublin@098'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    return connection.cursor()


def prod_Dataentry(Prod_Name,Prod_Size,Description,bin_data):
    handler = Database_Connection()
    handler.execute("INSERT INTO Product(Prod_Name,V_ID,Prod_Size,Prod_Description) VALUES(?,1,?,?)",Prod_Name,Prod_Size,Description)
    handler.commit()
    handler.execute("SELECT PROD_ID FROM PRODUCT WHERE PROD_NAME=?",Prod_Name)
    prod_id = handler.fetchval()
    handler.execute("INSERT INTO Prod_IMAGES(Prod_ID,PROD_IMAGE) VALUES(?,?)",prod_id,bin_data)
    handler.commit()


def req_Dataentry(req_title,req_desc,hosp_name,req_dimensions,req_budget,req_nbd,req_qty):
    handler = Database_Connection()
    handler.execute("INSERT INTO OnDemand_Request(req_title,req_description,req_dimensions,req_quantity,req_need_by_data,req_budget) VALUES(?,?,?,?,?,?)", req_title, req_desc, req_dimensions, req_qty, req_nbd, req_budget)
    handler.commit()
    handler.execute("SELECT H_ID from Hospital where hosp_name=?",hosp_name)
    h_id = handler.fetchval()
    handler.execute("INSERT INTO OnDemand_Request(h_id) values(?)",h_id)
    handler.commit()
"""
The below section of code was generated as an initial step to generate the xml file.
def credentials_generator():
    root = x.Element("Credentials")
    vendor = x.Element("Vendor")
    root.append(vendor)
    vendor_default = x.SubElement(vendor,"default")
    vendor_default.text = " "
    hospital = x.Element("Hospital")
    hospital_default = x.SubElement(hospital,"default")
    hospital_default.text = " "
    root.append(hospital)
    admin = x.Element("Admin")
    root.append(admin)
    admin_cred = x.SubElement(admin,"admin")
    admin_cred.text = "password"
    tree = x.ElementTree(root)
    with open("credentials.xml",'wb+') as f:
        tree.write(f)
"""


def credentials_addition(usertype,username,password):
    tree_read = x.parse("credentials.xml")
    root = tree_read.getroot()
    for i in root:
        if usertype==i.tag:
            provider = i.tag
            break
    provider_user = x.SubElement(provider,username)
    provider_user.text = password
    tree_write = x.ElementTree(root)
    with open("credentials.xml",'wb+') as f:
        tree_write.write(f)

@app.route("/", methods=['GET', 'POST'])
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
        return render_template("user_homepage.html", row_length=int(row_length), prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image_list=image_list)
    else:
        return redirect("/")


@app.route("/Login", methods=['GET', 'POST'])
def loginpage():
    if request.method == "POST" and not session.get('uname'):
        username = request.form['uname']
        password = request.form['pwd']
        # credentials_generator()
        tree = x.parse('credentials.xml')
        root = tree.getroot()
        for i in root:
            login_ids[i[0].tag] = i[0].text
        if username in login_ids:
            if password == login_ids[username]:
                session['uname'] = username
                return redirect("/Home")
            else:
                message = 'PASSWORD is incorrect'
                flash(message)
                return render_template("login.html")
        else:
            flash('Username not found, Please register...')
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/Logout",methods=['GET', 'POST'])
def logout():
    session.pop('uname',None)
    return redirect("/")


@app.route("/Registration",methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usertype = request.form['user_type']
        provider = request.form['provider']
        spl_char = ['%','!','@','#','$','^','&','*','(',')','_','-','=','+']
        upper_char = string.ascii_uppercase
        lower_char = string.ascii_lowercase
        number_char = range(0,9)
        username = request.form['uname']
        password = request.form['pwd']
        message="Please use \n Password length >8 character \n one Upper character \n one lower character \n one number \n special character(@,#,!,etc) "
        if len(password)<8:
            flash(message)
            return redirect("/Registration")
        for i in password:
            if i in spl_char or i in upper_char or i in lower_char or i in number_char:
                continue
        email = request.form['email']
        if '@' not in email or "dbs.ie" not in email:
            flash("Incorrect email id")
            return redirect("/Registration")
        phone_no = request.form['num']
        if not int(phone_no) or len(phone_no) > 10:
            flash("Incorrect phone number")
            return redirect("/Registration")
        credentials_addition(usertype,username,password)
        return redirect('/Login')
    else:
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
    if session.get('uname'):
        return render_template("products.html", row_length=int(row_length), prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image_list=image_list,session_value=session.get('uname'))
    else:
        return render_template("products.html", row_length=int(row_length), prod_ids=prod_ids, prod_names=prod_names, prod_descs=prod_descs, image_list=image_list,session_value=session.get('uname'))


@app.route("/<int:prod_id>",methods=['GET','POST'])
def product_page(prod_id):
    cursor = Database_Connection()
    cursor.execute("SELECT prod_name,prod_description,prod_size,v_id from product where prod_id=?",prod_id)
    prod_values = cursor.fetchall()
    prod_name = prod_values[0][0]
    prod_description = prod_values[0][1]
    prod_size=prod_values[0][2]
    v_id=prod_values[0][3]
    cursor.execute("SELECT v_name,v_phone,v_email,v_website from vendor where v_id=?",v_id)
    vend_values = cursor.fetchall()
    v_name = vend_values[0][0]
    v_phone= vend_values[0][1]
    v_email= vend_values[0][2]
    v_website= vend_values[0][3]
    cursor.execute("SELECT prod_image from prod_images where prod_id=?",prod_id)
    image_val = cursor.fetchval()
    if image_val is not None:
        filename = "image_" + str(prod_id) + ".png"
        image_new_loc = image_loc + filename
        with open(image_new_loc, "wb") as f:
            f.write(image_val)
    else:
        image_new_loc = image_loc + "images/blank.png"
    return render_template('product_page.html',prod_name=prod_name,prod_description=prod_description,prod_size=prod_size,prod_image=image_new_loc,v_name=v_name,v_website=v_website,v_phone=v_phone,v_email=v_email)


@app.route("/New_Products", methods=['GET', 'POST'])
def new_products():
    image_loc = app.config['UPLOADED_IMAGES_DEST']+'/'
    if request.method == "POST":
        Prod_Name = request.form['Prod_Name']
        Description = request.form['Description']
        Prod_Size = request.form['Prod_Size']
        files = request.files['photos']
        file_name = files.filename
        files.save(image_loc + file_name)
        with open(image_loc+file_name, 'rb') as f:
            bin_data = f.read()

        prod_Dataentry(Prod_Name,Prod_Size,Description,bin_data)
        message = "New Product added"
        flash(message)
        return redirect('/New_Products')
    else:
        allVendors_list = []
        handler = Database_Connection()
        handler.execute("SELECT V_NAME FROM VENDOR")
        allVendors = handler.fetchall()
        for i in allVendors:
            allVendors_list.append(i[0])
        return render_template('new_product_form.html',message=None,allVendors=allVendors_list)


@app.route("/OnDemandRequest",methods = ['GET', 'POST'])
def On_Demand_Request():
    if session.get('uname'):
        req_ids = []
        req_titles = []
        req_descs = []
        image_list = []
        cursor = Database_Connection()
        cursor.execute("SELECT req_id,req_title,req_description from OnDemand_Request")
        all_reqs = cursor.fetchall()

        if len(all_reqs) % 3 == 0:
            row_length = len(all_reqs) / 3
        else:
            row_length = (len(all_reqs) / 3) + 1
        for value in range(len(all_reqs)):
            req_ids.append(all_reqs[value][0])
            req_titles.append(all_reqs[value][1])
            req_descs.append(all_reqs[value][2])

        return render_template("on_demand_request.html", row_length=int(row_length), req_ids=req_ids, req_titles=req_titles, req_descs=req_descs)
    else:
        return redirect("/Login")


@app.route("/New_Request",methods = ['GET', 'POST'])
def new_request():
    if request.method == "POST":
        req_title = request.form['Req_title']
        req_desc = request.form['Req_Description']
        hosp_name = request.form['hospitals']
        req_dimensions = request.form['Dimensions']
        req_budget = request.form['Budget']
        req_nbd = request.form['NeedByDate']
        req_qty = request.form['Quantity']
        req_Dataentry(req_title,req_desc,hosp_name,req_dimensions,req_budget,req_nbd,req_qty)
        message = "New Request created"
        flash(message)
        return redirect('/New_Request')
    else:

        allHospitals_list = []
        handler = Database_Connection()
        handler.execute("SELECT H_NAME FROM HOSPITAL")
        allhospitals = handler.fetchall()
        for i in allhospitals:
            allHospitals_list.append(i[0])
        return render_template("new_request_form.html",message=None,allhospitals=allHospitals_list)


@app.route("/Requests/<int:req_id>",methods = ['GET', 'POST'])
def request_display(req_id):
    cursor = Database_Connection()
    cursor.execute("SELECT * FROM OnDemand_Request where req_id=?",req_id)
    req_values = cursor.fetchall()
    req_title = req_values[0][1]
    req_quantity = req_values[0][2]
    req_dimensions = req_values[0][3]
    req_description = req_values[0][4]
    req_need_by_data = req_values[0][5]
    req_budget = req_values[0][6]
    h_id = req_values[0][7]
    cursor.execute("SELECT h_name,h_phone,h_email FROM hospital where h_id=?", h_id)
    h_values = cursor.fetchall()
    h_name = h_values[0][0]
    h_phone = h_values[0][1]
    h_email = h_values[0][2]
    return render_template("request_page.html",req_title=req_title,req_quantity=req_quantity,req_dimensions=req_dimensions,req_description=req_description,req_need_by_data=req_need_by_data,req_budget=req_budget,h_name=h_name,h_phone=h_phone,h_email=h_email)

@app.route("/AboutUs")
def about_us():
    return render_template("about_us.html",session_value=session.get('uname'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # Remove Host and Port after testing

