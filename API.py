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
            print(create_table_query)
            cursor.execute(create_table_query)
            return jsonify(cursor.fetchall())
        except Exception as e:
            return jsonify(str(e))
        finally:
            mydb.close()


@app.route('/insert_single_record', methods=['POST']) # for calling the API from Postman/SOAPUI
def db_operation_insert_single_record():
    if (request.method=='POST'):
        host1 = request.json['host']
        user1=  request.json['userid']
        password1=request.json['password']
        dbname1 = request.json['database']
        table_name1 = request.json['tablename']
        val1 = int(request.json["val1"])
        val2 = request.json["val2"]

        try:
            mydb = connection.connect(host=host1, user=user1, passwd=password1, use_pure=True)
            cursor = mydb.cursor()  # create a cursor to execute queries
            # insert_table_query = "insert into student_table values(10,'Ravi Dubey', 19830115,'10-C');"
            insert_single_record_query = "INSERT INTO" + " " + dbname1 + "." + table_name1 + " values(" + str(val1) +", " + "'" + val2 +"'" + ");"
            print(insert_single_record_query)
            cursor.execute(insert_single_record_query)
            mydb.commit()
            return jsonify(cursor.fetchall())
        except Exception as e:
            return jsonify(str(e))
        finally:
            mydb.close()



@app.route('/update_single_record', methods=['POST']) # for calling the API from Postman/SOAPUI
def db_operation_update_single_record():
    if (request.method=='POST'):
        host1 = request.json['host']
        user1=  request.json['userid']
        password1=request.json['password']
        dbname1 = request.json['database']
        table_name1 = request.json['tablename']
        dfield1 = request.json["dfield"]
        val1 = request.json["val1"]

        try:
            mydb = connection.connect(host=host1, user=user1, passwd=password1, use_pure=True)
            cursor = mydb.cursor()  # create a cursor to execute queries
            update_single_record_query = "update" + " " + dbname1 + "." + table_name1 + " set "  + dfield1 + " = " +"'" + val1 + "'"
            print(update_single_record_query)
            cursor.execute(update_single_record_query)
            mydb.commit()
            return jsonify(cursor.fetchall())
        except Exception as e:
            return jsonify(str(e))
        finally:
            mydb.close()

@app.route('/select_record', methods=['POST']) # for calling the API from Postman/SOAPUI
def db_operation_select_record():
    if (request.method=='POST'):
        host1 = request.json['host']
        user1=  request.json['userid']
        password1=request.json['password']
        dbname1 = request.json['database']
        table_name1 = request.json['tablename']

        try:
            mydb = connection.connect(host=host1, user=user1, passwd=password1, use_pure=True)
            cursor = mydb.cursor()  # create a cursor to execute queries
            select_record_query = "select " + "*  from " + dbname1 + "." + table_name1
            print(select_record_query)
            cursor.execute(select_record_query)
            return jsonify(cursor.fetchall())
        except Exception as e:
            return jsonify(str(e))
        finally:
            mydb.close()


if __name__ == '__main__':
    app.run()
