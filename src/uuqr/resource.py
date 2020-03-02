# base for mongo.Resource, *.Resource, etc.
class Resource:
    def __init__(self, domain, *args, **kwargs):
        init = self._init_helper(domain, *args, **kwargs)
        self.subdomain = init['subdomain']
        self.domain = init['domain']
        self.port = init['port']
        self.path = init['path']

    @staticmethod
    def _init_helper(domain, subdomain=None, port=None, path=None, *args, **kwargs):
        init = {}

        init['subdomain'] = subdomain
        init['domain'] = domain
        init['port'] = port
        init['path'] = path

        for key, value in kwargs.items():
            init[key] = value

        return init

    # def modify(self, host, subdomain=self.subdomain, port=self.port, path=self.path, *args, **kwargs):
    #     create_helper()

    def get_url(self):
        return "{0}{1}{2}{3}".format(
            self.subdomain + '.' if self.subdomain else '',
            self.domain,
            ':' + self.port if self.port else '',
            (('/' + dir) for dir in self.path) if self.path else ''
        )
