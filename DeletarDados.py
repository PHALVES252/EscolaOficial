import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()


def deletar2():



    while True:
        print("1) Nome")
        print("2) E-mail")
        print("3) Telefone")
        print("4) Cpf")

        dicionario= {1:'nome',2:'email'}
        escolha=int(input("Escolha uma opção de busca"))

        valor_busca = input(f"Digite o {dicionario[escolha]} do registro do professor que deseja cancelar")
        query = f'''SELECT * FROM professores WHERE {dicionario[escolha]}=?'''
        cursor.execute(query,(valor_busca,))
        resposta = cursor.fetchone()

        if resposta:
            print(
                f"Professor localizado: ID = {resposta[0]}, Nome atual = {resposta[1]}, Email Atual {resposta[3]}"
                f",Telefone atual{resposta[4]} ")

        else:
            print("Não foi possivel localizar o id informado\n"
                  "Verifique as informações e tente novamente ")
            continue

        op = input("Deseja mesmo apagar esse registro essa ção não pode ser desfeita")

        if op in 'sS':

            cursor.execute(f'''DELETE FROM professores WHERE {dicionario[escolha]}=?''', (valor_busca,))
            conn.commit()

            if cursor.rowcount>0:
                print(" Registro Apagado com sucesso")

            else:
                print("Registro não apagador")

        elif op in 'Nn':
            print(" Operação cancelada")
            break


deletar2()