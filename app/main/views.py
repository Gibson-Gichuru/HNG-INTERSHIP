from flask.views import MethodView
from flask import jsonify

class Main(MethodView):

    def get(self):

        response = {
            "slackUsername": "gibson gichuru",
            "backend":True,
            "age":22,
            "bio":"am a fullstack webdeveloper with two years work experience"
        }

        return jsonify(response)