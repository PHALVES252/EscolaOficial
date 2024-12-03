import sqlite3
from time import sleep

conn = sqlite3.connect('../ProjetoEscola_Paulo/escola.db')
cursor = conn.cursor()


def menu_principal(cursor):
    print("====" * 42)
    print("1) Buscar por id professor")
    print("2) Buscar por nome do professor")
    print("3) Buscar por cpf do professor")
    print("4) Buscar por email do professor")
    print("5) Buscar por telefone do professor")
    print("====" * 42)
    print("0) Para voltar")

def menu_professores(cursor):
    while True:
        menu_principal(cursor)

        opcao = input("Escolha uma opção (1/5) ou 0 para voltar")

        if opcao == '0':
            return

        elif opcao == '1':
            print()
            print("===" * 45)
            print("Pesquisar pelo id do professor")
            print("=====" * 45)
            while True:
                id_professor = pergunta_inteiro("Insira o id do professor")
                if id_professor is None:
                    break

                else:

                    resposta = buscar_id_professor(cursor,id_professor)
                    print(f'Ao pesquisar  pelo id {id_professor} na tabela professor encontramos')
                    exibe_resposta_dicionario(resposta)

        elif opcao == '2':
            while True:
                nome = pergunta_string("Digite o nome do professor")
                if not nome:
                    break

                resposta = buscar_nome_professor(nome, cursor)
                print(f"\nAo pesquisar pelo nome {nome} na tabela professores:")
                exibe_resposta_lista(resposta)

        elif opcao == '3':
            while True:
                email = pergunta_string("Insira o email do professor: ")
                if not nome:
                    break

        resposta = (email, cursor)
        print(f"\nAo pesquisar pelo emaIL {email} na tabela professores:")
        exibe_resposta_lista(resposta)


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
                    'E-mail': resposta[3],
                    'Telefone': resposta[4]
                }





        else:
            print("Nenhum professor encontrado.")
            return None

    except Exception as e:
        print(f"Erro ao buscar pelo nome: {e}")
        return None





    # cursor.execute('''SELECT * FROM professores WHERE id_professor=?''', (id_professor,))
    # resposta = cursor.fetchone()
    #
    # if resposta:
    #
    #     return {
    #         "Nome": resposta[1],
    #         "cpf": resposta[2],
    #         "E-mail": resposta[3],
    #         "Telefone": resposta[4],
    #         "Formação": resposta[5]
    #
    #     }
    #
    # else:
    #     return None


def exibe_resposta_dicionario(dicionario):
    if not dicionario:
        print("  Vixe! :-(  Nenhum registro foi encontrado.")
    else:
        for chave, valor in dicionario.items():
            print(f"  O campo: '{chave}' contém o valor: '{valor}'.")


def buscar_nome_professor(cursor, nome):
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
