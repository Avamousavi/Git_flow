todo_list = list()

def lister_todos():
    if len(todo_list) == 0:
        print("Rien a faire")

    for i in range(len(todo_list)):
        print(f"{i+1}. {todo_list[i]}")
def creer_todos():
    status = "A faire"
    title = input("Entrer votre tache: ")

    todo_list.append([title, status])