import sys
from tqdm import tqdm
from pathlib import Path
from typing import Dict, List, Tuple

from utils.paths import DICT_DIR, DOCS_DIR, OUTPUT_FILE
from docs_processing import read_file, get_docs_paths
from analysis import load_keywords, count_keywords, calculate_sentiment, process_text
from reporting import save_to_csv


def main() -> None:
    keywords = load_keywords(DICT_DIR)
    docs: List[Path] = get_docs_paths(DOCS_DIR)
    results: List[Tuple[str, int, int, int]] = []
    errors: Dict[str, str] = {}

    with tqdm(docs, desc="Processing documents", unit="file") as pbar:
        for doc_path in pbar:
            pbar.set_postfix_str(doc_path.name)
            try:
                # Чтение очередного файла
                text = read_file(doc_path)
                # Приведение слов в тексте к нормальной форме
                words = process_text(text)
                # Подсчет параметров (overconfidence, underconfidence, neutral -
                #   ни то, ни другое)
                counts = count_keywords(words, keywords)

                # Расчет тональности текста
                sentiment = calculate_sentiment(
                    counts["over"], counts["under"], counts["neutral"]
                )

                results.append(
                    (
                        doc_path.name,
                        counts["over"],
                        counts["under"],
                        counts["neutral"],
                        sentiment,
                    )
                )

            except Exception as e:
                error_msg = f"{type(e).__name__}: {str(e)}"
                errors[doc_path.name] = error_msg
                tqdm.write(
                    f"Error in file {doc_path.name}: {error_msg}", file=sys.stderr
                )

    save_to_csv(results, OUTPUT_FILE)
    print(f"\nResults saved in {OUTPUT_FILE}")

    if errors:
        print("\nErrors during file processing:")
        for file, error in errors.items():
            print(f"- {file}: {error}")


if __name__ == "__main__":
    main()
