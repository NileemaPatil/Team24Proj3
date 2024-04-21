from datetime import datetime

from .. import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    file_text = db.Column(db.Text, nullable=False)
    uploaded_by = db.Column(db.Text, nullable=False)
    uploaded_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sentences = db.relationship('Sentence', backref='project', lazy=True)
