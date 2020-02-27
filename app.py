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
def page_not_found():
    return {'detail': 'Not found.'}, 404


@app.route('/readings/', methods=['GET', 'POST'])
def readings():
    schema = ReadingSchema()

    if request.method == 'GET':
        pagination = Reading.query.order_by(Reading.timestamp).paginate()
        instances = schema.dump(pagination.items, many=True)
        return {
            'items': instances,
            'page': pagination.page,
            'pages': pagination.pages,
            'total': pagination.total,
        }

    try:
        data = schema.load(request.get_json())
    except ValidationError as e:
        return e.messages, 400

    instance = Reading(value=data['value'])
    db.session.add(instance)
    db.session.commit()

    return schema.dump(instance), 201


@app.route('/readings/<int:pk>/', methods=['GET', 'PUT', 'DELETE'])
def reading(pk):
    schema = ReadingSchema()
    instance = Reading.query.get_or_404(pk)

    if request.method == 'GET':
        return schema.dump(instance)

    if request.method == 'DELETE':
        db.session.delete(instance)
        db.session.commit()
        return {}, 204

    try:
        data = schema.load(request.get_json())
    except ValidationError as e:
        return e.messages, 400

    instance.value = data['value']
    db.session.commit()

    return schema.dump(instance)


@app.route('/statistics/', methods=['GET'])
def statistics():
    return {
        'statistics': 'statistics'
    }
