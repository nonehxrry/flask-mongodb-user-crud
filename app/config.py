class Config:
    MONGO_URI = "mongodb://mongo:27017/user_db"
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass