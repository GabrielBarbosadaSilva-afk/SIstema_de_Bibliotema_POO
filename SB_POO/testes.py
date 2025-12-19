from usuario import Aluno, Professor
from livro import Livro
from biblioteca import Biblioteca
from emprestimo import Emprestimo

if __name__ == '__main__':
    aluno = Aluno('nome')
    livro = Livro('livro', 'autor', 2005)
    emprestimo = Emprestimo(livro, aluno)
    print(aluno._emprestimos_ativos)
    print(aluno._historico_emprestimos)
    emprestimo.registrar_devolucao()
    print(aluno._emprestimos_ativos)
    print(aluno._historico_emprestimos)
    emprestimo.registrar_devolucao()