


class Config(object):
    DEBUG=False
    TESTING=False
    SECRET_KEY=None
    DB_NAME=""
    DB_USERNAME=""
    DB_PASSWORD=""

class ProductionConfig(Config):
    DEBUG=False
    TESTING=False
    SECRET_KEY="fgdgfdgd589gfd"
    DB_NAME="/home/ayoub/devHacking/python/fileScan/database/database.db"
    DB_USERNAME=""
    DB_PASSWORD=""
    UPLOADS="/home/ayoub/devHacking/python/fileScan/uploads"
    IP_BAN_LIST_COUNT=0
    IP_BAN_LIST_SECONDS=0

class DevelopmentConfig(Config):
    DEBUG=False
    TESTING=False
    SECRET_KEY=None
    DB_NAME="/home/ayoub/devHacking/python/fileScan/database/database.db"
    DB_USERNAME=""
    DB_PASSWORD=""
    UPLOADS="/home/ayoub/devHacking/python/fileScan/uploads"


class TestingConfig(Config):
    
    TESTING=True
    SECRET_KEY=None
    DB_NAME=""
    DB_USERNAME=""
    DB_PASSWORD=""