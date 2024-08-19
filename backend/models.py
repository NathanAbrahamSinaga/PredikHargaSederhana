from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PredictionData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Float, nullable=False)