from flask import Flask, request, jsonify, render_template, redirect
import random

app = Flask(__name__)

task_list=[]

#GET retrieves a list of all tasks
#POST creates a new task that was typed in the form
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_id = len(task_list)+1
        task_list.append({"id": new_id, "task": task_content})

    return render_template("index.html", task_list=task_list)

#GET returns a list of all tasks
@app.route('/tasks')
def tasks():
    return jsonify(task_list)

#GET retrieves the task based on the id
@app.route('/tasks/<id>')
def get_task(id):
    task_id = int(id)
    for item in task_list:
        if item["id"] == task_id:
            return jsonify({"task":item["task"]})
    return "No tasks have that id"

#POST creates a new task by passing JSON to the API
@app.route('/tasks/post_task', methods=['POST'])
def post_task():
    print(f"There was a {request.method} request")
    print(f"The parameters are:{request.args}")

    data = request.get_json()

    new_id = len(task_list)+1
    task_list.append({"id": new_id, "task": data["task"]})

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
    app.run(debug=True)



"""
Sample curl request

curl -X POST http://127.0.0.1:5000/tasks/post_task \
-H "Content-Type: application/json" \
-d '{"task": "Jill Li"}'

"""