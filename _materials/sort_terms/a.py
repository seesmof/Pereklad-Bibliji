import os

current_dir: str = os.path.dirname(os.path.abspath(__file__))
terms_file_path: str = os.path.join(current_dir, "..", "Terms.yml")


def detect_duplicates(): ...


def safe_split(text: str, sep: str) -> list:
    return text.partition(sep)


Bible_terms: list[str] = []
with open(terms_file_path, "r", encoding="utf-8") as file:
    for line in file:
        Bible_terms.append(line.strip())

Bible_terms = sorted(Bible_terms)

with open(terms_file_path, "w", encoding="utf-8") as file:
    for term in Bible_terms:
        file.write(f"{term}\n")
