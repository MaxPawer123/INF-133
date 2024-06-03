import pytest
from flask_jwt_extended import create_access_token
#configuramos en app

#create_access_token =cuando se crea un token 
from app.database import db
from app.run import app

@pytest.fixture(scope="module")

def test_client():
    #esta configurado por app 
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:" #una memoria temporal que no tiene registrarse 
    app.config["JWT_SECRET_KEY"] = "test_secret_key"

    with app.test_client() as testing_client: # levanta el servidor el with
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()


@pytest.fixture(scope="module")
def admin_auth_headers():
    with app.app_context():
        access_token = create_access_token(
            identity={"username": "testuser", "roles": '["admin"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers


@pytest.fixture(scope="module")
def user_auth_headers():
    with app.app_context():
        access_token = create_access_token(
            identity={"username": "user", "roles": '["user"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers
