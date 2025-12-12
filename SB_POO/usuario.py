import abc

class Usuario(abc.ABC):
    @abc.abstractmethod
    def __init__(self, id_usuario, nome):
        self._id_usuario = id_usuario
        self._nome = nome
    
    @property
    def id_usuario(self):
        self._id_usuario = int

    @property
    def nome(self):
        self._nome = str
    
    @nome.setter
    def nome(self):
        return self._nome
    
    def pode_emprestar():
        return True or False

class Aluno(Usuario):
    def __init__(self, id_usuario, nome, limite_emprestmo):
        super().__init__(id_usuario, nome)
        self._limite_emprestimo = 2
    

class Professor(Usuario):
    def __init__(self, id_usuario, nome, limite_emprestimo):
        super().__init__(id_usuario, nome)
        self._limite_emprestimo = 3
