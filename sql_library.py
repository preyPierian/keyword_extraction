
import mysql.connector

class sql_connector :
    def __init__(self,host_name,username,password):
        mydb = mysql.connector.connect(
            host =host_name,
            user =username,
            passwd =password, 
        )
        self.db = mydb
        self.cursor = self.db.cursor()

    def sql_setup(self,database_name,table_name) :
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS "+database_name+";")
        self.cursor.execute("USE " +database_name)
        self.cursor.execute("DROP TABLE IF EXISTS "+ table_name +";")
        self.cursor.execute("CREATE TABLE "+ table_name +" (word VARCHAR(255), start_index INTEGER(10), end_index INTEGER(10), keyword_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
        

    def sql_add_subwords(self,array,table_name):
        for x in array :
            self.cursor.execute(("INSERT INTO "+  table_name +" (word,start_index,end_index) VALUES (%s,%s,%s) "),(x.word,x.start_index,x.end_index))
        self.db.commit()
    
    