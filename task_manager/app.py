from flask import Flask

app = Flask(__name__)

task_list=[{"id":1, "name":"clean"}, {"id":2, "name": "sweep"}]

@app.route('/')
def index():
    return 'Hello World'

@app.route('/tasks')
def tasks():
    return task_list

@app.route('/tasks/<id>')
def task_id(id):
    index = int(id)-1
    return task_list[index]["name"]

if __name__ == "__main__":
    app.run(debug=True)