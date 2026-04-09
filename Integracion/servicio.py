from repositorio import LibroRepository
from models import Libro

class BibliotecaService:
    def __init__(self, repo: LibroRepository):
        self.repo = repo

    def agregar_libro(self, titulo: str, autor: str) -> Libro:
        if not titulo or not autor:
            raise ValueError('TÃ­tulo y autor son obligatorios')
        return self.repo.guardar(Libro(titulo=titulo, autor=autor))

    def prestar_libro(self, titulo: str) -> Libro:
        libro = self.repo.buscar_por_titulo(titulo)
        if libro is None:
            raise LookupError(f'Libro {titulo!r} no encontrado')
        if not libro.disponible:
            raise RuntimeError(f'Libro {titulo!r} no disponible')
        libro.disponible = False
        self.repo.session.commit()
        return libro
