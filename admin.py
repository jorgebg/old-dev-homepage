#!/usr/bin/env python
from app import db, app

from flask_peewee.auth import Auth
from flask_peewee.admin import Admin

auth = Auth(app, db)       
admin = Admin(app, auth)

for model in db.models:
    admin.register(model)

admin.setup()

if __name__ == '__main__':
    app.run()