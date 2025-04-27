from docx import Document
from pathlib import Path
from .base import FileParser


class DocxParser(FileParser):
    @classmethod
    def parse(cls, file_path: Path) -> str:
        doc = Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs)

    @classmethod
    def supported_extensions(cls) -> list[str]:
        return [".docx", ".doc"]
