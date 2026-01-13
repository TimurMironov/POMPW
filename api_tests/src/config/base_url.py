import os


class Host:
    BASE_URL = "https://dev-gs.qa-playground.com/api/v1/setup" if os.getenv(
        "HOST") == 'qa' else "https://release-gs.qa-playground.com/api/v1"
