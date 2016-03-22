from securionpay.resource import Resource


class Customers(Resource):
    def create(self, params):
        return self.request('POST', self.url(), params)

    def get(self, id):
        return self.request('GET', self.instance_url(id))

    def update(self, id, params):
        return self.request('POST', self.instance_url(id), params)

    def delete(self, id):
        return self.request('DELETE', self.instance_url(id))

    def list(self, params=None):
        return self.request('GET', self.url(), params)['list']
