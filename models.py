from peewee import *
from app import db

def __modelstr__(self):
    candidates = ('title', 'name', 'description', 'id')
    for candidate in candidates:
        if hasattr(self, candidate):
            return str(getattr(self, candidate))

db.Model.__str__ = __modelstr__

class Job(db.Model):
    content = TextField()
    title = CharField()

class Company(db.Model):
    content = TextField()
    location = TextField()
    title = CharField()
    url = CharField()

class Education(db.Model):
    content = TextField()
    end_date = DateField(null=True)
    location = TextField()
    start_date = DateField()
    title = CharField()

class Tech(db.Model):
    title = CharField()
    content = TextField()
    url = CharField()

class Experience(db.Model):
    company = ForeignKeyField(Company)
    end_date = DateField()
    job = ForeignKeyField(Job)
    start_date = DateField()

class ExperienceTech(db.Model):
    description = TextField()
    experience = ForeignKeyField(Experience)
    level = IntegerField(null=True)
    tech = ForeignKeyField(Tech)

class Achievements(db.Model):
    description = TextField()
    experience = ForeignKeyField(Experience)

class Interest(db.Model):
    description = TextField()

class Profile(db.Model):
    name = CharField()
    address = CharField()
    email = CharField()
    phone = CharField()
    description = TextField()

class ProfileTech(db.Model):
    description = TextField()
    level = IntegerField()
    tech = ForeignKeyField(Tech)

class Reference(db.Model):
    company = ForeignKeyField(Company, null=True)
    email = CharField()
    phone = CharField(null=True)
    title = CharField()
    url = CharField()
