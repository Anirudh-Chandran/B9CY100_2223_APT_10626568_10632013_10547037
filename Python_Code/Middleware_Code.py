from flask import Flask,request,render_template
import os
import pyodbc

prod_insert = """?,?,?,?,?,?)"""

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'uploads'


@app.route("/")#URL leading to method
def index():  # Name of the method
    return render_template("index.html")


@app.route("/submission", methods=['GET', 'POST'])
def submission():
    if request.method == "POST":
        fname = request.form['fname']
        files = request.files['photo']
        file_name = files.filename
        files.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'],file_name))
        with open(os.path.join(app.config['UPLOADED_IMAGES_DEST'],file_name), 'rb') as f:
            bin_data = f.read()
        Database_Connection(bin_data)
        return render_template('submission.html')
    else:
        return "except"


def Database_Connection(binary_value):
    server = 'tcp:avadb01.database.windows.net'
    database ='AVA_DB_1'
    username ='SAadmin'
    password ='Dublin@098'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    cursor = connection.cursor()
    command = "INSERT INTO Product(Prod_id, Prod_Name, Prod_Man_Date, Prod_Man_By, Prod_Dimensions, Prod_Image) VALUES('1', 'X-RAY', 2021-02-28, 'Pharma', '10x10x10',?)"
    cursor.executemany(command,binary_value)
    cursor.commit()
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # indent this line

