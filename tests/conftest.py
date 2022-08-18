import pytest
from flask import Flask
from routes import configure_routes

@pytest.fixture()
def app():
  app = Flask(__name__)
  configure_routes(app)

  yield app

@pytest.fixture()
def client(app):
  return app.test_client()

@pytest.fixture()
def runner(app):
  return app.test_cli_runner()
