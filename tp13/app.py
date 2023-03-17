from flask import Flask
from TodoDAO import TodoDAO
from Todo import Todo


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/todos")
def todos():
    todoDAO = TodoDAO("todos.db")
    html="<table>"
    for todo in todoDAO.findAll():
        html+=f"""<tr>
        <td>{todo.id}</td>
        <td>{todo.title}</td>
        <td>{todo.completed}</td>
        </tr>"""
        print(todo)    
    return html