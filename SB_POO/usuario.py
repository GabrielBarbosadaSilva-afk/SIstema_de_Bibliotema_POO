import abc
import datetime

class Usuario(abc.ABC):
    id_usuario_contador = 1

    @abc.abstractmethod
    def __init__(self, nome):
        self._nome = nome
        self._id_usuario = Usuario.id_usuario_contador
        Usuario.id_usuario_contador += 1

        # listas de objetos do tipo Emprestimo
        self._emprestimos_ativos = []
        self._historico_emprestimos = []

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nome(self):
        return self._nome

    @property
    def emprestimos_ativos(self):
        return self._emprestimos_ativos
    
    @property
    def hitorico_emprestimos(self):
        return self._hitorico_emprestimos

    def pode_emprestar(self):
        if len(self._emprestimos_ativos) < self._limite_emprestimo:
            return True
        return False

    def adicionar_emprestimo_ativo(self, emprestimo):
        self._emprestimos_ativos.append(emprestimo)
    
    def remover_emprestimo_ativo(self, emprestimo):
        self._historico_emprestimos.append(emprestimo)
        self._emprestimos_ativos.remove(emprestimo)

class Aluno(Usuario):
    def __init__(self, nome):
        super().__init__(nome)
        self._limite_emprestimo = 2

    def pode_emprestar(self):
        if not super().pode_emprestar():
            return False

        for emprestimo in self._emprestimos_ativos:
            diaEmprestimo = datetime.datetime.strptime(emprestimo._data_emprestimo.data_formatada(),"%d/%m/%y").date()
            if datetime.datetime.today().date() == diaEmprestimo:
                return False
        return True

class Professor(Usuario):
    def __init__(self, nome):
        super().__init__(nome)
        self._limite_emprestimo = 3
