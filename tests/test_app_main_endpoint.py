from tests import BaseTestConfig

from flask import json

class TestAppEndPoints(BaseTestConfig):

    def setUp(self):

        super().setUp()

        self.client = self.app.test_client()


    def test_app_main_endpoint(self):

        response = self.client.get("/api").get_json()

        self.assertDictEqual(response, {
            "slackUsername": "gibson gichuru",
            "backend":True,
            "age":22,
            "bio":"am a fullstack webdeveloper with two years work experience"
        })

    def make_post_request(self, operation_type, num1, num2):

        data = json.dumps({"operation_type":operation_type,"x":num1,"y":num2})

        headers={"content-type": "application/json"}

        res = self.client.post("/api",headers=headers,data=data)

        return res


    def test_arithmetic_endpoint_supports_addition(self):

        response = self.make_post_request("addition",2,3)

        answ = response.get_json()

        self.assertEqual(answ.get("result"), 5)

    def test_arithmetic_endpoint_supports_subtraction(self):

        response = self.make_post_request("subtraction",2,3)

        answ = response.get_json()

        self.assertEqual(answ.get("result"), -1)

    def test_aithmetic_endpoint_supports_multiplication(self):

        response = self.make_post_request("multiplication", 2,3)

        answ = response.get_json()

        self.assertEqual(answ.get("result"), 6)