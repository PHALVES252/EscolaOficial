import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

print("Conexão estabelecida com sucesso")


def apagar(tabela):
    cursor.execute('''DROP TABLE {tabela}''')
    conn.commit()


