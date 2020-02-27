from marshmallow import (
    Schema,
    fields,
)


class ReadingSchema(Schema):
    id = fields.Integer(dump_only=True)
    value = fields.Float(required=True, as_string=True)
    timestamp = fields.DateTime(dump_only=True)
