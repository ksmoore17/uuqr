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
        ## get_uuid()
        return {
            'subdomain' : subdomain,
            'host' : host,
            'port' : port,
            'path' : path
        }

    # def modify(self, host, subdomain=self.subdomain, port=self.port, path=self.path, *args, **kwargs):
    #     create_helper()

    def get_url(self):
        return "{0}{1}{2}{3}".format(
            self.subdomain + '.' if self.subdomain else '',
            self.host,
            ':' + self.port if self.port else '',
            (('/' + dir) for dir in self.path) if self.path else ''
        )
