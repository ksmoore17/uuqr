from mongoengine import *
from ..helper import *
from exceptions import PurposeError, WrongStatusError

STATUSES = ['created', 'certified', 'authenticated']
PURPOSES = ['create', 'certify', 'authenticate']

class Access(EmbeddedDocument):
    agent = ReferenceField(User, required=True)
    purpose = StringField(required=True, choices=PURPOSES)
    dt = DateTimeField(required=True)

    meta = {"db_alias": "default", 'collection': 'accesses'}

class Registration(EmbeddedDocument):
    status = StringField(required=True, choices=STATUSES)
    creation = EmbeddedDocumentField(Access, required=True)
    print = EmbeddedDocumentField(Access)
    certification = EmbeddedDocumentField(Access)
    authentication = EmbeddedDocumentField(Access)

class Unit(Document):
    code = StringField(primary_key=True, max_length=10, min_length=10)
    registration = EmbeddedDocumentField(Registration)
    product = ReferenceField(Product, required=True)

    meta = {'allow_inheritance': True, "db_alias": "default", 'collection': 'units'}

    @classmethod
    def get(cls, **kwargs):
        # launch authenticate page
        return Unit.objects.get(kwargs)

    @classmethod
    def create(cls):
        # create candidate codes until one is not in the database
        created = False
        while not created:
            cd = create_alphanumeric_id(10)
            # if code doesn't already exist
            if not cls.objects(code=cd):
                # create an access record to attach to the creation
                a = Access(agent=agent, purpose='create_unit', dt=datetime.now)
                u = cls(code=cd, registration=Registration(status='created', creation=a))
                u.save()

                created = True

        return u

    def certify(self, cert_data):
        # cert_data must contain the right keys
        if not any(key not in cert_data for key in ['product_id']):
            # see if the code is fresh
            if self.registration.status == 'created':

                # find the product object in the database
                try:
                    p = Product.objects.get(product_id=cert_data['product_id'])

                    a = Access(agent=agent, purpose='certify_unit', dt=datetime.now)

                    # update the unit object
                    self.registration.status = 'certified'
                    self.registration.certification = a
                    self.product = p

                    self.save()
            else:
                raise WrongStatusError(u.registration.status)

        else:
            raise ValueError(key)

        return {'success': success, 'message': message}

    def authenticate(self):
        # see if the unit has been assigned a product
        if self.registration.status == 'certified':
            a = Access(agent=agent, purpose='authenticate_unit', dt=datetime.now)

            # update the unit object
            self.registration.status = 'authenticated'
            self.registration.authentication = a

            self.save()
        else:
            raise WrongStatusError(self.registration.status)

        return self

    def register(self, registration):
        purpose = registation['purpose']

        # need to separate authentication and certification
        if purpose == 'certify':
            # find the unit object to register
            u = Unit.get(code=cd)
            return u.certify(registation['data'])

        elif purpose == 'authenticate':
            # find the unit object to register
            u = Unit.get(code=cd)
            return u.authenticate()

        else:
            raise PurposeError(purpose)
    
    def delete(self):
        self.delete()


