from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from views.post import post_bp
from views.user import user_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(post_bp)
app.register_blueprint(user_bp)


@app.route("/")
def index():
    return {"message": "Server is running"}


if __name__ == "__main__":
    app.run(port=5000, debug=True)