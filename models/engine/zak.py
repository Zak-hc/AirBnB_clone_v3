from DBStorage import DBStorage

db_storage = DBStorage()

data = db_storage.execute_sql_query('SELECT * FROM table_name WHERE condition')

print(data)
