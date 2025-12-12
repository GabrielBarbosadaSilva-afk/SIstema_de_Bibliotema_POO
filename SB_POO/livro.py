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
        self._disponivel = False
        return self._disponivel
       
    def marcar_devolvido(self) -> None:
       self._disponivel = True
       return self._disponivel