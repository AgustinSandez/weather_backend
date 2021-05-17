class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

TUTIEMPO_API_LANG = 'es'
TUTIEMPO_API_ID = 'awYXaXqqzaX7wwg'

config = {
    'development': DevelopmentConfig,
    'tutiempo_url': 'https://api.tutiempo.net/json/?lan={}&apid={}&lid={{}}'
        .format(TUTIEMPO_API_LANG, TUTIEMPO_API_ID)
}