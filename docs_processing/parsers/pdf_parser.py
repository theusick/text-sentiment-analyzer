from pathlib import Path
from PyPDF2 import PdfReader
from .base import FileParser


class PdfParser(FileParser):
    @classmethod
    def parse(cls, file_path: Path) -> str:
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            return "\n".join(page.extract_text() for page in reader.pages)

    @classmethod
    def supported_extensions(cls) -> list[str]:
        return [".pdf"]
