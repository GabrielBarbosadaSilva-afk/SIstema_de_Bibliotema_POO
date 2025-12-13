class Livro:
    id_livr = 0.001
    def __init__(self, titulo: str, autor: str, ano: int):
        self._id_livro = Livro.id_livr
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True
        Livro.id_livr += 0.001
   
    @property
    def id_livro(self) -> float:
        return self._id_livro

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def autor(self) -> str:
        return self._autor
    
    @property
    def ano(self) -> int:
        return self._ano

    @property
    def disponivel(self) -> bool:
        return self._disponivel
   
    def marcar_emprestado(self) -> None:
        pass

    def marcar_devolvido(self) -> None:
        pass

    def __str__(self):
        return f'\nID: {self.id_livro}; \nTítulo: {self.titulo}; \nAutor: {self.autor}; \nAno de lançamento: {self.ano}.\n{"_"*20}\n'