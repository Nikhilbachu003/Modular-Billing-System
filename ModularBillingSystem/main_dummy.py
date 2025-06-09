from database_dummy import DataBase
from Authentication import customer
from database_dummy import menu
from service import bill
from valinix import is_valid_password

DB=DataBase.dataB( )
Menuu=menu.dataB()
Customer=customer.cust(DB,Menuu)
Menu_details=([("kaju panner biryani",280),("palak panner",160),("paneer butter masala",160),("pameer tikka masala",310),("kaju curry",310),("paneer bhurji",310),("ginger paneer",290),("crispy corn",200),("baby corn",190),("curd rice",180),("dal rice",160),])
if not Menuu.fetch_menu():
    for item_name,price in Menu_details:
        Customer.menu_details(item_name,price)
while True:
    print('''--------------WELCOME TO SANTOSH DHABA----------------------------''')
    choice=int(input('''
                    press 1 to signin : 
                    press 2 to login : 
                    press 3 to exit : 
                    '''))
    if choice==1:
        name=input("Enter The Name :")
        number=input("Enter The Number : ")
        email=input("Enter the email : ")
        password=input("enter the password : ")
        if is_valid_password(password):
            Customer.create_customer(name,number,email,password)
            print("the data inserted sucessfully")
        else:
            print('''Invalid password !!!!!
                  Note:
                    password must contain atleast 1 uppercase 
                    password must contain atleast 1 Lowercase
                    password must contain atleast 1 Special character ''')
    elif choice==2:
        email=input("Enter The email :")
        password=input("Enter The password : ")
        user=Customer.get_details_email(email)
        if user:
            stored_password=user[4]
            if password==stored_password:
                print("login is sucessfull")
                print("\n----------SANTOSH DHABA MENU--------")
                Customer.display_menu()
                cart=bill.take_order(Menuu)
                bill.generate_bill(cart)
            else:
                print("password is wrong")
        else:
            print("email is not found !!!!!!!!!!")
    elif choice==3:
        print("quit")
        break
    else:
        print("invalid choice ! choose  your option wisely.")
                    
    