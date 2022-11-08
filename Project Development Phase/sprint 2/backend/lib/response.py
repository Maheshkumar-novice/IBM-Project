from flask import jsonify
from lib.response_status_codes import *


class Response():
    @staticmethod
    def success(data={}, message='', status_code=REQUEST_COMPLETED):
        response = {
            'status': 'success',
            'status_code': status_code,
            'data': data,
            'message': message
        }
        return jsonify(response), status_code

    @staticmethod
    def error(data={}, message='', status_code=INTERNAL_SERVER_ERROR):
        response = {
            'status': 'error',
            'status_code': status_code,
            'data': data,
            'message': message
        }
        return jsonify(response), status_code