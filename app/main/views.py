from unittest import result
from flask.views import MethodView
from flask import jsonify, request

from app.schema import ArithmeticSchema

class Main(MethodView):

    def get(self):

        response = {
            "slackUsername": "gibson gichuru",
            "backend":True,
            "age":22,
            "bio":"am a fullstack webdeveloper with two years work experience"
        }

        return jsonify(response)

    def post(self):

        request_data = request.get_json()

        schema = ArithmeticSchema()

        # pass the request data to the schema for validation
        errors = schema.validate(request_data)
        # return any errors found by the schema

        if errors:

            return jsonify({
                "errors":errors
            }), 400

        operation_type = request_data.get("operation_type")

        x = request_data.get("x")

        y = request_data.get("y")

        results = None

        if operation_type == "addition":

            results = x + y
        elif operation_type == "subtraction":

            results = x - y
        else:

            results = x * y

        # perform operations

        res_results = {"slackUsername":"gibson gichuru", "result":results}


        return jsonify(res_results)