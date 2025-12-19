from biblioteca import Biblioteca
from usuario import Aluno, Professor
from livro import Livro
from emprestimo import Emprestimo
from time import sleep

biblioteca = Biblioteca()

while True:
    print('+' + '-'  * 10 + '+')
    print('|' + f'{"MENU": ^10}' + '|')
    print('+' + '-'  * 10 + '+')
    print('1 - Cadastrar usuário')
    print('2 - Cadastrar livro')
    print('3 - Visualizar livros')
    print('4 - Visualizar usuários')
    print('5 - Visualizar empréstimos')
    print('6 - Buscar livros')
    print('7 - Emprestar livro')
    print('8 - Devolver livro')
    print('0 - Sair')

    op = input().strip()
    try:
        op = int(op)
        continuar = True
    except:
        continuar = False

print('Programa finalizado!')