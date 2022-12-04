from flask import Flask,request,render_template
import os
import pyodbc

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'uploads'


@app.route("/")#URL leading to method
def index():  # Name of the method
    return render_template("index.html")


@app.route("/submission", methods=['GET', 'POST'])
def submission():
    image_loc = ''
    if request.method == "POST":
        fname = request.form['fname']
        files = request.files['photo']
        file_name = files.filename
        print(file_name)
        files.save(app.config['UPLOADED_IMAGES_DEST']+'/'+file_name)
        with open(os.path.join(app.config['UPLOADED_IMAGES_DEST'],file_name), 'rb') as f:
            bin_data = f.read()
        Database_Connection(bin_data)
        image_val = Data_Retrieval(bin_data)
        image_loc = app.config['UPLOADED_IMAGES_DEST'] +'/'+file_name
        with open(image_loc,"wb") as f:
            f.write(image_val)

        return render_template('submission.html', image=image_loc)
    else:
        return render_template('submission.html', image=image_loc)


def Database_Connection(binary_value):
    server = 'tcp:avadb01.database.windows.net'
    database ='AVA_DB_1'
    username ='SAadmin'
    password ='Dublin@098'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    cursor = connection.cursor()
    command = "INSERT INTO Images(col_image) VALUES(?)"
    cursor.execute(command,binary_value)
    cursor.commit()

def Data_Retrieval(filename):
    server = 'tcp:avadb01.database.windows.net'
    database = 'AVA_DB_1'
    username = 'SAadmin'
    password = 'Dublin@098'
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';ENCRYPT=yes;UID=' + username + ';PWD=' + password)
    cursor = connection.cursor()
    cursor.execute("SELECT ? from Images",filename)
    image_value = cursor.fetchval()
    return image_value


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) # Remove Host and Port after testing

