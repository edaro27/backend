from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'tasks.db'

task_list=[]

#When app restarts, if there is already a table, grab largest id
# with sqlite3.connect(DATABASE) as conn:
#     c = conn.cursor()
#     c.execute("SELECT MAX(id) FROM tasks")
#     max_id = c.fetchall()
#     print(max_id)

global id_count

#GET retrieves a list of all tasks
#POST creates a new task that was typed in the form
@app.route('/', methods = ['POST', 'GET'])
def index(id_count):
    if request.method == 'POST':
        task_content = request.form['content']
        id_count = id_count+1
        task_list.append({"id": id_count, "task": task_content})

    return render_template("index.html", task_list=task_list)

#GET returns a list of all tasks
@app.route('/tasks')
def tasks():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM tasks")
        task_list = c.fetchall()
        response = {}
        for task in task_list: #each task is a tuple: (1, pony)
            response[task[0]] = task[1]
        return jsonify(response)

#GET retrieves the task based on the id
@app.route('/tasks/<id>')
def get_task(id):
    task_id = int(id)
    for item in task_list:
        if item["id"] == task_id:
            return jsonify({"task":item["task"]})
    return "No tasks have that id"

#POST creates a new task by passing JSON to the API
@app.route('/tasks/', methods=['POST'])
def post_task():
    #print(f"There was a {request.method} request")
    #print(f"The parameters are:{request.args}")

    data = request.get_json()
    global id_count
    id_count += 1
    # task_list.append({"id": new_id, "task": data["task"]})

# use with as context manager
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tasks VALUES (:id, :task)",{'id':id_count, 'task':data["task"]})

    response = {
        "Received": data,
        "New Task ID": id_count,  
        "message": "JSON received"
    }
    return jsonify(response)

#PUT updates the task name
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    item_id = int(id)-1
    task_list[item_id] = {"id":id, "task": data["task"]}
    return task_list[item_id]

#DELETE removes a task
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    item_id = int(id)
    for i in task_list:
        if i["id"] == item_id:
            removed_index = task_list.index(i)
            del task_list[removed_index]
            return task_list
        

if __name__ == "__main__":
    #Initialize db and create table if it doesn't exist
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER, task TEXT)''')
        c.execute("SELECT MAX(id) FROM tasks")
        max_id = c.fetchone()
        id_count = max_id[0]
        conn.commit()

    app.run(debug=True)



"""
Sample curl request

curl -X POST http://127.0.0.1:5000/tasks/post_task \
-H "Content-Type: application/json" \
-d '{"task": "Jill Li"}'

"""