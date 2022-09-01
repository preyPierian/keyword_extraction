from keyword_extraction_library import keyword_extraction

search_list = "random_words"

test = keyword_extraction(search_list,["cat","rat","rough","mat", "tough", "hot"],"gh")

test.sql_connection("localhost","root","root")

test.sql_setup(test.cursor)

test.sql_add_entries(test.found_keywords,test.insert_template,test.cursor,test.db)