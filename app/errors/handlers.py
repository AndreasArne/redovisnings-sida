"""
Contains error handlers
"""
from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(unused_error):
    """
    Error handler for code 404
    """
    # print(dir(error))
    return render_template('errors/404.html')


@bp.app_errorhandler(500)
def internal_error(unused_error):
    """
    Error handler for code 500
    """
    db.session.rollback()
    return render_template('errors/500.html')
