import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\t\x93\x19 \xb7\xb9\xb9x/N{\x12\xf3\xf2\x8b\xa6'

    MONGODB_SETTINGS = { 'db' : 'Tech_Enroll'}