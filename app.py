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


@app.errorhandler(404)
def page_not_found(e):
    return {'detail': 'Not found.'}, 404

