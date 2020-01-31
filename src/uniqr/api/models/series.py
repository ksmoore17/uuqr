from mongoengine import URLField
from ..helper import *

class Series(Document):
    domain = UrlField(primary_key=True)

    meta = {'allow_inheritance': True, "db_alias": "default", 'collection': 'identifier'}

    @classmethod
    def get(cls, **kwargs):
        # launch authenticate page
        return cls.objects.get(kwargs)

    @classmethod
    def create(cls, **kwargs):
        # create candidate product ids until one is not in the database
        s = cls(**kwargs)

                s.save()

        return s

    def update(self):
        pass

    def modify(self, company_data):
        for old_attr in self._fields.keys():
            for new_attr in request.json.keys():
                if new_attr == old_attr:
                        setattr(self, old_attr, company_data[old_attr])

        self.save()

        return self

    def delete(self):
        self.delete()
