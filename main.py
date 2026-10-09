import json

def carregar_quests():
    with open("quests.json", "r", encoding="utf-8") as arquivo:
        quests = json.load(arquivo)
    return quests

def listar_quests(quests):
    for quest in quests:
        if quest["concluida"]:
            status = "Concluída"
        else:
            status = "Pendente"
        print(f'Título: {quest["titulo"]}, '
              f'Prioridade: {quest["prioridade"]}, '
              f'Status: {status}'
        )

def adicionar_quest():
    titulo = input("Digite o título: ")
    prioridade = input("Digite a prioridade (Alta/Média/Baixa): ")
    status = input("Digite o status (Concluída/Pendente): ")
    quest = {
        "titulo": titulo,
        "prioridade": prioridade,
        "concluida": status == "Concluída"}
    return quest

def salvar_quests(quests):
    with open("quests.json", "w", encoding="utf-8") as arquivo:
        json.dump(quests, arquivo, ensure_ascii=False, indent=4)

def menu():
    quests = carregar_quests()
    print("Seja bem-vindo ao Quest Manager!")
    while True:
        print()
        print("1 - Listar quests")
        print("2 - Adicionar quest")
        print("3 - Excluir quest")
        print("4 - Mudar status")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1": #listar quests
            listar_quests(quests)
        elif opcao == "2": #adicionar quests
            quest = adicionar_quest()
            quests.append(quest)
            salvar_quests(quests)
        elif opcao == "3": #excluir quests
            titulo = input("Digite o título da quest a ser excluída: ")
            quests = [quest for quest in quests if quest["titulo"] != titulo]
            salvar_quests(quests)
        elif opcao == "4": #mudar status
            titulo = input("Digite o título da quest a ser alterada: ")
            for quest in quests:
                if quest["titulo"] == titulo:
                    novo_status = input("Digite o novo status (concluido/pendente): ")
                    if novo_status.lower() == "concluida":
                        quest["concluida"] = True
                    else:
                        quest["concluida"] = False
        elif opcao == "0": #sair
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
