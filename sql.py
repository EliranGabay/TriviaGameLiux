#!/usr/bin/python3
# viewer sqlite https://inloop.github.io/sqlite-viewer/
# to run the sql "python3 sql.py"
import sqlite3
connection = sqlite3.connect('sql_data.db')
# connection.row_factory=sqlite3.Row #get row.key or row['id']
cursor = connection.cursor()

# create table
# cursor.execute('CREATE TABLE score(id INTEGER PRIMARY KEY ,name TEXT,score INTEGER)')
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


def addScore(name, score):
    cursor.execute('INSERT INTO score VALUES(?,?,?)',
                   (getScoresNums()+1, name, score))
    print("add score")
    connection.commit()


def getAllScore():
    listS = []
    cursor.execute('SELECT * FROM score')
    row = cursor.fetchone()
    while row is not None:
        name = row[1]
        score = row[2]
        listS.append([name, score])
        row = cursor.fetchone()
    return listS


def getAllQues():
    listQ = []
    cursor.execute('SELECT * FROM question')
    row = cursor.fetchone()
    while row is not None:
        id = row[0]
        que = row[1]
        answer = row[2]
        op1 = row[3]
        op2 = row[4]
        op3 = row[5]
        op4 = row[6]
        listQ.append([id, que, answer, op1, op2, op3, op4])
        row = cursor.fetchone()
    return listQ


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


def getScoresNums():  # get number of rows in table
    cursor.execute('SELECT id FROM score')
    row = cursor.fetchone()
    id = 0
    while row is not None:
        id = row[0]
        row = cursor.fetchone()
    return id


def addQues(name, answer, op1, op2, op3, op4):
    cursor.execute('INSERT INTO question VALUES(?,?,?,?,?,?,?)',
                   (getQuesNums()+1, name, answer, op1, op2, op3, op4))
    print("add ques")
    connection.commit()
    #printSQL()


def read_from_file():
    with open("question.txt") as myFile:
        text = myFile.read()
        result = text.split("$")
    for i in result:
        temp=i.split("@")
        addQues(temp[0], temp[5][:3], temp[1][2:len(temp[1])-1], temp[2][2:len(temp[2])-1], temp[3][2:len(temp[3])-1], temp[4][2:len(temp[4])-1])
    


def printSQL():
    cursor.execute('SELECT * FROM question')
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
