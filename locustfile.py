import gevent
from locust import FastHttpUser, task

endpoints = [
    '/api/city',
    '/api/country',
    '/api/credential',
    '/api/establishment',
    '/api/information_about_owner',
    '/api/review',
    '/api/street',
    '/api/type_of_establishment',
    '/api/type_of_establishment',
]


class UserPool(FastHttpUser):
    @task
    def generate_all_requests(self):
        def request(endpoint):
            self.client.get(endpoint, auth=("user", "Test12345"))

        pool = gevent.pool.Pool()

        for endpoint in endpoints:
            pool.spawn(request, endpoint)

        pool.join()
