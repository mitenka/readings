from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return '<Reading %r>' % self.id
