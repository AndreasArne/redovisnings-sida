import pytest
from app.models import User

def test_password_hashing(app):
    u = User(username='susan')
    u.set_password('cat')
    assert u.check_password('dog') is False
    assert u.check_password('cat') is True

def test_avatar(app):
    u = User(username='john', email='john@example.com')
    assert u.avatar(128) ==  ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=retro&s=128')
