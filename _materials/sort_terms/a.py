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
for term in Bible_terms:
    original, translation = term.split(":", 1)
    original, translation = original.strip(), translation.strip()

    translation = safe_split(translation, ";")
    translation = [
        translation.strip()
        for translation in translation
        if translation != ";" and translation != ""
    ]
    affirmed: str = translation[0]
    options: list[str] | None = translation[1:]
    if options:
        options = options[0].split(",")
        options = [option.strip() for option in options if option != ""]
    print(f"{original}:{affirmed};{','.join(options) if options else ''}")
