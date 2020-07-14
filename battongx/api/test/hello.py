import json

from flask import g, current_app, render_template, Blueprint
from flask_restful import Resource, reqparse


class Hello(Resource):
    def get(self):
        print(100)
        return {
            'code': 200,
            'message': 'Success',
            'data': {
                'data': 'Hello'
            }
        }, 200
