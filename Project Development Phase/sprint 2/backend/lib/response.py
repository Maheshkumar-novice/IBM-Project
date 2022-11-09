from flask import jsonify


def response(status_code, status='success', data={}, message=''):
    response_data = {
        'status_code': status_code,
        'status': status,
        'data': data,
        'message': message
    }
    return jsonify(response_data), status_code