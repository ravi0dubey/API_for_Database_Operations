import mysql.connector as connection
def mysql_conn():
    mydb = connection.connect(host="localhost", user="devuser", passwd="Logitech1234#", use_pure=True)
    return mydb

def cassandrasql_conn():
    mydb = connection.connect(host="localhost", user="devuser", passwd="Logitech1234#", use_pure=True)
    return mydb