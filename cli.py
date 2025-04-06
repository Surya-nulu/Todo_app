# from functions import get_todos, write_todos
import functions
import time

day = time.strftime("%b %d ,%Y , %H:%M:%S")
print("It is", day)
while True:
    user_action = input("Type add, show, exit, complete or edit:")
    user_action = user_action.strip()

    if user_action.startswith("add") :
        todo = user_action[4:] + '\n'

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        # with -- context manager is preferred over above method for reading a file.

        todos = functions.get_todos()

        todos.append(todo)

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()
        functions.write_todos(todos)
    elif user_action.startswith("show") :

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f"{index + 1}-{item}")
    elif user_action.startswith("edit"):
        try :
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            print(todos[number])
            todos[number] = input("enter new todo:") +"\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            todo_num = int(user_action[9:])
            todos = functions.get_todos()

            todo_to_remove = todos[todo_num - 1].strip('\n')
            todos.pop(todo_num - 1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} is removed for the todos."
            print(message)
        except IndexError:
            print("There is no item with that number.")
    elif 'exit' in user_action:
        break
    else:
        print("Enter a valid command")
print("bye")
