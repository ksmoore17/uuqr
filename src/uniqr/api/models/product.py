from mongoengine import *
from ..helper import *

class Product(Document):
    product_id = StringField(primary_key=True, default=create_alphanumeric_id(7))
    name = StringField(required=True)
    company = ReferenceField(Company, required=True)

    modifiable_fields = ['name']

    meta = {'allow_inheritance': True, "db_alias": "default", 'collection': 'products'}
