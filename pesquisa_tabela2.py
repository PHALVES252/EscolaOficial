import sqlite3
from select_professores_Paulo import menu_professores

def pesquisar2(tabela,cursor,conn):
   if tabela == '2':
       menu_professores(cursor)


