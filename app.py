from flask import (
    Flask,
    request,
)
from marshmallow import ValidationError
from models import (
    db,
    Reading,
)
from schemas import ReadingSchema


app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
