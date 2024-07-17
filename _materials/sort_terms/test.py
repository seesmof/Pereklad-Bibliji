def safe_split(text: str, sep: str) -> list:
    return text.partition(sep)


term: str = "faith,belief:віра,вірувати"
original, translation = term.split(":", 1)
original, translation = original.strip(), translation.strip()
translations = safe_split(translation, ";")
print(f"{original}: {translations}")

term: str = "elder:старець;старішина"
original, translation = term.split(":", 1)
original, translation = original.strip(), translation.strip()
translations = safe_split(translation, ";")
translations = [translation for translation in translations if translation != ";"]
print(f"{original}: {translations}")

term: str = "beware:стерегтися;остерігатися,стережіться"
original, translation = term.split(":", 1)
original, translation = original.strip(), translation.strip()
translations = safe_split(translation, ";")
translations = [translation for translation in translations if translation != ";"]
print(f"{original}: {translations}")
