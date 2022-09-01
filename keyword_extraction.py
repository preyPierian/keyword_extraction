import mysql.connector
import argparse

# Get inputs for program via flags
parser = argparse.ArgumentParser(description='Gather inputs for program')
parser.add_argument('-l','--list_name',type=str,metavar='', required=True,help = 'Name of list to extract keywords from')
parser.add_argument('-w','--search_word',type=str,metavar='', required=True,help = 'Word to search for')
args = parser.parse_args()

try:
  # Set the list we are extracting keywords from and the search subword
  list_name = args.list_name
  search_word =  args.search_word

  # Create SQL connection
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
  )

  # Create database (named after search word) and table (names after search list ) if they do not exsit
  # One to many relationship between search words and lists
  # To create one to many relationship between lists and search words, swar where search_word and list_name are in SQL code below
  my_cursor = mydb.cursor()
  my_cursor.execute("CREATE DATABASE IF NOT EXISTS "+search_word+";")
  my_cursor.execute("USE " +search_word)
  my_cursor.execute("DROP TABLE IF EXISTS "+ list_name +";")
  my_cursor.execute("CREATE TABLE "+ list_name +" (word VARCHAR(255), start_index INTEGER(10), end_index INTEGER(10), keyword_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

  sql_insert_template = "INSERT INTO "+list_name+" (word,start_index,end_index) VALUES (%s,%s,%s) "

  # Opens csv and extracts words from there
  keywords_file = open(list_name + ".csv", "r")
  # Stored words in an array
  keywords_array = (keywords_file.read()).split(",")
  
  for current_word in keywords_array :
    # If subword found
    if search_word in  current_word :
      print("Found in " + current_word)
      start_indexes = [i for i in range(len(current_word)) if current_word.startswith(search_word, i)]
      for current_start_index in start_indexes :
        # assuming 0 indexing, this is what python uses
        substring_index_start = current_start_index
        substring_index_end = substring_index_start + len(search_word) - 1
        print(str(substring_index_start) + "," + str(substring_index_end))
        my_cursor.execute(sql_insert_template,(current_word,substring_index_start,substring_index_end))
    else : 
      print("Not found in " + current_word )

  mydb.commit()

except FileNotFoundError :
  print ("The list input file does not exsist")
except mysql.connector.errors.ProgrammingError: 
  print("Issue in connection made to MySQL database")
except  mysql.connector.errors :
  print ("Issue occured with SQL database")
except :
  print ("Something went wrong !")