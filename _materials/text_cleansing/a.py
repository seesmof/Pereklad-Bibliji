import os
import re


def remove_usfm_tags(text: str) -> str:
    """
    given text in USFM format, removes all the USFM tags

    IN:
    text (str): text in USFM format

    OUT:
    str: text with removed USFM tags
    """

    def remove_extra_spacing(text: str) -> str:
        """
        removes extra spacing that is not needed

        IN:
        text (str): text to remove extra spacing from

        OUT:
        str: text with removed extra spacing
        """
        clean_text: str = " ".join(text.split())
        lines: list[str] = [
            line.strip() for line in clean_text.splitlines() if line.strip()
        ]
        clean_text = "\n".join(lines).strip()
        return clean_text

    singles: list[str] = ["pmo", "m", "pi", "p", "b", "em"]
    levels: list[str] = ["q", "s"]
    numbers: list[str] = ["c", "v"]
    surroundings_delete: list[str] = ["f", "x"]
    surroundings_leave: list[str] = ["nd", "wj"]

    for single in singles:
        single = r"\\" + single + r"\s*" if "\\" not in single else single
        text = re.sub(single, "", text)

    for level in levels:
        level = r"\\" + level + r"\d*\s*" if "\\" not in level else level
        text = re.sub(level, "", text)

    for number in numbers:
        number = r"\\" + number + r"\s*\d*" if "\\" not in number else number
        text = re.sub(number, "", text)

    for surrounding_delete in surroundings_delete:
        surrounding_delete = (
            (r"\\" + surrounding_delete + r"\s*(.*?)\\" + surrounding_delete + r"\*")
            if "\\" not in surrounding_delete
            else surrounding_delete
        )
        text = re.sub(surrounding_delete, "", text)

    for surrounding_leave in surroundings_leave:
        surrounding_leave = (
            (r"\\" + surrounding_leave + r"\s*(.*?)\\" + surrounding_leave + r"\*")
            if "\\" not in surrounding_leave
            else surrounding_leave
        )
        text = re.sub(surrounding_leave, r"\1", text)

    text = remove_extra_spacing(text)
    return text


current_dir: str = os.path.dirname(os.path.abspath(__file__))
target_file_path: str = os.path.join(current_dir, "a.txt")

with open(target_file_path, "r", encoding="utf-8") as file:
    text: str = file.read()

clean_text: str = remove_usfm_tags(text)

with open(target_file_path, "w", encoding="utf-8") as file:
    file.write(clean_text)
