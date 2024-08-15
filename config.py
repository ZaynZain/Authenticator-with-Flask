import os

class Config:
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/Authenticator'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = 'mysecretsalt'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'zayn69zain@gmail.com'  # Directly set email here
    MAIL_PASSWORD = 'scwu xqsx tgsn gmem'  # Directly set password here
    MAIL_DEFAULT_SENDER = 'zayn69zain@gmail.com'



    print(os.environ.get('MAIL_USERNAME'))
    print(os.environ.get('MAIL_PASSWORD'))
