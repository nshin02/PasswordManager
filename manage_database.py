import mysql.connector as mysql
from mysql.connector import Error

def store_password(password, user_email, username, site_url, site_name):
    try:
        connection = connect()
        if (connection.is_connected()):
            print("Connection Established")
        cursor = connection.cursor(buffered=True)

        record = (password, user_email, username, site_url, site_name)

        cursor.execute("INSERT INTO Accounts (password, user_email, username, site_url, site_name) VALUES (%s, %s, %s, %s, %s)", record)
        connection.commit()
    except Error as e:
        print("ERROR: Trouble storing password into server", e)

def connect():
    try:
        connection = mysql.connect(host="localhost",user="root",password="localpass", database="sys")
        return connection
    except:
        print("ERROR: Could not make connection to server.")

def retrieve_password(site_name):
    print(site_name)
    try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        query = (site_name,)
        cursor.execute("SELECT password FROM Accounts WHERE site_name = %s", query)
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ' + result[0])
    except Error as e:
        print("ERROR: Trouble retrieving password from server", e)

def retrieve_username(site_name):
    try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        query = (site_name,)
        cursor.execute("SELECT username FROM Accounts WHERE site_name = %s", query)
        connection.commit()
        result = cursor.fetchone()
        print('Username is: ' + result[0])
    except Error as e:
        print("ERROR: Trouble retrieving username from server", e)


def exec_table_view():
    try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT * FROM Accounts")
        connection.commit()
        result = cursor.fetchall()
        print("Col ID -- Password ----- Email ------ Username ------ Site URL ----- Site Name")
        for row in result:
            print(row)
            print("\n")
    except Error as e:
        print("ERROR: Trouble retrieving username from server", e)















