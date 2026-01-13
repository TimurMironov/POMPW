from urllib.parse import urljoin

import requests

from api_tests.src.config.base_url import Host
from api_tests.src.config.headers import Headers


class BaseClient:

    def __init__(self, headers: dict = None):
        self.host = Host()
        self.session = requests.Session()
        self.session.headers.update(headers or Headers.BASE_HEADERS)

    def _url(self, endpoint):
        return urljoin(self.host.BASE_URL, endpoint)

    def get(self, endpoint, **kwargs):
        return self.session.get(self._url(endpoint), **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self.session.post(self._url(endpoint), data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, **kwargs):
        return self.session.put(self._url(endpoint), data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.session.delete(self._url(endpoint), **kwargs)
