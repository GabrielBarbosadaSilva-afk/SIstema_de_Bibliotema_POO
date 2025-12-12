from usuario import Usuario
from livro import Livro
class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = []

    def cadastrar_livro(self, livro):
        self._livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self._usuario.append(usuario)

    def listar_livros(self):
        for l in self._livros():
            print(l)

    def listar_usuarios(self):
        for u in self.usuarios():
            print(u)

    def buscar_livro_por_id(self, id_livro):
        pass

    def buscar_usuario_por_id(self, id_usuario):
        pass

    def emprestar_livro(self, id_livro, id_usuario):
        pass

    def devolver_livro(self, id_livro, id_usuario):
        pass