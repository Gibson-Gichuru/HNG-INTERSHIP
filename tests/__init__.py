import unittest

from app import create_app

from config import config_object

class BaseTestConfig(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config = "testing")

        self.app_context = self.app.app_context()

        self.app_context.push()

    def tearDown(self):

        self.app_context.pop()

        self.app = None

