import sqlite3
from time import sleep
from criacao_tabelas_Paulo import criar2
from insercao_tabelas_Paulo import inserir2
from pesquisa_tabela2 import pesquisar2
from atualizar_tabela import atualizar
from DeletarDados import  deletar
from Apagar_tabela import  apagar

# Menu de seleção de tabela
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()


print("Conexão estabelecida com sucesso")

def selecionar_tabela():
    while True:
        print("===" * 45)
        print("Menu de Seleção de Tabela")
        print("===" * 45)
        print("1)Selecionar Tabela Alunos")
        print("2)Selecionar Tabela Professores")
        print("3)Selecionar Tabela Cursos ")
        print("4)Selecionar Tabela Disciplinas")
        print("5)Selecionar Tabela Avaliações")
        print("6) Selecionar Tabela Matriculas")
        print("7)Selecionar Tabelas Frequencias")

        print("0) Para Sair")

        op = input("Escolha uma opção de 1 a 7 ou 0 para sair")

        if op == "0":
            break

        elif op in "1234567":
            return op
        print(" Alternativa invalida tente Novamente")
        sleep(1)




# Menu principal:
while True:

    print("===" * 45)
    print("Menu principal")
    print("===" * 45)
    print("1) Criar tabela")
    print("2) Inserir")
    print("3)Pesquisar|Ler")
    print("4)Editar")
    print("5)Excluir dados")
    print("6) Excluir Tabela")
    print("===" * 45)
    print("0) Sair do programa")
    print("===" * 45)

    opcao = input("Escolha uma atividade(1/6) ou 0 para sair")

    if opcao == "0":
        break

    elif opcao not in "123456":
        print("Opção invalida, tente novamente")
        continue

    while True:

        tabela = selecionar_tabela()

        if tabela == '0':
            break

        if opcao == '1':
            criar2(tabela, cursor, conn)
        elif opcao == '2':
            inserir2(tabela, cursor, conn)

        elif opcao == '3':
            pesquisar2(tabela, cursor, conn)

        elif opcao == '4':
            atualizar()

        elif opcao == '5':
            apagar(tabela)




        sleep(2)
