import sqlite3

#can pass a file or have an in memory database
conn = sqlite3.connect('tasks.db') 
#pass ':memory:' instead for db to live in ram, clean db in every run


#create a cursor to run sql commands
c = conn.cursor()
# c.execute("PRAGMA table_info(tasks)")
# c.execute("PRAGMA index_info(idx_tasks_user_id)")
# columns=c.fetchall()
# for col in columns:
#     print(col)
# c.execute("DROP TABLE users")
# c.execute("""

#         CREATE TABLE tasks (
#         task_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         task_title TEXT NOT NULL,
#         task_status TEXT CHECK(task_status IN('pending','in_progress','done')) NOT NULL DEFAULT 'pending',
#         user_id INTEGER NOT NULL,
#         due_date DATETIME,
#         created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        
#         FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
#         )

# """)

# c.execute("""
# CREATE TABLE users (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_name TEXT NOT NULL
# )
# """)

# c.execute("INSERT INTO users (user_name) VALUES (:user_name)", {'user_name':'clara'})
# c.execute("SELECT * FROM users")
# print(c.fetchall())

# c.execute("SELECT name FROM sqlite_master WHERE type='table'")
# tables = c.fetchall()

# for table in tables:
#     print(table[0])

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

# c.execute("""
          
# SELECT tasks.user_id, tasks.task_title, users.user_name 
#           FROM tasks
#           JOIN users ON tasks.user_id = users.user_id
#           WHERE users.user_name = 'clara'
#           """
#           )

c.execute("SELECT * FROM tasks")

# c.execute("CREATE INDEX idx_tasks_user_id ON tasks(user_id)")

#An index is a data structure that letes the database find rows faster without scanning the whole table. 
# Useful for frequently used queries. But uses extra storage. Like a sorted list or b-tree.


# c.fetchone will get the next row in results and only return that row
# c.fetchmany() takes number for how many rows to return
print(c.fetchall())

# print(c.fetchone())


#commits current transaction
conn.commit()

#close connection to db
conn.close()