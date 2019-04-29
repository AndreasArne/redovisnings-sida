"""
Test handlers for request errors, app/errors/handlers
"""
import pytest
from werkzeug.exceptions import HTTPException

def test_404(client):
    response = client.get('/non_existing_route')
    assert response.status_code == 404
    assert b"File Not Found" in response.data
    assert b"V\xc3\xa4lkommen till min me-sida" in response.data

# def test_500(client):
#     response = client.get('/wrong')
#     assert response.status_code == 500
#     assert b"An unexpected error has occurred" in response.data
#     assert b"V\xc3\xa4lkommen till min me-sida" in response.data
