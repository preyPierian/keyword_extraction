import imp
from keyword_extraction_library import keyword_extraction
from sql_library import sql_connector

search_list = "random_words"

test = keyword_extraction(search_list,["cat","rat","rough","mat", "tough", "hot"],"ough")

sql_connection = sql_connector("localhost","root","root")

sql_connection.sql_setup(test.search_word,test.list_name)

sql_connection.sql_add_subwords(test.found_keywords,test.list_name)