from mongoengine import *
from ..helper import *

class Role(Document):
    name = StringField(primary_key=True)
    can_create = BooleanField(required=True)
    can_print = BooleanField(required=True)
    can_certify = BooleanField(required=True)

    modifiable_fields = ['name', 'can_create', 'can_print', 'can_certify']

    meta = {"db_alias": "default", 'collection': 'roles'}