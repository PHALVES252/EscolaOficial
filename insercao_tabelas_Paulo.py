
def inserir2(tabela, cursor, conn):
    if tabela == "2":
        professores = [

            ("PH100", "0000001267860904", "Amoa00J8888JJSa77kk44ra@gmail", "0560000000008912548",
             "Como  kalinagot"),
            ("Jhon B", "000001253", "Poguelandia@gmail.com", "056000089008912548",
             "Como falar kalinago"),
            ("J J", "0000001789", "Maybanck@gmail.com", "05600000078912548",
             "Matematica"),
        ]
        inserir_na_tabela_professores(professores, cursor, conn)


def inserir_na_tabela_professores(professores, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO professores (nome, cpf, email, telefone, formaçao)
            VALUES (?, ?, ?, ?, ?);
        ''', professores)
        conn.commit()
        print("Professores inseridos com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir professores.\nErro: {e}")
        return False
    return True
