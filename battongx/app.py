import json

from flask import Flask, make_response, current_app
from flask_restful_swagger_2 import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    api = Api(
            app,
            api_version="0.1",
            api_spec_url="/api/spec",
            title="battongx spec",
            catch_all_404s=True,
        )

    from .api.test import Hello

    api.add_resource(Hello, "/")

    with app.app_context():
        CORS(app)

        @api.representation('application/json')
        def output_json(data, code, headers=None):
            resp = make_response(json.dumps(data, ensure_ascii=False), code)
            resp.headers.extend(headers or {})
            return resp

        return app