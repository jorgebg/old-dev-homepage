from app import db

for model in db.models:
    model.create_table()

from admin import auth
auth.User.create_table()
user = auth.User(username='admin', admin=True, email='admin@localhost', active=True)
user.set_password('admin')
user.save()