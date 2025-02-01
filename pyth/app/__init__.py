from flask import Flask
from flask_restx import Api
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app, title="Vetty Market API", version="1.0", description="API for fetching cryptocurrency market updates")

    from .routes import ns as crypto_ns
    api.add_namespace(crypto_ns)

    return app