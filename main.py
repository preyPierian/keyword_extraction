import imp
from keyword_extraction_library import keyword_extraction
from sql_library import sql_connector

search_list = "random_words_2"

test = keyword_extraction(search_list,["cat","rat","rough","mat", "tough", "hot"],"ough")

random_words_db = sql_connector("localhost","root","root",test.search_word)
random_words_db.sql_create_table(test.list_name)
random_words_db.sql_add_subwords(test.found_keywords,test.list_name)

input_dp = sql_connector("localhost","root","root","data2")

vegan_food =  (input_dp.sql_query("sku,text","data2.tescoscrape","text LIKE '%vegan%'"))

