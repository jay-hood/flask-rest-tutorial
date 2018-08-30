# import sqlite3
#
#
# connection = sqlite3.connect('data.db')
#
# cursor = connection.cursor()
#
# create_table = "CREATE TABLE users (id int, username text, password text)"
# cursor.execute(create_table)
#
# user = (1, 'jay', 'abcd')
# insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# cursor.execute(insert_query, user)
#
# users = [
#     (2, 'simeon', 'defg'),
#     (3, 'josh', 'hijk')
# ]
# cursor.executemany(insert_query, users)
#
# select_query = "SELECT * from users"
# for row in cursor.execute(select_query):
#     print(row)
#
# connection.commit()
# connection.close()

double_list = [[1, 2], [3, 4], [5, 6]]

mapped_nums = [{'name': list_[0], 'price': list_[1]} for list_ in double_list]

print(mapped_nums)