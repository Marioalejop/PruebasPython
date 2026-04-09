from sqlalchemy.orm import Session
from models import Libro

class LibroRepository:
    def __init__(self, session: Session):
        self.session = session

    def guardar(self, libro: Libro) -> Libro:
        self.session.add(libro)
        self.session.commit()
        self.session.refresh(libro)
        return libro

    def buscar_por_titulo(self, titulo: str) -> Libro | None:
        return self.session.query(Libro)\
            .filter(Libro.titulo == titulo).first()
