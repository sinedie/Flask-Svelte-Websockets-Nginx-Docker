import os

# Flask env
FLASK_ENV = os.environ.get("FLASK_ENV")
SECRET_KEY = os.environ.get("SECRET_KEY")

# JWT
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES"))

# Postgres
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

# Redis
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_DB = os.environ['REDIS_DB']

# REDIS_URI = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
REDIS_URI = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'


class Config:
    FLASK_ENV = FLASK_ENV
    DEBUG = False
    TESTING = False
    SECRET_KEY = SECRET_KEY
    JWT_SECRET_KEY = JWT_SECRET_KEY
    JWT_REFRESH_TOKEN_EXPIRES = JWT_REFRESH_TOKEN_EXPIRES
    SQLALCHEMY_DATABASE_URI = DATABASE_CONNECTION_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URI = REDIS_URI



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