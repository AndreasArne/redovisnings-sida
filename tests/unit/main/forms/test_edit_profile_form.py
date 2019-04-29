"""
Contains tests for app.main.forms.EditProfileForm class
"""
import pytest
from unittest import mock
from wtforms.validators import ValidationError
from app.main.forms import EditProfileForm



@mock.patch("app.main.forms.User")
def test_validate_username(mock_user, test_app):
    first = mock.Mock()
    mock_user.query.filter_by.return_value = first
    first.first.return_value = None
    username = mock.Mock()
    username.data = "john"
    assert EditProfileForm(username.data).validate_username(username) == None
    assert EditProfileForm("susan").validate_username(username) == None



@mock.patch("app.main.forms.User")
def test_validate_username_raise_exception(mock_user, test_app):
    first = mock.Mock()
    mock_user.query.filter_by.return_value = first
    first.first.return_value = "john"
    username = mock.Mock()
    username.data = "john"
    with pytest.raises(ValidationError):
        EditProfileForm("susan").validate_username(username)
