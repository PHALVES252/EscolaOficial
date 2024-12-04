import sqlite3
from time import sleep

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()


def menu_principal(cursor):
    print("====" * 42)
    print("1) Buscar por nome do professor")
    print("2) Buscar por email do professor")
    print("3) Buscar por cpf do professor")
    print("4) Buscar por telefone do professor")
    print("====" * 42)
    print("0) Para voltar")

def menu_professores(cursor):
    global email
    while True:
        menu_principal(cursor)

        opcao = input("Escolha uma opção (1/5) ou 0 para voltar")

        if opcao == '0':
            return


        elif opcao == '1':
            while True:
                nome = pergunta_string("Digite o nome do professor")
                if not nome:
                    break

                resposta = buscar_nome_professor(nome, cursor)
                print(f"\nAo pesquisar pelo nome {nome} na tabela professores:")
                exibe_resposta_lista(resposta)

        elif opcao == '2':
            while True:
                email = pergunta_string("Insira o email do professor: ")
                if not email:
                    break

                resposta = buscar_email_professor(email, cursor)
                print(f"\nAo pesquisar pelo emaIL {email} na tabela professores:")
                exibe_resposta_lista(resposta)

        elif opcao == '3':
            while True:
                cpf = pergunta_string("Insira o cpf do professor")
                if not cpf:
                    break

                resposta = buscar_cpf_professor(cpf,cursor)
                print(f"\n Ao pesquisar pelo CPF: {cpf} localizamos")
                exibe_resposta_lista(resposta)

        elif opcao == '4':
            while True:
                telefone = pergunta_string("Insira o Telefone do professor")
                if not telefone:
                    break

                resposta = buscar_telefone_professor(telefone, professor)
                print(f'\n Ao pesquisar pelo telefone {telefone} encontramos')
                exibe_resposta_dicionario(resposta)


def exibe_resposta_lista(lista):
    if lista is None:
        print("  Ops! :-|  Nenhum registro foi encontrado.")
    else:
        for linha in lista:
            exibe_resposta_dicionario(linha)


def pergunta_string(mensagem):
    while True:
        print()
        print("_" * 45)
        print("_" * 45)
        resposta = input(mensagem).strip()
        if resposta == "":
            break
        return resposta


def pergunta_inteiro(mensagem):
    while True:
        resposta = input(mensagem).strip()
        try:
            resp = int(resposta)

            return resp

        except Exception as e:
            print("Insira os dados validos")


def buscar_id_professor(cursor,id_professor):
    # Verifica se o cursor é válido antes de executar a consulta
    if not hasattr(cursor, 'execute'):
        print("Erro: O cursor não é válido.")
        return None

    try:
        # Realiza a consulta SQL para buscar pelo nome (usando LIKE para busca parcial)
        cursor.execute('''SELECT * FROM professores WHERE id_professor= ?''', ( id_professor,))

        # Recupera todos os resultados da consulta
        resposta = cursor.fetchone()

        if resposta:  # Verifica se existem resultados

                return {
                    'id_professor': resposta[0],
                    'nome': resposta[1],
                    'cpf': resposta[2],
                    'e-mail': resposta[3],
                    'Telefone': resposta[4]
                }





        else:
            print("Nenhum professor encontrado.")
            return None

    except Exception as e:
        print(f"Erro ao buscar pelo nome: {e}")
        return None


def exibe_resposta_dicionario(dicionario):
    if not dicionario:
        print("  Vixe! :-(  Nenhum registro foi encontrado.")
    else:
        for chave, valor in dicionario.items():
            print(f"  O campo: '{chave}' contém o valor: '{valor}'.")


def buscar_nome_professor(nome, cursor):
    # Verifica se o cursor é válido antes de executar a consulta
    if not hasattr(cursor, 'execute'):
        print("Erro: O cursor não é válido.")
        return None

    try:

        cursor.execute('''SELECT * FROM professores WHERE nome LIKE ?''', ('%' + nome + '%',))

        # Recupera todos os resultados da consulta
        resposta = cursor.fetchall()

        if resposta:  # Verifica se existem resultados
            registros = []

            # Percorre os resultados e os organiza em um formato de dicionário
            for linha in resposta:
                registros.append({
                    'id_professor': linha[0],
                    'nome': linha[1],
                    'cpf': linha[2],
                    'E-mail': linha[3],
                    'Telefone': linha[4]
                })

            return registros  # Retorna os registros encontrados

        else:
            print("Nenhum professor encontrado.")
            return None

    except Exception as e:
        print(f"Erro ao buscar pelo nome: {e}")
        return None


def buscar_email_professor(cursor,email):
    cursor.execute('''SELECT * FROM PROFESSORES WHERE email=?''', (email,))
    resposta = cursor.fetchone()

    if resposta:
        return {
            'id_professor': resposta[0],
            'nome': resposta[1],
            'cpf': resposta[2],
            'telefone': resposta[4]
        }


def buscar_cpf_professor(cpf, cursor):
    cursor.execute('''SELECT * FROM PROFESSORES WHERE email=?''', (cpf,))
    resposta = cursor.fetchone()

    if resposta:
        return {
            'id_professor': resposta[0],
            'nome': resposta[1],
            'cpf': resposta[2],
            'telefone': resposta[4]
        }


def buscar_telefone_professor(telefone, cursor):
    cursor.execute('''SELECT * FROM PROFESSORES WHERE email=?''', (telefone,))
    resposta = cursor.fetchone()

    if resposta:
        return {
            'id_professor': resposta[0],
            'nome': resposta[1],
            'cpf': resposta[2]
        }
