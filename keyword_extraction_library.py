import keyword
import mysql.connector

#test comment

class found_word :
    def __init__(self, word, start_index, end_index):
        self.word = word
        self.start_index = start_index
        self.end_index = end_index
        

class keyword_extraction :
    def __init__(self, list_name, keywords, search_word):
        self.keywords = keywords
        self.search_word = search_word
        self.list_name = list_name
        #self.insert_template= ""
        keywords_array = self.keywords
        search_word = self.search_word
        output = []

        for current_word in keywords_array :
            # If subword found
            if search_word in  current_word :
                print("Found in " + current_word)
                start_indexes = [i for i in range(len(current_word)) if current_word.startswith(search_word, i)]
                for current_start_index in start_indexes :
                    # assuming 0 indexing, this is what python uses
                    substring_index_start = current_start_index
                    substring_index_end = substring_index_start + len(search_word) - 1
                    data = (found_word(current_word,substring_index_start,substring_index_end))
                    output.append(data)
                    print(str(substring_index_start) + "," + str(substring_index_end))
            else : 
                print("Not found in " + current_word )
        
        self.found_keywords = output
    
"""  def sql_connection(self,host_name,username,password):
        mydb = mysql.connector.connect(
            host =host_name,
            user =username,
            passwd =password, 
        )
        self.db = mydb
        self.cursor = self.db.cursor()

    def sql_setup(self, my_cursor) :
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.search_word+";")
        my_cursor.execute("USE " +self.search_word)
        my_cursor.execute("DROP TABLE IF EXISTS "+ self.list_name +";")
        my_cursor.execute("CREATE TABLE "+ self.list_name +" (word VARCHAR(255), start_index INTEGER(10), end_index INTEGER(10), keyword_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
        self.insert_template = ("INSERT INTO "+self.list_name+" (word,start_index,end_index) VALUES (%s,%s,%s) ")

    def sql_add_entries(self,array,insert_template,cursor,db):
        for x in array :
            print(x.word)
            cursor.execute(insert_template,(x.word,x.start_index,x.end_index))
        db.commit()
    """
