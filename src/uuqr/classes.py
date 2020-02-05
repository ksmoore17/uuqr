from .exceptions import PurposeError, WrongStatusError
from .helper import create_alphanumeric_id

# base for mongo.Unit, *.Unit, etc.
class Unit:
    #
    # redefine __init__ function on multiple inheritance
    # mongoengine example:
    #
    ##########################################################################
    #
    #    def __init__(self, **kwargs):
    #        b = BaseUnit(**kwargs)
    #        rs = [Registration(purpose='create', datetime=datetime.now())]
    #        return super(Document, self).__init__(
    #            code=b.code,
    #            status=b.status,
    #            registrations=rs,
    #            **kwargs)
    #
    def __init__(self, *args, **kwargs):
        return self.create_helper(**kwargs)


    def create_helper(self, code=create_alphanumeric_id(10), resource=None, *args, **kwargs):
        ## get_uuid()
        self.code = code
        self.status = "created"
        self.resource = resource

    # redefine _helper functions on inheritance
    def certify_helper(self):
        return self

    def certify(self, resource, *args, **kwargs):
        print(kwargs)
        # see if the code is fresh
        if self.status == 'created':
            self.status = 'certified'
            self.resource = resource
            return self.certify_helper(resource, *args, **kwargs)

        # elif self.registration.status == 'certified':
        #     raise WrongStatusError(u.registration.status)

        else:
            raise WrongStatusError(self.status)

    def authenticate_helper(self):
        return self

    def authenticate(self):
        # see if the unit has been assigned a product
        if self.status == 'certified':
            self.status = 'authenticated'
            return self.authenticate_helper()

        else:
            raise WrongStatusError(self.status)

    def get_url(self):
        return "{}{}".format(
            self.resource.get_url() + '/' if self.resource else '',
            self.code
        )

class Resource:
    def __init__(self, host, *args, **kwargs):
        return self.create_helper(host, *args, **kwargs)

    def create_helper(self, host, subdomain=None, port=None, path=None, *args, **kwargs):
        self.subdomain = subdomain
        self.host = host
        self.port = port
        self.path = path

    # def modify(self, host, subdomain=self.subdomain, port=self.port, path=self.path, *args, **kwargs):
    #     create_helper()

    def get_url(self):
        return "{0}{1}{2}{3}".format(
            self.subdomain + '.' if self.subdomain else '',
            self.host,
            ':' + self.port if self.port else '',
            (('/' + dir) for dir in self.path) if self.path else ''
        )
