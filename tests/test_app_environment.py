from tests import BaseTestConfig

class TestApplicationEvironment(BaseTestConfig):

    def test_application_is_in_test_mode(self):

        self.assertTrue(self.app.config['TESTING'])

        

        