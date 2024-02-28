def adicionar_tarefa(lista_tarefas):
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"Título": titulo, "Descrição": descricao, "Concluída": False}
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def mostrar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for idx, tarefa in enumerate(lista_tarefas, 1):
            status = "Concluída" if tarefa["Concluída"] else "Pendente"
            print(f"{idx}. {tarefa['Título']} - ({status})")


def editar_tarefa(lista_tarefas):
    mostrar_tarefas(lista_tarefas)
    indice = int(input("Digite o número da tarefa que deseja editar: ")) - 1
    if 0 <= indice < len(lista_tarefas):
        titulo = input("Digite o novo título da tarefa: ")
        descricao = input("Digite a nova descrição da tarefa: ")
        lista_tarefas[indice]["Título"] = titulo
        lista_tarefas[indice]["Descrição"] = descricao
        print("Tarefa editada com sucesso!")
    else:
        print("Número de tarefa inválido.")

def marcar_concluida(lista_tarefas):
    mostrar_tarefas(lista_tarefas)
    indice = int(input("Digite o número da tarefa concluída: ")) - 1
    if 0 <= indice < len(lista_tarefas):
        lista_tarefas[indice]["Concluída"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def excluir_tarefa(lista_tarefas):
    mostrar_tarefas(lista_tarefas)
    indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
    if 0 <= indice < len(lista_tarefas):
        del lista_tarefas[indice]
        print("Tarefa excluída com sucesso!")
    else:
        print("Número de tarefa inválido.")

# Lista de tarefas
tarefas = []

while True:
    print("\n===== Sistema de Gerenciamento de Tarefas =====")
    print("1. Adicionar Tarefa")
    print("2. Mostrar Tarefas")
    print("3. Editar Tarefa")
    print("4. Marcar Tarefa como Concluída")
    print("5. Excluir Tarefa")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(tarefas)
    elif opcao == "2":
        mostrar_tarefas(tarefas)
    elif opcao == "3":
        editar_tarefa(tarefas)
    elif opcao == "4":
        marcar_concluida(tarefas)
    elif opcao == "5":
        excluir_tarefa(tarefas)
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Escolha novamente.")
