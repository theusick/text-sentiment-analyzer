from pathlib import Path

from .base import FileParser
from .docx_parser import DocxParser
from .pdf_parser import PdfParser

PARSERS = [DocxParser, PdfParser]


def get_parser(file_path: Path) -> FileParser:
    ext = file_path.suffix.lower()
    for parser in PARSERS:
        if parser.supports(ext):
            return parser
    raise ValueError(f"No parser available for {ext}")
