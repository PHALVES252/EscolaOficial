import sqlite3

conn = sqlite3.connect('../ProjetoEscola_Paulo/escola.db')
cursor = conn.cursor()

from select_professores_Paulo import buscar_nome_professor, buscar_id_professor, buscar_email_professor, menu_principal


def editar(cursor, conn):
    global escolhido, dados
    menu_principal(cursor)
    escolha = input('Escolha uma opção')
    while True:

        if escolha == '1':
            try:

                id_professor = int(input("Digite o ID do professor: "))
                dados = buscar_id_professor(cursor, id_professor)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")


        elif escolha == '2':
            nome = input("Digite o nome do professor: ")
            dados = buscar_nome_professor(cursor, nome)


        elif escolha == '3':
            email = input("Digite o email")
            dados = buscar_email_professor(cursor, email)
        else:
            print("Opção inválida.")
            return

        if not dados:
            print("Nenhum professor encontrado.")
            return

        if isinstance(dados, list):

            for i, registro in enumerate(dados, start=1):
                print(
                    f" lISTA DE DICIONARIOS:{i}) ID: {registro['id_professor']} Cpf: {registro['cpf']} Nome: {registro['nome']}")

            try:
                op = int(input("Escolha uma opção: "))
                if op < 1 or op > len(dados):
                    print("Opção inválida.")
                    return
            except ValueError:
                print("Entrada inválida.")
                return

            escolhido = dados[op - 1]
        elif isinstance(dados, dict):
            escolhido = dados
            print(f" DICIONARIO ID: {escolhido['id_professor']} Cpf: {escolhido['cpf']} Nome: {escolhido['nome']}")

        while True:
            nome = input("Digite o novo nome: ")
            cpf = input('Digite o cpf correto')

            cursor.execute('UPDATE professores SET nome = ?,cpf = ?'
                           ' WHERE id_professor = ?', (nome, cpf, escolhido['id_professor']))
            conn.commit()
            resp = input("Deseja concluir a alteração [S|N]: ")

            if resp in 'Ss':
                print("Concuido")
                if cursor.rowcount > 0:
                    print("Edição realizada com sucesso!")
                else:
                    print("A alteração não foi concluída.")
                return
            else:
                print("Alteração cancelada.")
                return




