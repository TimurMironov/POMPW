from dataclasses import dataclass
from typing import Any


@dataclass
class InvalidDataCase:
    field: str
    value: Any
    expected_status: int
    expected_error: str
