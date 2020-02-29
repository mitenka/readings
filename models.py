from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    @classmethod
    def get_statistics(cls):
        readings = cls.query.all()
        count = len(readings)
        mean = cls.query.with_entities(db.func.avg(cls.value)).one()[0]
        variance = sum((reading.value - mean) ** 2 for reading in readings) / count

        return {
            'count': count,
            'mean': str(mean),
            'variance': str(variance)
        }

    def __repr__(self):
        return '<Reading %r>' % self.id
