class Livro:
    def __init__(self, id_livro: int, titulo: str, autor: str, ano: int):
        self._id_livro = id_livro
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True

   
    @property
    def id_livro(self) -> int:
        return self._id_livro

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo: str):
        self._titulo = novo_titulo

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, novo_autor: str):
        self._autor = novo_autor

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, novo_ano: int):
        self._ano = novo_ano

    @property
    def disponivel(self) -> bool:
        return self._disponivel

   
    def marcar_emprestado(self) -> None:
        """Marca o livro como emprestado."""
        if self._disponivel:
            self._disponivel = False
        else:
            print("O livro já está emprestado.")

    def marcar_devolvido(self) -> None:
        """Marca o livro como devolvido."""
        self._disponivel = True