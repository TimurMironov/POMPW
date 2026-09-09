from urllib.parse import urljoin

import requests

from api_tests.src.config.headers import Headers
from api_tests.src.config.logger import logger
from api_tests.src.config.settings import Settings


class BaseClient:
    def __init__(self, settings: Settings, headers: dict = None):
        self.session = requests.Session()
        self.session.headers.update(headers or Headers.BASE_HEADERS)
        self.settings = settings

    def _url(self, endpoint):
        return urljoin(self.settings.base_url, endpoint)

    def request(self, method, endpoint, **kwargs):
        logger.info("%s %s", method, endpoint)
        logger.debug("Request kwargs: %s", kwargs)
        try:
            response = self.session.request(
                method=method,
                url=self._url(endpoint),
                timeout=self.settings.timeout,
                **kwargs,
            )
        except requests.exceptions.RequestException as e:
            logger.exception("%s %s | RequestException - %s", method, endpoint, e)
            raise
        logger.debug("Response status: %s", response.status_code)
        logger.debug("Response body: %s", response.text)
        return response
