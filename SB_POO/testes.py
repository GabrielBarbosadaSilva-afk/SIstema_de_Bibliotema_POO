from usuario import Aluno, Professor
from livro import Livro
from biblioteca import Biblioteca
from emprestimo import Emprestimo

if __name__ == '__main__':
    aluno = Aluno('nome')
    livro = Livro('livro', 'autor', 2005)
    biblioteca = Biblioteca()
    biblioteca.cadastrar_livro(livro)
    biblioteca.cadastrar_usuario(aluno)
    biblioteca.emprestar_livro(1, 1)
    print(aluno.emprestimos_ativos)
    biblioteca.devolver_livro(1, 1)
    print(aluno.emprestimos_ativos)
    biblioteca.devolver_livro(1, 1)
