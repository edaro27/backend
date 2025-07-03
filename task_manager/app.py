from flask import Flask, request, jsonify
import random

app = Flask(__name__)

task_list=[]

@app.route('/')
def index():
    return 'Hello World'

@app.route('/tasks')
def tasks():
    return jsonify(task_list)

@app.route('/tasks/<id>')
def get_task(id):
    task_id = int(id)
    for item in task_list:
        if item["id"] == task_id:
            return jsonify({"name":item["name"]})
    return "No tasks have that id"

@app.route('/tasks/post_task', methods=['POST'])
def post_task():
    print(f"There was a {request.method} request")
    print(f"The parameters are:{request.args}")

    data = request.get_json()

    #Creates random ID and assigns is to the new task
    new_id = random.randint(1,100)
    task_list.append({"id": new_id, "name": data["name"]})

    response = {
        "Received": data,
        "New Task ID": new_id,
        "message": "JSON received"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)



"""
Sample curl request

curl -X POST http://127.0.0.1:5000/tasks/post_task \
-H "Content-Type: application/json" \
-d '{"name": "Jill Li"}'

"""