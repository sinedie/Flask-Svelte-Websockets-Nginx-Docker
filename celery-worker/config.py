import os

# Enviroment
ENV = os.environ.get("ENV")

# Redis
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_DB = os.environ['REDIS_DB']

# REDIS_URI = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
REDIS_URI = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'


class Config:
    ENV = ENV
    DEBUG = False
    TESTING = False
    REDIS_URI = REDIS_URI


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


if ENV == 'production':
    config = ProdConfig()
elif ENV == 'development':
    config = DevConfig()
elif ENV == 'testing':
    config = TestConfig()