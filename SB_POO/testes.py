from usuario import Aluno, Professor
from livro import Livro
from biblioteca import Biblioteca

if __name__ == '__main__':
    a1 = Aluno('vini')
    a2 = Aluno('Eduardo')
    a3 = Aluno('Gabriel')
    a4 = Aluno('Alysson')
    p = Professor('Jean')
    l1 = Livro('Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)
    l2 = Livro('livro aleatório', 'alguem', 0000)
    l3 = Livro('sla', 'eu', 2025)
    b = Biblioteca()
    b.cadastrar_usuario(a1)
    b.cadastrar_usuario(a2)
    b.cadastrar_usuario(a3)
    b.cadastrar_usuario(a4)
    b.cadastrar_usuario(p)
    b.listar_usuarios()
    b.cadastrar_livro(l1)
    b.cadastrar_livro(l2)
    b.cadastrar_livro(l3)
    b.listar_livros()
    b.buscar_usuario_por_id(10)
    b.buscar_livro_por_id(0.002)

