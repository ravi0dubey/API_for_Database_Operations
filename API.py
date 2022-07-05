import mysql.connector as connection
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/create_database', methods=['POST']) # for calling the API from Postman/SOAPUI
def db_operation_createdb():
    if (request.method=='POST'):
        host1 = request.json['host']
        user1=  request.json['userid']
        password1=request.json['password']
        dbname = request.json['database']
        try:
            # mydb = connection.connect(host="localhost", user="devuser", passwd="Logitech1234#", use_pure=True)
            mydb = connection.connect(host= host1, user = user1, passwd = password1,use_pure=True)
            # check if the connection is established
            create_db_query = "CREATE DATABASE " + dbname
            cursor = mydb.cursor()  # create a cursor to execute queries
            cursor.execute(create_db_query)
            return jsonify(cursor.fetchall())
        except Exception as e:
            return jsonify(str(e))
        finally:
            mydb.close()

@app.route('/create_table', methods=['POST']) # for calling the API from Postman/SOAPUI
def db_operation_createtable():
    if (request.method=='POST'):
        host1 = request.json['host']
        user1=  request.json['userid']
        password1=request.json['password']
        dbname = request.json['database']
        table_name = request.json['tablename']
        field1 = request.json["field1"]
        dfield1 = request.json["dtypefield1"]
        dlength1 = int(request.json["dlength1"])
        field2 = request.json["field2"]
        dfield2 = request.json["dtypefield2"]
        dlength2 = int(request.json["dlength2"])

        try:
            mydb = connection.connect(host=host1, user=user1, passwd=password1, use_pure=True)
            cursor = mydb.cursor()  # create a cursor to execute queries
            # use_db_query = "use" + dbname
            # cursor.execute(use_db_query)
            # # create_table_query = "CREATE TABLE  student_table(studentid decimal(10) primary key,name varchar(30),age date,classno varchar(30)); "
            create_table_query = "CREATE TABLE" + " " + dbname + "." + table_name + "(" + field1 + " " + dfield1+"("+str(dlength1)+")"+ "," + field2 + " " + dfield2+"("+str(dlength2)+")" +");"
            cursor.execute(create_table_query)
            return jsonify(cursor.fetchall())
        except Exception as e:
            return jsonify(str(e))
        finally:
            mydb.close()

if __name__ == '__main__':
    app.run()
