import os

import sys

from app import create_app

from config import config_object

app = create_app(config = os.environ.get("FLASK_ENV")  or  "default" )


# Test running command

@app.cli.command()
def test():

    import unittest

    tests = unittest.TestLoader().discover("tests")

    results = unittest.TextTestRunner(verbosity = 2).run(tests)

    if not results.wasSuccessful():

        sys.exit()



