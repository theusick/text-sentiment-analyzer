from pathlib import Path, PurePath
from typing import Final


ROOT_DIR: Final[Path] = Path(__file__).parent.parent
DICT_DIR: Final[Path] = ROOT_DIR / "data" / "dictionary.xlsx"
DOCS_DIR: Final[Path] = ROOT_DIR / "data" / "docs"

OUTPUT_FILE: Final[Path] = ROOT_DIR / "result.csv"
