"""
Contains tests for app.models.Post class
"""
import pytest
from datetime import datetime
from app.models import Post

@pytest.fixture
def post1():
    return Post(
        title='First post',
        body='Hello this is my firtst post',
    )



def test_new_post(post1):
    assert post1.title == 'First post'
    assert post1.body == "Hello this is my firtst post"
    assert str(post1) == "<Post Hello this is my firtst post>"
