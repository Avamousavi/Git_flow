todo_list = list()

def lister_todos():
    if len(todo_list) == 0:
        print("Rien a faire")

    for i in range(len(todo_list)):
        print(f"{i+1}. {todo_list[i]}")

def creer_todo():
    status = "A faire"
    title = input("Entrer votre tache: ")

    todo_list.append([title, status])


def modifier_statut_todo():
    title = input('entrer tache a modifier: ')

    if title not in [todo[0] for todo in todo_list]:
        print("Not found")
    else:
        for todo in todo_list:
            if title == todo[0]:
                if todo[1] == "A faire":
                    todo[1] = "Fait"
                else:
                    todo[1] = "A faire"




            

# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('q: quitter')
    print('========================')
    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todo()
        case '3': modifier_statut_todo()
        case 'q': print('Au revoir')
        case _: print('Choix invalide')