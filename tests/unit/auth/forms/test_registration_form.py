"""
Contains tests fortest_app.auth.forms.RegistrationForm class
"""
import pytest
from unittest import mock
from wtforms.validators import ValidationError
from app.auth.forms import RegistrationForm



@mock.patch("app.auth.forms.User")
def test_validate_username(mock_user, test_app):
    first = mock.Mock()
    mock_user.query.filter_by.return_value = first
    first.first.return_value = None
    username = mock.Mock()
    username.data = "john"
    assert RegistrationForm().validate_username(username) == None



@mock.patch("app.auth.forms.User")
def test_validate_username_raise_exception(mock_user, test_app):
    first = mock.Mock()
    mock_user.query.filter_by.return_value = first
    first.first.return_value = "john"
    username = mock.Mock()
    username.data = "john"
    with pytest.raises(ValidationError):
        RegistrationForm().validate_username(username)



@mock.patch("app.auth.forms.User")
def test_validate_email(mock_user, test_app):
    first = mock.Mock()
    mock_user.query.filter_by.return_value = first
    first.first.return_value = None
    email = mock.Mock()
    email.data = "john@gmail.com"
    assert RegistrationForm().validate_email(email) == None



@mock.patch("app.auth.forms.User")
def test_validate_email_raise_exception(mock_user, test_app):
    first = mock.Mock()
    mock_user.query.filter_by.return_value = first
    first.first.return_value = "john@gmail.com"
    email = mock.Mock()
    email.data = "john@gmail.com"
    with pytest.raises(ValidationError):
        RegistrationForm().validate_email(email)
