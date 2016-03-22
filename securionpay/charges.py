from securionpay.resource import Resource


class Charges(Resource):
    def create(self, params):
        return self.request('POST', self.url(), params)

    def get(self, id):
        return self.request('GET', self.instance_url(id))

    def update(self, id, params):
        return self.request('POST', self.instance_url(id), params)

    def list(self, params=None):
        return self.request('GET', self.url(), params)['list']

    def capture(self, charge_id):
        return self.request('POST', self.instance_url(charge_id, ['capture']))

    def refund(self, charge_id, params=None):
        return self.request('POST', self.instance_url(charge_id, ['refund']), params)
