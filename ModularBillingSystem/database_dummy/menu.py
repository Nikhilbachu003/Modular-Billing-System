import sqlite3
class dataB:
    def __init__(self,db=r"C:\Users\DELL\OneDrive\Desktop\dummy\database_dummy\menu.db"):
        self.DB=db
        self.conn=sqlite3.connect(self.DB)
        self.cursor=self.conn.cursor()
        
    def insert_menu_data(self,item_name,price):
        self.item_name=item_name
        self.price=price
        self.cursor.executemany('''insert or ignore into menu(item_name,price) values(?,?)''',[(item_name,price)])
        self.conn.commit()
    def fetch_menu(self):
        self.cursor.execute("select item_name,price from menu")
        return self.cursor.fetchall()
    def get_item_by_id(self,item_id):
        self.cursor.execute("SELECT item_name,price FROM menu WHERE item_id=?",(item_id,))
        return self.cursor.fetchone()