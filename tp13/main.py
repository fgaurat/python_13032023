import requests
import sqlite3
from TodoDAO import TodoDAO
from Todo import Todo

def main():
    todoDAO = TodoDAO("todos.db")
    for todo in todoDAO.findAll():
        print(todo)
    
def main_save():
    url="https://jsonplaceholder.typicode.com/todos"
    response =  requests.get(url)
    todos = response.json()
    todoDAO = TodoDAO("todos.db")
    for todo in todos:
        todo = Todo(title = todo['title'],completed=todo['completed'],userId=todo['userId'],)
        todoDAO.save(todo)
    
    

def main_dirty():
    url="https://jsonplaceholder.typicode.com/todos"
    response =  requests.get(url)
    todos = response.json()
    
    with sqlite3.connect("todos.db") as con:
        cur = con.cursor()
        for todo in todos:
            sql_insert = f"""INSERT INTO todo_tbl(title,completed,user_id)
VALUES('{todo['title']}',{todo['completed']},{todo['userId']})
"""
            cur.execute(sql_insert)
        con.commit() 

    

    

if __name__=='__main__':
    main()

