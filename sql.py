# viewer sqlite https://inloop.github.io/sqlite-viewer/
# to run the sql "python3 sql.py"
import sqlite3
connection = sqlite3.connect('sql_data.db')
# connection.row_factory=sqlite3.Row #get row.key or row['id']
cursor = connection.cursor()

# create table
# cursor.execute('CREATE TABLE question(id INTEGER PRIMARY KEY ,name TEXT)')
# cursor.execute('INSERT INTO question VALUES(?,?)',(1,'what my name?')) #add new row
# cursor.execute('INSERT INTO question(name) VALUES(?)',('what my last name?',))  # add new row auto id
# cursor.execute('SELECT * FROM question WHERE id=?',(1,)) #read from sql
# cursor.execute("DELETE FROM question WHERE id=?", "6") #DELETE row
# cursor.execute('UPDATE question SET id=6 WHERE id=7')  # update row
# row=cursor.fetchone() #get the rows return work with while loop
# rows=cursor.fetchall() #get all rows into rows work with for loop
# id=row[0] #save data

# print all rows
# cursor.execute('SELECT * FROM question')
# row = cursor.fetchone()
# while row is not None:
#    id = row[0]
#    row=cursor.fetchone()
# connection.commit()  # push to sql
# connection.close()


def getAllRows(data):
    cursor.execute('SELECT * FROM question')
    row = cursor.fetchone()
    while row is not None:
        # id = row[0]
        # que = row[1]
        # answer = row[2]
        # op1 = row[3]
        # op2 = row[4]
        # op3 = row[5]
        # op4 = row[6]
        row = cursor.fetchone()


def checkAnswer(op, id):
    cursor.execute('SELECT answer FROM question WHERE id=?', (id,))
    opIn = cursor.fetchone()
    if (opIn[0] == op):
        return True
    else:
        return False


def getQuesNums():  # get number of rows in table
    cursor.execute('SELECT id FROM question')
    row = cursor.fetchone()
    while row is not None:
        id = row[0]
        row = cursor.fetchone()
    return id


def addQues(name, answer, op1, op2, op3, op4):
    cursor.execute('INSERT INTO question VALUES(?,?,?,?,?,?,?)',
                   (getQuesNums()+1, name, answer, op1, op2, op3, op4))
    print("add ques")
    connection.commit()
    printSQL()


def printSQL():
    cursor.execute('SELECT * FROM question')
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
