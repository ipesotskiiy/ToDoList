import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from config import DB_USER_TEST, DB_PASSWORD_TEST, DB_HOST_TEST, DB_PORT_TEST, DB_NAME_TEST
from database import Base
from main import app, get_session

DATABASE_URL_TEST = f'postgresql://{DB_USER_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}'

engine_test = create_engine(DATABASE_URL_TEST)
SessionLocalTest = sessionmaker(engine_test, expire_on_commit=False)


def for_test_get_session():
    session_test = SessionLocalTest()
    try:
        yield session_test
    finally:
        session_test.close()


app.dependency_overrides[get_session] = for_test_get_session


@pytest.fixture(scope='session', autouse=True)
def setup_db():
    Base.metadata.drop_all(engine_test)
    Base.metadata.create_all(engine_test)


client = TestClient(app)
