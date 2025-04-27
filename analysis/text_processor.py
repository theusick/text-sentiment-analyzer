import re
from pymorphy3 import MorphAnalyzer
from typing import List, Final

morph = MorphAnalyzer()
RE_WORD: Final = re.compile(r"\b[а-яё]+\b", re.I)


def process_text(text: str) -> List[str]:
    words = RE_WORD.findall(text.lower())
    return [morph.parse(word)[0].normal_form for word in words]
