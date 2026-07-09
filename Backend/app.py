from flask import Flask
from flask_login import LoginManager
from auth import User

from routes import register_routes

app = Flask(__name__)

app.secret_key = "devops-control-center-secret-key"

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)