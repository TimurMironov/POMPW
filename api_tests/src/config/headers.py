import os

from dotenv import load_dotenv

load_dotenv()

class Headers:
    BASE_HEADERS = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
    }
