from typing import Any
from fastapi import status

class GlobalException(Exception):
    """Generic api exception"""

    def __init__(self, status_code: status, content: Any) -> None:
        self.status = content
        self.message = content
        super().__init__()