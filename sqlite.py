import sqlite3


# connect sqlite 3

connection = sqlite3.connect("student.db")


# create a cursor object to insert record and create table


cursor = connection.cursor()

# table info

table_info = """
create table STUDENT(NAME VARCHAR(25), ClASS VARCHAR(25), 
SECTION VARCHAR(25));

"""

cursor.execute(table_info)

## insert some more records
cursor.execute('''Insert Into STUDENT values('krish', 'Data Science', 'A')   ''')
cursor.execute('''Insert Into STUDENT values('lakshya', 'Web Dev', 'B')   ''')
cursor.execute('''Insert Into STUDENT values('sanchit', 'Data Science', 'B')   ''')
cursor.execute('''Insert Into STUDENT values('kush', 'python', 'C')   ''')
cursor.execute('''Insert Into STUDENT values('bhuvan', 'CAT', 'A')   ''')
cursor.execute('''Insert Into STUDENT values('Aditya', 'data science', 'B')   ''')
cursor.execute('''Insert Into STUDENT values('Arjun', 'BBA', 'A')   ''')

print("The inserted recoreds are ")
data = cursor.execute('''Select * from STUDENT  ''')

for row in data:
    print(row)


connection.commit()
connection.close()

