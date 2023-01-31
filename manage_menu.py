from hasher import password
from manage_database import store_password, retrieve_password, retrieve_username, exec_table_view

def menu():
    while 1:
        print("-------Password Manager---------")
        secret_key = input(str("Please enter the secret key to access: "))
        if secret_key != "dbkey":
            print("Incorrect key: Exiting...")
            break
        else:
            print("Welcome to Password Manager!")
            print("1. Create a new password")
            print("2. Find password to a site")
            print("3. Find username to a site")
            print("4. View entire Table")
            print("P. Exit")

            option = input(str("Option: "))
            if option == "1":
                create_password()
            elif option == "2":
                find_password()
            elif option == "3":
                find_username()
            elif option == "4":
                view_table()
            elif option == "P":
                print("Exiting Password Manager...")
                break

def create_password():
    print("Please provide the name of the site or app: ")
    app_name = input()
    print("Please provide a simple password for the site: ")
    plaintext = input()
    passw = password(plaintext, app_name, 12)
    user_email = input('Please provide a user email for this app or site:  ')
    username = input('Please provide a username for this app or site (if applicable: ')

    url = input('Please paste the url to the site that you are creating the password for: ')
    store_password(passw, user_email, username, url, app_name)
    print("Password created and stored into database!")

def find_password():
   print('Please proivide the name of the site or app you want to find the password to')
   app_name = input()
   retrieve_password(app_name)

def find_username():
   print('Please proivide the site name that you want to find the username for')
   site_name = input() 
   retrieve_username(site_name)

def view_table():
    exec_table_view()
menu()