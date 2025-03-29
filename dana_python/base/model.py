from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, List
from datetime import datetime
from typing_extensions import Self

class BaseSdkModel(ABC):
    """Interface for Model clas in SDK."""

    @abstractmethod
    def to_str(self) -> str:
        pass

    @abstractmethod
    def to_json(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        pass