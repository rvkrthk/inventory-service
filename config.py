import os

class Config:
    """
    Configuration
    """
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME', 'qtdevops')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'qtdevops')
    MYSQL_SERVER = os.getenv('MYSQL_SERVER', 'localhost')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'qtinvsrv')
    DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DATABASE}"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
