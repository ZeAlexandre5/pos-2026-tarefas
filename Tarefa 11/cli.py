import user_wrapper as users
import os

while True:
    print("\nMenu:")
    print("1. Listar usuários")
    print("2. Ver detalhes do usuário")
    print("3. Criar usuário")
    print("4. Atualizar usuário")
    print("5. Deletar usuário")
    print("6. Listar tarefas do usuário")
    print("0. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        usuarios = users.listar_usuarios()
        for user in usuarios:
            print(f"- {user['name']} ({user['email']})")
    elif opcao == "2":
        user_id = input("Digite o ID do usuário: ")
        detalhes = users.usu_detalhes(user_id)
        if detalhes:
            print(f"Nome: {detalhes['name']}")
            print(f"Email: {detalhes['email']}")
            print(f"Telefone: {detalhes['phone']}")
    elif opcao == "3":
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        telefone = input("Digite o telefone do usuário: ")
        novo_usuario = {"name": nome, "email": email, "phone": telefone}
        usuario_criado = users.usu_criar(novo_usuario)
        if usuario_criado:
            print(f"Usuário criado com sucesso! ID: {usuario_criado['id']}")
    elif opcao == "4":
        user_id = input("Digite o ID do usuário a ser atualizado: ")
        nome = input("Digite o novo nome do usuário: ")
        email = input("Digite o novo email do usuário: ")
        telefone = input("Digite o novo telefone do usuário: ")
        dados_atualizados = {"name": nome, "email": email, "phone": telefone}
        usuario_atualizado = users.usu_atualizar(user_id, dados_atualizados)
        if usuario_atualizado:
            print("Usuário atualizado com sucesso!")
    elif opcao == "5":
        user_id = input("Digite o ID do usuário a ser deletado: ")
        if users.usu_deletar(user_id):
            print("Usuário deletado com sucesso!")
    elif opcao == "6":
        user_id = input("Digite o ID do usuário: ")
        tarefas = users.listar_usuarios(user_id)
        if tarefas:
            for tarefa in tarefas:
                print(f"- {tarefa['title']}")
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")