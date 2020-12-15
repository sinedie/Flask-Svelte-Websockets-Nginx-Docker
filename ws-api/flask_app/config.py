import os

# Flask env
FLASK_ENV = os.environ.get("FLASK_ENV")
SECRET_KEY = os.environ.get("SECRET_KEY")

# Redis
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_DB = os.environ['REDIS_DB']

# REDIS_URI = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
REDIS_URI = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'


class Config:
    FLASK_ENV = FLASK_ENV
    SECRET_KEY = SECRET_KEY
    REDIS_URI = REDIS_URI
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


if FLASK_ENV == 'production':
    config = ProdConfig()
elif FLASK_ENV == 'testing':
    config = TestConfig()
else:
    config = DevConfig()