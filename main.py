from flask import Flask, render_template, request, jsonify
from Database_conn import mysql_conn,cassandrasql_conn

app = Flask(__name__)

@app.route('/create_table2', methods=['POST']) # for calling the API from Postman/SOAPUI
def db_operation_createtable():
    if (request.method=='POST'):
        dbname = request.json['dbname']
        database = request.json['database']
        table_name = request.json['tablename']
        field1 = request.json["field1"]
        dfield1 = request.json["dtypefield1"]
        # dlength1 = int(request.json["dlength1"])
        field2 = request.json["field2"]
        dfield2 = request.json["dtypefield2"]
        # dlength2 = int(request.json["dlength2"])
        # print(dbname)
        if dbname == "mysql":
            try:
                mydb = mysql_conn()
                cursor = mydb.cursor()
                create_table_query = "CREATE TABLE if not exists {}{}{}{}{}{};".format(database,table_name,field1,dfield1,field2,dfield2)
                print(create_table_query)
                cursor.execute(create_table_query)
                print("table created")
                return jsonify("sql connection established" + str(mydb))
            except Exception as e:
                return jsonify(str(e))
            finally:
                mydb.close()

        elif dbname == "cassandra":
            try:
                mydb = cassandrasql_conn()
                cursor = mydb.cursor()
                create_table_query = "CREATE TABLE if not exists {}{}{}{}{}{};".format(database,table_name,field1,dfield1,field2,dfield2)
                print(create_table_query)
                cursor.execute(create_table_query)
                return jsonify(cursor.fetchall())
            except Exception as e:
                return jsonify(str(e))
            finally:
                mydb.close()


if __name__ == '__main__':
    app.run()