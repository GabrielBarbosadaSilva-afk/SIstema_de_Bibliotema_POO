import abc

class Usuario(abc.ABC):
    id_us = 10
    @abc.abstractmethod
    def __init__(self, nome):
        self._nome = nome
        self._id_usuario = Usuario.id_us
        Usuario.id_us += 10
        
    
    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def nome(self) -> str:
        return self._nome 
    
    def pode_emprestar() -> bool:
        return True or False

    def __str__(self):
        return f'\nTipo de usuario: {self.tipo}; \nID: {self.id_usuario}; \nNome: {self.nome}; \nEmprestimos disponíiveis: {self.l}.\n{"_"*20}\n'

class Aluno(Usuario):
    tipo = 'Aluno'
    def __init__(self, nome):
        super().__init__(nome)
        self._limite_emprestimo = 2
    
    def pode_emprestar(self) -> bool:
        if self._limite_emprestimo < 0:
            return False
        else:
            return True

class Professor(Usuario):
    tipo = 'Professor'
    def __init__(self, nome):
        super().__init__(nome)
        self._limite_emprestimo = 3

    def pode_emprestar(self) -> bool:
        if self._limite_emprestimo < 0:
            return False
        else:
            return True

