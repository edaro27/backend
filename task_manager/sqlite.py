import sqlite3

#can pass a file or have an in memory database
conn = sqlite3.connect('tasks.db') 
#pass ':memory:' instead for db to live in ram, clean db in every run


#create a cursor to run sql commands
c = conn.cursor()

# c.execute("""CREATE TABLE tasks (
#           id integer,
#           task text
#           )""")

# c.execute("INSERT INTO tasks VALUES (10, 'play')")
# c.execute("INSERT INTO tasks VALUES (11, 'rest')")

# c.execute("INSERT INTO tasks VALUES ({}, '{}')".format(task.id, task.task))
# c.execute("DROP TABLE tasks")

#SELECT * FROM tasks where task='sleep'
#SELECT statements never need to be committed like INSERTS, UPDATES, and DELETES. Just have to do the c.execute

# c.execute("""UPDATE employees SET pay = :pay
#           WHERE first = :first AND last = :last""",
#           {'first': emp.first, 'last': emp.last, 'pay': pay})

# c.execute("DELETE from employees WHERE first = :first AND last = :last",
#           {'first': emp.first, 'last':emp.last})


c.execute("SELECT * FROM tasks")


# c.fetchone will get the next row in results and only return that row
# c.fetchmany() takes number for how many rows to return
# c.fetchall()

# print(c.fetchone())
print(c.fetchall())


#commits current transaction
conn.commit()

#close connection to db
conn.close()