from statistics import variance

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):

    """ This function(get_todos) reads the todos.txt file and returns a
    list of to-do items."""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath= FILEPATH):

    """ This function(write_todos) rewrites the todos.txt
    file with updated todos list."""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    # name is variable that is assigned with a string("__main__") by the python.
    print("hello")