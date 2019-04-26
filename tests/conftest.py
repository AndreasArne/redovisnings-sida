"""
COntains fixtures for tests
"""
import pytest
from app import create_app, db
from app.config import TestConfig

@pytest.fixture(scope='function')
def app():
    """
    Create Flask app fixture
    """
    app_ = create_app(TestConfig)
    app_context = app_.app_context()
    app_context.push()
    db.create_all()

    yield app_

    db.session.remove()
    db.drop_all()
    app_context.pop()


@pytest.fixture(scope="function")
def client(app_):
    """
    Create client for app
    """
    return app_.test_client()
