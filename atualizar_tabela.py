import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

from select_professores_Paulo import buscar_nome_professor, buscar_id_professor, buscar_email_professor, menu_principal
from select_professores_Paulo import pergunta_string, pergunta_inteiro


def Atualizar(cursor, conn):

    global dados
    menu_principal(cursor)

    while True:
        escolha = input('Escolha uma opção')

        if escolha == "" or escolha == '0':
            return

        elif escolha == '2':
            nome = pergunta_string("Digite o nome do professor: ")
            dados = buscar_nome_professor(cursor, nome)

        elif escolha == '3':
            email = pergunta_string("Digite seu email")
            dados = buscar_email_professor(email,cursor)
        else:
            print("Opção inválida.")
            return

        if not dados:
            return

        if isinstance(dados, list):

            for i, registro in enumerate(dados):
                print(
                    f" {i + 1}) | {registro['id_professor']} |  | Nome {registro['nome']} CPF :{registro['cpf']} {registro['e-mail']} ")

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
            print(f'====='*len(dados))
            print(f" |ID = {escolhido['id_professor']}|  | Nome: {escolhido['nome']}|Cpf ={escolhido['cpf']} E-mail= {escolhido ['e-mail']} ")
        while True:


            nome = input("Digite o novo nome: ")
            cpf = input('Digite o cpf correto: ')
            email = input('Dgite o novo email: ')
            telefone = input('Digite o telefone: ')
            formacao = input('Digite a formação: ')
            if nome.isdigit() or len(nome) < 2:
                print("Aviso o nome deve ter mais de 2 letras e não pode ser numerico")
                continue


            cursor.execute('UPDATE professores SET nome = ?,cpf = ?,email = ?, telefone = ?, formaçao = ?'
                           ' WHERE id_professor = ?', (nome, cpf, email, telefone, formacao, escolhido['id_professor']))

            resp = input("Deseja concluir a alteração [S|N]: ")

            if resp in 'Ss':
                conn.commit()

                if cursor.rowcount > 0:
                    print("Edição realizada com sucesso!")

                else:
                    print("A alteração não foi concluída.")
                return

            else:
                print("Alteração cancelada.")
                return
