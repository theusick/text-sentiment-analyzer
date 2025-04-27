import pandas as pd
from pathlib import Path
from typing import Dict, List, Set, TypedDict


class KeywordDict(TypedDict):
    over: Set[str]
    under: Set[str]
    neutral: Set[str]


def load_keywords(dict_path: Path) -> KeywordDict:
    keywords: KeywordDict = {"over": set(), "under": set(), "neutral": set()}

    df = pd.read_excel(dict_path)
    for _, row in df.iterrows():
        word = row["lemma"].strip().lower()
        if row["overconfidence"] == "overconfidence":
            keywords["over"].add(word)
        elif row["underconfidence"] == "underconfidence":
            keywords["under"].add(word)
        else:
            keywords["neutral"].add(word)

    return keywords


def count_keywords(words: list[str], keywords: KeywordDict) -> Dict[str, int]:
    return {
        "over": sum(1 for w in words if w in keywords["over"]),
        "under": sum(1 for w in words if w in keywords["under"]),
        "neutral": sum(1 for w in words if w in keywords["neutral"]),
    }


def calculate_sentiment(over: int, under: int, neutral: int) -> float:
    denominator = over + under + neutral
    if denominator == 0:
        return 0.0
    return (over - under) / denominator
