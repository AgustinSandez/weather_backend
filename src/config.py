class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'tutiempo_url': 'https://api.tutiempo.net/json/?lan=es&apid=awYXaXqqzaX7wwg&lid=3768'
}