import os

from dotenv import load_dotenv

load_dotenv()

class Data:

    def __init__(self):
        self.LOGIN = os.getenv("LOGIN")
        self.PASSWORD = os.getenv("PASSWORD")