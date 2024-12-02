import sqlite3

conn = sqlite3.connect("../ProjetoEscola_Paulo/escola.db")
cursor = conn.cursor()


def deletar2():
    while True:
        iden = int(input("Digite o id do registro do professor que deseja cancelar"))
        cursor.execute('''SELECT * FROM professores WHERE id_professor=?''', (iden,))
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

            cursor.execute('''DELETE FROM professores WHERE id_professor=?''', (iden,))
            conn.commit()
            print(" Registro Apagado com sucesso")

        elif op in 'Nn':
            print(" Operação cancelada")
            break
