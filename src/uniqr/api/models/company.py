from mongoengine import *
from ..helper import *

from exceptions import ExistenceError, PurposeError

class Company(Document):
    name = StringField(required=True)

    modifiable_fields = ['name']

    meta = {'allow_inheritance': True, "db_alias": "default", 'collection': 'companies'}

    def get(self, kwargs):
        # if kwargs empty, return all
        return Company.objects.get(kwargs).to_json()

    def create(self, company_data):
        # check for a company with this name already (might need to change)
        try:
            # company required payload keys
            pl_name = company_data['name']

            if Company.objects(name=pl_name):
                raise ExistenceError(pl_name)
            
            # create candidate company ids until one is not in the database
            created = False
            while not created:
                cid = create_alphanumeric_id(6)
                # if pid does not already exist
                if not Company.objects(company_id=cid):
                    c = Company(company_id=cid, name=pl_name)

                    c.save()
        except ExistenceError:
            print("Company:" + pl_name + "already exists")

        except:
            print("Company creation failed")

        return c
    
    def modify(self, cid, company_data):
        try:
            c = Company.objects.get(company_id=cid)
            for old_attr in c._fields.keys():
                for new_attr in request.json.keys():
                    if new_attr == old_attr:
                        if old_attr in Company.modifiable_fields:
                            setattr(c, old_attr, company_data[old_attr])

            c.save()

        except MultipleObjectsReturned:
            print("Company \'" + cid + "\' is duplicated")

        except DoesNotExist:
            print("Company \'" + cid + "\' does not exist")

        except:
            print("Company alteration failed")

        return c

    def delete(self, cid):
        try:
            c = Company.objects.get(company_id=cid)
            c.delete()

        except MultipleObjectsReturned:
            print("Company \'" + cid + "\' is duplicated")

        except DoesNotExist:
            print("Company \'" + cid + "\' does not exist")

        except:
            print("Company deletion failed")