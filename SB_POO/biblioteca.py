from usuario import Usuario, Aluno, Professor
from livro import Livro
class Biblioteca:
    def __init__(self):
        self._livros = [] 
        self._usuarios = []

    def cadastrar_livro(self, livro: Livro) -> None:
        self._livros.append(livro)

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def listar_livros(self) -> None:
        print('*'*30,f'\n*{"Lista de Livros:":^28}*\n','*'*29)
        for l in self._livros:
            print(l)

    def listar_usuarios(self) -> None:
        print('*'*30,f'\n*{"Lista de Usuários:":^28}*\n','*'*29)
        for u in self._usuarios:
            print(u)

    def buscar_livro_por_id(self, id_livro: int) -> Livro:
        for l in self._livros:
            if id_livro == l.id_livro:
                print('*'*30,f'\n*{"O livro encontrado foi:":^28}*\n','*'*29, l)
                return l

    def buscar_usuario_por_id(self, id_usuario: int) -> Usuario:
        for u in self._usuarios:
            if id_usuario == u.id_usuario:
                print('*'*30,f'\n*{"O usuário encontrado foi:":^28}*\n','*'*29, u)
                return u
            
    def emprestar_livro(self, id_livro: int, id_usuario: int) -> None:
        livro = self.buscar_livro_por_id(id_livro)
        usuario = self.buscar_usuario_por_id(id_usuario)
        if livro.disponivel:
            
            livro.marcar_emprestado

    def devolver_livro(self, id_livro: int, id_usuario: int) -> None:
        livro = self.buscar_livro_por_id(id_livro)
        if not(livro.disponivel):
            
            livro.marcar_devolvido

