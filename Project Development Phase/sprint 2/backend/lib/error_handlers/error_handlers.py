from flask import current_app
from flask_jwt_extended.exceptions import JWTExtendedException
from sqlalchemy.exc import SQLAlchemyError

from application import jwt
from lib.error_handlers.constants import *
from lib.response.constants import *
from lib.response.constants import ERROR, MESSAGE_404, MESSAGE_500
from lib.response.response import response


@current_app.errorhandler(404)
def error_handler_404(error):
    return response(status_code=404, status=ERROR, data={}, message=MESSAGE_404)


@current_app.errorhandler(500)
def error_handler_500(error):
    return server_error_response(error)


@current_app.errorhandler(SQLAlchemyError)
def error_handler_SQL(error):
    return server_error_response(error)


@current_app.errorhandler(JWTExtendedException)
def error_handler_SQL(error):
    return server_error_response(error)


def server_error_response(error):
    return response(status_code=500, status=ERROR, data={}, message=MESSAGE_500)


@jwt.expired_token_loader
def expired_token_callback(_jwt_header, _jwt_data):
    return response(status_code=UNAUTHORIZED_ACCESS, status=ERROR, data={}, message=TOKEN_EXPIRED)


@jwt.invalid_token_loader
def invalid_token_callback(error_string):
    return response(status_code=UNPROCESSABLE_ENTITY, status=ERROR, data={}, message=error_string)


@jwt.unauthorized_loader
def unauthorized_callback(error_string):
    return response(status_code=UNAUTHORIZED_ACCESS, status=ERROR, data={}, message=error_string)


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(_jwt_header, _jwt_data):
    return response(status_code=UNAUTHORIZED_ACCESS, status=ERROR, data={}, message=FRESH_TOKEN_REQUIRED)


@jwt.revoked_token_loader
def revoked_token_callback(_jwt_header, _jwt_data):
    return response(status_code=UNAUTHORIZED_ACCESS, status=ERROR, data={}, message=TOKEN_REVOKED)


@jwt.user_lookup_error_loader
def user_lookup_error_callback(jwt_header, jwt_data):
    return response(status_code=UNAUTHORIZED_ACCESS, status=ERROR, data={}, message=ERROR_LOADING_USER)


@jwt.token_verification_failed_loader
def token_verification_failed_callback(jwt_header, jwt_data):
    return response(status_code=BAD_REQUEST, status=ERROR, data={}, message=CLAIM_VERIFICATION_FAILED)
