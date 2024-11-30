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






# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('q: quitter')
    print('========================')
    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todos()