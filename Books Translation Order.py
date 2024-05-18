import os
from rich.console import Console
from rich.traceback import install

install()
console = Console()


Bible_Book_Names = {
    "Genesis": {"USFM_Name": "GEN", "Chapters_Count": 50, "Testament": "Old"},
    "Exodus": {"USFM_Name": "EXO", "Chapters_Count": 40, "Testament": "Old"},
    "Leviticus": {"USFM_Name": "LEV", "Chapters_Count": 27, "Testament": "Old"},
    "Numbers": {"USFM_Name": "NUM", "Chapters_Count": 36, "Testament": "Old"},
    "Deuteronomy": {"USFM_Name": "DEU", "Chapters_Count": 34, "Testament": "Old"},
    "Joshua": {"USFM_Name": "JOS", "Chapters_Count": 24, "Testament": "Old"},
    "Judges": {"USFM_Name": "JDG", "Chapters_Count": 21, "Testament": "Old"},
    "Ruth": {"USFM_Name": "RUT", "Chapters_Count": 4, "Testament": "Old"},
    "1 Samuel": {"USFM_Name": "1SA", "Chapters_Count": 31, "Testament": "Old"},
    "2 Samuel": {"USFM_Name": "2SA", "Chapters_Count": 24, "Testament": "Old"},
    "1 Kings": {"USFM_Name": "1KI", "Chapters_Count": 22, "Testament": "Old"},
    "2 Kings": {"USFM_Name": "2KI", "Chapters_Count": 25, "Testament": "Old"},
    "1 Chronicles": {"USFM_Name": "1CH", "Chapters_Count": 29, "Testament": "Old"},
    "2 Chronicles": {"USFM_Name": "2CH", "Chapters_Count": 36, "Testament": "Old"},
    "Ezra": {"USFM_Name": "EZR", "Chapters_Count": 10, "Testament": "Old"},
    "Nehemiah": {"USFM_Name": "NEH", "Chapters_Count": 13, "Testament": "Old"},
    "Esther": {"USFM_Name": "EST", "Chapters_Count": 10, "Testament": "Old"},
    "Job": {"USFM_Name": "JOB", "Chapters_Count": 42, "Testament": "Old"},
    "Psalms": {"USFM_Name": "PSA", "Chapters_Count": 150, "Testament": "Old"},
    "Proverbs": {"USFM_Name": "PRO", "Chapters_Count": 31, "Testament": "Old"},
    "Ecclesiastes": {"USFM_Name": "ECC", "Chapters_Count": 12, "Testament": "Old"},
    "Song of Solomon": {"USFM_Name": "SNG", "Chapters_Count": 8, "Testament": "Old"},
    "Isaiah": {"USFM_Name": "ISA", "Chapters_Count": 66, "Testament": "Old"},
    "Jeremiah": {"USFM_Name": "JER", "Chapters_Count": 52, "Testament": "Old"},
    "Lamentations": {"USFM_Name": "LAM", "Chapters_Count": 5, "Testament": "Old"},
    "Ezekiel": {"USFM_Name": "EZK", "Chapters_Count": 48, "Testament": "Old"},
    "Daniel": {"USFM_Name": "DAN", "Chapters_Count": 12, "Testament": "Old"},
    "Hosea": {"USFM_Name": "HOS", "Chapters_Count": 14, "Testament": "Old"},
    "Joel": {"USFM_Name": "JOL", "Chapters_Count": 3, "Testament": "Old"},
    "Amos": {"USFM_Name": "AMO", "Chapters_Count": 9, "Testament": "Old"},
    "Obadiah": {"USFM_Name": "OBA", "Chapters_Count": 1, "Testament": "Old"},
    "Jonah": {"USFM_Name": "JON", "Chapters_Count": 4, "Testament": "Old"},
    "Micah": {"USFM_Name": "MIC", "Chapters_Count": 7, "Testament": "Old"},
    "Nahum": {"USFM_Name": "NAM", "Chapters_Count": 3, "Testament": "Old"},
    "Habakkuk": {"USFM_Name": "HAB", "Chapters_Count": 3, "Testament": "Old"},
    "Zephaniah": {"USFM_Name": "ZEP", "Chapters_Count": 3, "Testament": "Old"},
    "Haggai": {"USFM_Name": "HAG", "Chapters_Count": 2, "Testament": "Old"},
    "Zechariah": {"USFM_Name": "ZEC", "Chapters_Count": 14, "Testament": "Old"},
    "Malachi": {"USFM_Name": "MAL", "Chapters_Count": 4, "Testament": "Old"},
    "Matthew": {"USFM_Name": "MAT", "Chapters_Count": 28, "Testament": "New"},
    "Mark": {"USFM_Name": "MRK", "Chapters_Count": 16, "Testament": "New"},
    "Luke": {"USFM_Name": "LUK", "Chapters_Count": 24, "Testament": "New"},
    "John": {"USFM_Name": "JHN", "Chapters_Count": 21, "Testament": "New"},
    "Acts": {"USFM_Name": "ACT", "Chapters_Count": 28, "Testament": "New"},
    "Romans": {"USFM_Name": "ROM", "Chapters_Count": 16, "Testament": "New"},
    "1 Corinthians": {"USFM_Name": "1CO", "Chapters_Count": 16, "Testament": "New"},
    "2 Corinthians": {"USFM_Name": "2CO", "Chapters_Count": 13, "Testament": "New"},
    "Galatians": {"USFM_Name": "GAL", "Chapters_Count": 6, "Testament": "New"},
    "Ephesians": {"USFM_Name": "EPH", "Chapters_Count": 6, "Testament": "New"},
    "Philippians": {"USFM_Name": "PHP", "Chapters_Count": 4, "Testament": "New"},
    "Colossians": {"USFM_Name": "COL", "Chapters_Count": 4, "Testament": "New"},
    "1 Thessalonians": {"USFM_Name": "1TH", "Chapters_Count": 5, "Testament": "New"},
    "2 Thessalonians": {"USFM_Name": "2TH", "Chapters_Count": 3, "Testament": "New"},
    "1 Timothy": {"USFM_Name": "1TI", "Chapters_Count": 6, "Testament": "New"},
    "2 Timothy": {"USFM_Name": "2TI", "Chapters_Count": 4, "Testament": "New"},
    "Titus": {"USFM_Name": "TIT", "Chapters_Count": 3, "Testament": "New"},
    "Philemon": {"USFM_Name": "PHM", "Chapters_Count": 1, "Testament": "New"},
    "Hebrews": {"USFM_Name": "HEB", "Chapters_Count": 13, "Testament": "New"},
    "James": {"USFM_Name": "JAS", "Chapters_Count": 5, "Testament": "New"},
    "1 Peter": {"USFM_Name": "1PE", "Chapters_Count": 5, "Testament": "New"},
    "2 Peter": {"USFM_Name": "2PE", "Chapters_Count": 3, "Testament": "New"},
    "1 John": {"USFM_Name": "1JN", "Chapters_Count": 5, "Testament": "New"},
    "2 John": {"USFM_Name": "2JN", "Chapters_Count": 1, "Testament": "New"},
    "3 John": {"USFM_Name": "3JN", "Chapters_Count": 1, "Testament": "New"},
    "Jude": {"USFM_Name": "JUD", "Chapters_Count": 1, "Testament": "New"},
    "Revelation": {"USFM_Name": "REV", "Chapters_Count": 22, "Testament": "New"},
}

