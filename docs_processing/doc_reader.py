from pathlib import Path
from typing import List

from .parsers import get_parser, PARSERS


def read_file(file_path: Path) -> str:
    parser = get_parser(file_path)
    return parser.parse(file_path)


def get_docs_paths(directory: Path) -> List[Path]:
    extensions = set()
    for parser in PARSERS:
        extensions.update(parser.supported_extensions())

    return [
        p for p in directory.glob("*") if p.suffix.lower() in extensions and p.is_file()
    ]
