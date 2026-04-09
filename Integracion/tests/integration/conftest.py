import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from repositorio import LibroRepository
from servicio import BibliotecaService

@pytest.fixture(scope='session')
def engine():
    _engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(_engine)
    yield _engine
    Base.metadata.drop_all(_engine)

@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    s = Session()
    yield s
    s.rollback()
    s.close()

@pytest.fixture
def servicio(session):
    return BibliotecaService(LibroRepository(session))
