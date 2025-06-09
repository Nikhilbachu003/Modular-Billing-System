import sqlite3

class dataB:
    def __init__(self,db=r"C:\Users\DELL\OneDrive\Desktop\dummy\database_dummy\DB.db"):
        self.db=db
        self.conn=sqlite3.connect(self.db)
        self.cursor=self.conn.cursor() 
    def insert_data(self,name,number,email,password):
        self.name=name
        self.number=number
        self.email=email
        self.password=password
        self.cursor.execute('''insert into dummy(name,number,email,password) values(?,?,?,?)''',(name,number,email,password))
        self.conn.commit()

    
    
    
        
