from tests import BaseTestConfig


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