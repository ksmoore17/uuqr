from . import mongo

# proxy for mongo.Unit
class Unit:
    def __new__(cls, **kwargs):
        db = "mongodb"
        if db == "mongodb":
            return mongo.Unit.create(**kwargs)

class Series:
    def __new__(cls, **kwargs):
        db = "mongodb"
        if db == "mongodb":
            return mongo.Series.create(**kwargs)
