import abc

class Usuario(abc.ABC):
    id_us = 10
    @abc.abstractmethod
    def __init__(self, nome):
        self._nome = nome
        self._id_usuario = Usuario.id_us
        Usuario.id_us += 10
        self._livros_pegos = []
        self._limite_emprestimo = int
        
    
    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def nome(self) -> str:
        return self._nome 

    @property
    def livros_pegos(self):
        return self._livros_pegos

    @property
    def limite_emprestimo(self):
        return self._limite_emprestimo

    @limite_emprestimo.setter
    def limite_emprestimo(self, limite : int):
        self._limite_emprestimo = limite
        return self._limite_emprestimo
    
    @abc.abstractmethod
    def pode_emprestar(self) -> bool:
        if self.limite_emprestimo <= 0:
            return False
        else:
            return True

    def __str__(self):
        return f'\nTipo de usuario: {self.tipo}; \nID: {self.id_usuario}; \nNome: {self.nome}; \nEmprestimos disponíiveis: {self.limite_emprestimo}.\n{"_"*20}\n'

class Aluno(Usuario):
    tipo = 'Aluno'
    def __init__(self, nome):
        super().__init__(nome)
        self._limite_emprestimo = 2
    
    def pode_emprestar(self) -> bool:
        super().pode_emprestar()
        

class Professor(Usuario):
    tipo = 'Professor'
    def __init__(self, nome):
        super().__init__(nome)
        self._limite_emprestimo = 3

    def pode_emprestar(self) -> bool:
        super().pode_emprestar()

