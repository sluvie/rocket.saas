import logging

TIMEZONE = 'Europe/Paris'

# DEBUG can only be set to True in a development environment for security reasons
DEBUG = True

# secret key for generating tokens
SECRET_KEY = "rocket.cms"

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'Pa$$word')

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'flask.rocket'
MAIL_PASSWORD = 'rocket123'
ADMINS = ['flask.rocket@gmail.com']

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

LOG_LEVEL = logging.DEBUG
LOG_FILENAME = 'activity.log'
LOG_MAXBYTES = 1024
LOG_BACKUPS = 2