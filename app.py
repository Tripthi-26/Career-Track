from pathlib import Path
from flask import Flask
from config import Config
from models import db
from routes.auth import auth_bp
from routes.applications import applications_bp
from routes.dashboard import dashboard_bp
from routes.resumes import resumes_bp
from routes.matcher import matcher_bp
from routes.exports import exports_bp
from routes.api import api_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    Path(app.config["UPLOAD_FOLDER"]).mkdir(parents=True, exist_ok=True)
    Path(app.config["UPLOAD_FOLDER"]).parent.parent.joinpath("database").mkdir(
        parents=True, exist_ok=True
    )

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(applications_bp)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
