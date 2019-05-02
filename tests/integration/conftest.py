"""
Fixtures for integration tests
"""
# pylint: disable=redefined-outer-name
import pytest

@pytest.fixture
def user_dict():
    """
    Dictionary with user data
    """
    data = {
        "username": "doe",
        "password": "test",
        "password2": "test",
        "email": "doe@example.com",
    }
    return data


@pytest.fixture
def register_user_response(client, user_dict):
    """
    Register user from user_dict
    """
    response = client.post(
        '/register',
        data=user_dict,
        follow_redirects=True,
    )
    return response