All_Books_Chapters_Count = {
    Book_Name: Book_Data["Chapters_Count"]
    for Book_Name, Book_Data in Bible_Book_Names.items()
}
All_Books_Chapters_Count = dict(
    sorted(All_Books_Chapters_Count.items(), key=lambda item: item[1], reverse=True)
)

Old_Testament_Chapters_Count = {
    Book_Name: Book_Data["Chapters_Count"]
    for Book_Name, Book_Data in Bible_Book_Names.items()
    if Book_Data["Testament"] == "Old"
}
Old_Testament_Chapters_Count = dict(
    sorted(Old_Testament_Chapters_Count.items(), key=lambda item: item[1], reverse=True)
)

New_Testament_Chapters_Count = {
    Book_Name: Book_Data["Chapters_Count"]
    for Book_Name, Book_Data in Bible_Book_Names.items()
    if Book_Data["Testament"] == "New"
}
New_Testament_Chapters_Count = dict(
    sorted(New_Testament_Chapters_Count.items(), key=lambda item: item[1], reverse=True)
)

Target_Folder_Name = "Books Translation Order"
Current_Folder_Path = os.path.dirname(os.path.abspath(__file__))
Target_Folder_Path = os.path.join(Current_Folder_Path, Target_Folder_Name)

if not os.path.exists(Target_Folder_Path):
    os.mkdir(Target_Folder_Path)

for Testament_Name in ["Old", "New"]:
    Target_File_Path = os.path.join(
        Target_Folder_Path, f"{Testament_Name}_Testament.md"
    )

    with open(Target_File_Path, "w", encoding="utf-8") as Target_File:
        Chapters_Count = (
            Old_Testament_Chapters_Count
            if Testament_Name == "Old"
            else New_Testament_Chapters_Count
        )

        for Book_Name in Chapters_Count:
            Target_File.write(f"- [ ] {Book_Name}\n")
