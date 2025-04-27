import csv
from pathlib import Path
from typing import List, Tuple


def save_to_csv(results: list, output_path: Path) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["File", "Over", "Under", "Neutral", "Sentiment"])
        for row in results:
            writer.writerow(row)
