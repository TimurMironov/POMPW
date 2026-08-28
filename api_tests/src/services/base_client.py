from urllib.parse import urljoin

import requests

from api_tests.src.config.base_url import Host
from api_tests.src.config.headers import Headers
from api_tests.src.config.logger import logger


class BaseClient:
    def __init__(self, headers: dict = None):
        self.host = Host()
        self.session = requests.Session()
        self.session.headers.update(headers or Headers.BASE_HEADERS)

    def _url(self, endpoint):
        return urljoin(self.host.BASE_URL, endpoint)

    def request(self, method, endpoint, **kwargs):
        logger.info("%s %s", method, endpoint)
        logger.debug("Request kwargs: %s", kwargs)
        response = self.session.request(
            method=method,
            url=self._url(endpoint),
            **kwargs,
        )
        logger.debug("Response status: %s", response.status_code)
        logger.debug("Response body: %s", response.json())
        return response
