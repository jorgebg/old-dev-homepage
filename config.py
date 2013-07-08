class Configuration:
    DATABASE = {
        'name': 'app.db',
        'engine': 'peewee.SqliteDatabase',
    }
    DEBUG = True
    SECRET_KEY = 'random'