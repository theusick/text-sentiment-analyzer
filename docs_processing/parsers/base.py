from abc import ABC, abstractmethod
from pathlib import Path


class FileParser(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, file_path: Path) -> str:
        pass

    @classmethod
    def supports(cls, ext: str) -> bool:
        return ext.lower() in cls.supported_extensions()

    @classmethod
    @abstractmethod
    def supported_extensions(cls) -> list[str]:
        pass
