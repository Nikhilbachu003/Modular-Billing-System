class cust:
    def __init__(self,db,DB):
        self.db=db
        self.DB=DB
    def create_customer(self,name,number,email,password):
        self.name=name
        self.number=number
        self.email=email
        self.password=password
        self.db.insert_data(name,number,email,password)
    def login_customer(self,email,password):
        self.email=email
        self.password=password
        self.db.cursor.execute("SELECT * FROM dummy WHERE email=? AND password=?",(email,password))
        result=self.db.cursor.fetchone()
        if result:
            return True
        else:
            return False   
    def get_details_email(self,email):  
        self.email=email
        self.db.cursor.execute('''SELECT * FROM DUMMY WHERE EMAIL=?''',(email,))
        return self.db.cursor.fetchone()
    def menu_details(self,item_name,price):
        self.DB.insert_menu_data(item_name,price)
    def display_menu(self):
        menu_items= self.DB.fetch_menu()
        if not menu_items:
            print("Menu is currently empty.")
            return
        index = 1
        for item in menu_items:
            item_name, price = item
            print(f"{index}. {item_name} - RS{price}")
            index += 1






















 