
class Config:

    DEBUG=True

    @staticmethod
    def init_app(app):

        pass

class Development(Config):

    pass

class Testing(Config):

    TESTING = True 

class Production(Config):

    DEBUG = False

config_object = {
    "default":Development,
    "development":Development,
    "testing": Testing,
    "production": Production
}