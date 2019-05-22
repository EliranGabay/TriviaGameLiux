# viewer sqlite https://inloop.github.io/sqlite-viewer/
# to run the sql "python3 sql.py"
import sqlite3
connection = sqlite3.connect('sql_data.db')
# connection.row_factory=sqlite3.Row #get row.key or row['id']
cursor = connection.cursor()

# create table
#cursor.execute('CREATE TABLE question(id INTEGER PRIMARY KEY,name TEXT)')
# cursor.execute('INSERT INTO question VALUES(?,?)',(1,'what my name?')) #add new row
cursor.execute('INSERT INTO question(name) VALUES(?)',('what my last name?',))  # add new row auto id
# cursor.execute('SELECT * FROM question WHERE id=?',(1,)) #read from sql
# row=cursor.fetchone() #get the rows return work with while loop
# rows=cursor.fetchall() #get all rows into rows work with for loop
# id=row[0] #save data

# print all rows
#cursor.execute('SELECT * FROM question')
# row=cursor.fetchone()
# while row is not None:
#    id=row[0]
#    row=cursor.fetchone()
connection.commit()  # push to sql
