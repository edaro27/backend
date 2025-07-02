from flask import Flask, request

app = Flask(__name__)

task_list=[]

@app.route('/')
def index():
    return 'Hello World'

@app.route('/tasks')
def tasks():
    return task_list

@app.route('/tasks/<id>')
def task_id(id):
    for item in task_list:
        if item["id"] == int(id):
            return item["name"]
    return "No tasks have that id"

@app.route('/tasks/post_task', methods=['POST'])
def post_task():
    data = request.get_json()
    task_list.append({"id": data["id"], "name": data["name"]})

    response = {
        "received": data,
        "message": "JSON received"
    }

    return response

if __name__ == "__main__":
    app.run(debug=True)