class Livro:
    id_livro_contador = 1

    def __init__(self, titulo, autor, ano):
        self._id_livro = Livro.id_livro_contador
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True
        Livro.id_livro_contador += 1

    @property
    def id_livro(self):
        return self._id_livro

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def ano(self):
        return self._ano

    @property
    def disponivel(self):
        return self._disponivel

    def marcar_emprestado(self):
        self._disponivel = False

    def marcar_devolvido(self):
        self._disponivel = True

    def __str__(self):
        return f"ID: {self.id_livro}\nTitulo: {self.titulo}\nAutor: {self.autor}\nAno de lançamento: {self.ano}\n{'-' * 20}\n"
