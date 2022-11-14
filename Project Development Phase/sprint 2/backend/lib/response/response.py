from flask import jsonify

from lib.response.constants import SUCCESS


def response(status_code=200, status=SUCCESS, data={}, message=SUCCESS):
    response_data = {
        'status_code': status_code,
        'status': status,
        'data': data,
        'message': message
    }
    return jsonify(response_data), status_code
