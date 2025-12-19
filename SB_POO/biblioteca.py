from usuario import Usuario, Aluno, Professor
from livro import Livro
from emprestimo import Emprestimo

class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = []

    def cadastrar_livro(self, livro):
        self._livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def listar_livros(self):
        print("Lista de Livros:")
        for l in self._livros:
            print(l)

    def listar_usuarios(self):
        print("Lista de Usuários:")
        for u in self._usuarios:
            print(u)

    def buscar_livro_por_id(self, id_livro):
        for l in self._livros:
            if id_livro == l.id_livro:
                return l

    def buscar_usuario_por_id(self, id_usuario):
        for u in self._usuarios:
            if id_usuario == u.id_usuario:
                return u

    def emprestar_livro(self, id_livro, id_usuario):
        livro = self.buscar_livro_por_id(id_livro)
        usuario = self.buscar_usuario_por_id(id_usuario)

        # se o livro ou o usuário forem inexistentes, retorne
        if livro is None:
            return
        if usuario is None:
            return
        
        # verifica se o empréstimo é possível
        if not livro.disponivel:
            return
        if not usuario.pode_emprestar():
            return
        
        # se a função não retornou, o empréstimo é válido
        livro.marcar_emprestado()
        Emprestimo(livro, usuario)

    def devolver_livro(self, id_livro, id_usuario):
        livro = self.buscar_livro_por_id(id_livro)
        usuario = self.buscar_usuario_por_id(id_usuario)

        # se o livro ou o usuário forem inexistentes, retorne
        if livro is None:
            return
        if usuario is None:
            return
        
        # procura o empréstimo em questão na lista de empréstimos ativos do usuário
        emprestimoExiste = False
        for emprestimo in usuario.emprestimos_ativos:
            if emprestimo.livro.id_livro == id_livro:
                emprestimoExiste = True
                break
        if emprestimoExiste:
            livro.marcar_devolvido()
            emprestimo.registrar_devolucao()

