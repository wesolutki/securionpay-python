from securionpay.resource import Subresource


class Cards(Subresource):
    def __init__(self):
        super(self.__class__, self).__init__('customers')

    def create(self, customer_id, params):
        return self.request('POST', self.url(customer_id), params)

    def get(self, customer_id, id):
        return self.request('GET', self.instance_url(customer_id, id))

    def update(self, customer_id, id, params):
        return self.request('POST', self.instance_url(customer_id, id), params)

    def delete(self, customer_id, id):
        return self.request('DELETE', self.instance_url(customer_id, id))

    def list(self, customer_id, params=None):
        return self.request('GET', self.url(customer_id), params)['list']
