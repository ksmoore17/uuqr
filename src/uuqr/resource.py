# base for mongo.Resource, *.Resource, etc.
class Resource:
    def __init__(self, host, *args, **kwargs):
        init = self._init_helper(host, *args, **kwargs)
        self.subdomain = init['subdomain']
        self.host = init['host']
        self.port = init['port']
        self.path = init['path']

    @staticmethod
    def _init_helper(host, subdomain=None, port=None, path=None, *args, **kwargs):
        init = {}

        init['subdomain'] = subdomain
        init['host'] = host
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
            self.host,
            ':' + self.port if self.port else '',
            (('/' + dir) for dir in self.path) if self.path else ''
        )
