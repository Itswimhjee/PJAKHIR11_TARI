from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .models import models
    with app.app_context():
        db.create_all()
        if not models.Tari.query.first():
            db.session.add_all([
                models.Tari(nama="Tari Gending Sriwijaya", asal="Sumatera Selatan"),
                models.Tari(nama="Tari Saman", asal="Aceh"),
                models.Tari(nama="Tari Jaipong", asal="Jawa Barat")
            ])
            db.session.commit()

    from app.controllers import tari_bp
    app.register_blueprint(tari_bp)

    return app
