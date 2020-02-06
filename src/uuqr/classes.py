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
        init = self._init_helper(*args, **kwargs)
        self.code = init['code']
        self.status = init['status']
        self.resource = init['resource']

    @staticmethod
    def _init_helper(code=create_alphanumeric_id(10), resource=None, status='created', *args, **kwargs):
        ## get_uuid()
        return {
            'code' : code,
            'status' : status,
            'resource' : resource
        }

    # redefine _helper functions on inheritance
    @staticmethod
    def _certify_helper(curr_status, resource):
        # see if the code is fresh
        if curr_status == 'created':
            return {
                'status' : 'certified',
                'resource' : resource
            }
        # elif self.registration.status == 'certified':
        #     raise WrongStatusError(u.registration.status)
        else:
            raise WrongStatusError(self.status)

    def certify(self, resource, *args, **kwargs):
        cert = self._certify_helper(self.status, resource)
        self.status = cert['status']
        self.resource = cert['resource']

        return self

    @staticmethod
    def _authenticate_helper(curr_status):
        # see if the code has a product
        if curr_status == 'certified':
            return {
                'status' : 'authenticated'
            }
        # elif self.registration.status == 'authenticated':
        #     raise WrongStatusError(u.registration.status)
        else:
            raise WrongStatusError(self.status)

    def authenticate(self):
        auth = self._authenticate_helper(self.status)
        self.status = auth['status']

        return self

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
