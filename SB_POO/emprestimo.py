import datetime


class Data:
    def __init__(self):
        self._data = datetime.datetime.today()

    @property
    def data(self):
        return self._data

    def data_formatada(self):
        return self._data.strftime("%d/%m/%y")


class Emprestimo:
    def __init__(self, livro, usuario):
        self._livro = livro
        self._usuario = usuario
        self._data_emprestimo = Data()
        self._data_devolucao = None  # OBS: a variável armazena quando o livro foi devolvido, não quando deve ser
        self._usuario.adicionar_emprestimo_ativo(self)


    @property
    def livro(self):
        return self._livro

    @property
    def usuario(self):
        return self._usuario

    @property
    def data_emprestimo(self):
        return self._data_emprestimo

    @property
    def data_devolucao(self):
        return self._data_devolucao

    def registrar_devolucao(self):
        if self._data_devolucao is not None:
            return # detecta se o empréstimo já foi devolvido
        self._data_devolucao = Data()
        self._usuario.remover_emprestimo_ativo(self)

