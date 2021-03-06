from .exceptions import PurposeError, WrongStatusError
from .helper import create_uuid

from .resource import Resource

# base for mongo.Unit, *.Unit, etc.
class Unit:
    #
    #       redefine __init__ function on multiple inheritance
    #           mongoengine example:
    #
    ##########################################################################
    #
    #    # check if document already exists
    #    if '_created' in kwargs.keys():
    #        init = kwargs
    #    else:
    #        init = self._init_helper(**kwargs)
    #        init['registrations'] = [Registration(purpose='create', datetime=datetime.now())]
    #
    #    super().__init__(**init)
    #
    def __init__(self, *args, **kwargs):
        init = self._init_helper(*args, **kwargs)
        self.code = init.pop('code')
        self.status = init.pop('status')
        self.resource = init.pop('resource')

    @staticmethod
    def _init_helper(resource=None, status='created', **kwargs):
        ## get_uuid()
        init = {}

        init['code'] = create_uuid()
        init['status'] = status
        init['resource'] = resource

        for key, value in kwargs.items():
            init[key] = value

        return init

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
            raise WrongStatusError(curr_status)

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
