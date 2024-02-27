import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table,retrieve 
cursor=connection.cursor()

##create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT );
"""

cursor.execute(table_info)

##insert some more records

cursor.execute('''Insert Into STUDENT values('Jatin','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Aman','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Abhi','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Manish','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Harsh','DEVOPS','A',35)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse 
connection.commit()
connection.close()
