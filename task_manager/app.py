from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'tasks.db'

task_list=[]

id_count = 0

#GET retrieves a list of all tasks
#POST creates a new task that was typed in the form
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        default_user_id = 1
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO tasks (task_title, user_id) VALUES (:task_title, :user_id)", {"task_title": task_content, "user_id": default_user_id})
            conn.commit()
        return redirect('/')

    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT task_id, task_title FROM tasks")
        task_list = c.fetchall()

    return render_template("index.html", task_list=task_list)

#GET returns a list of all tasks
@app.route('/tasks')
def get_tasks():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM tasks")
        task_list = c.fetchall()
        response = [{"task_id": task[0], "task_title": task[1], "task_status": task[2], "user_id": task[3], "created_at": task[5]} for task in task_list]
        return jsonify(response)

#         task_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         task_title TEXT NOT NULL,
#         task_status TEXT CHECK(task_status IN('pending','in_progress','done')) NOT NULL DEFAULT 'pending',
#         user_id INTEGER NOT NULL,
#         due_date DATETIME,
#         created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

#GET retrieves the task based on the id
@app.route('/tasks/<id>')
def get_task(id):
    task_id = int(id)
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT task_title FROM tasks WHERE task_id = :task_id", {'task_id':task_id}) #Placeholders good for multiple parameters, readable, less error-prone
        task_title = c.fetchone()
        return jsonify({"task_title": task_title[0]})

#POST creates a new task by passing JSON to the API
@app.route('/tasks/', methods=['POST'])
def post_task():
    #print(f"There was a {request.method} request")
    #print(f"The parameters are:{request.args}")

    data = request.get_json()

# use with as context manager
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tasks (task_title, user_id) VALUES (:task_title, :user_id)",{'task_title':data["task_title"], 'user_id':data["user_id"]})
        new_id = c.lastrowid
        conn.commit()
    
    response = {
        "Received": data,
        "New Task ID": new_id,  
        "message": "JSON received"
    }
    return jsonify(response)

#PUT updates the task name
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task_id = int(id)
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("UPDATE tasks SET task_title = :task_title WHERE task_id = :task_id", {'task_title':data['task_title'], 'task_id':task_id}) 
        conn.commit()
        return {"message": "Task updated", "task_id": task_id, "new_title": data['task_title']}, 200

#DELETE removes a task
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task_id = int(id)
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("DELETE from tasks WHERE task_id = :task_id", {'task_id':task_id}) 
        conn.commit()

        if c.rowcount == 0:
            return {"error": "Task not found"}, 404
        
        return {"message": "Task deleted", "task_id": task_id}, 200


if __name__ == "__main__":
    #Initialize db and create table if it doesn't exist
    #Grab largest id value if table is populated
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                  id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  task TEXT NOT NULL)''')
        conn.commit()

    app.run(debug=True)



"""
Sample curl request

curl -X POST http://127.0.0.1:5000/tasks/post_task \
-H "Content-Type: application/json" \
-d '{"task_title": "Jill Li"}'

"""