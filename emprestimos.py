class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo, data_devolucao):
        self._livro = livro
        self._usuario = usuario
        self._data_emprestimo = data_emprestimo # isso deve ser feito com a datetime?
        self._data_devolucao = data_devolucao # calcular automaticamente baseado em data_emprestimo?

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
    
    def registrar_devolucao(self, data):
        pass
