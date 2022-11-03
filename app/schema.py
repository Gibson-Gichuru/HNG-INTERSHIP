from app import ma

from marshmallow import fields, validates, ValidationError, validate

class ArithmeticSchema(ma.Schema):

    operation_type = fields.String(required=True)

    x = fields.Integer(required=True)

    y = fields.Integer(required=True)

    # custom operation type validation logic

    @validates("operation_type")
    def validate_operation_type(self, operation):

        supported_operations = ["addition", "subtraction", "multiplication"]

        if operation.lower() not in supported_operations:

            raise ValidationError("operation_type not supported")