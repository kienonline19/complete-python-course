import sqlite3

# connect to a local database
connection = sqlite3.connect("data.db")

# get a cursor for that connection
# to execute SQL Queries
cursor = connection.cursor()

sql_command = ''
cursor.execute(sql_command)

"""
save the contents of whatever changes you've made
to the disc
"""
connection.commit()

connection.close()
