import os
from rich.console import Console
from rich.traceback import install

from Library import Get_Current_Folder_Path, Load_Bible_Books_Data

install()
console = Console()


Bible_Books_Data = Load_Bible_Books_Data()

All_Books_Chapters_Count = {
    Book_Name: Book_Data["Chapters_Count"]
    for Book_Name, Book_Data in Bible_Books_Data.items()
}
All_Books_Chapters_Count = dict(
    sorted(All_Books_Chapters_Count.items(), key=lambda item: item[1], reverse=True)
)

Old_Testament_Chapters_Count = {
    Book_Name: Book_Data["Chapters_Count"]
    for Book_Name, Book_Data in Bible_Books_Data.items()
    if Book_Data["Testament"] == "Old"
}
Old_Testament_Chapters_Count = dict(
    sorted(Old_Testament_Chapters_Count.items(), key=lambda item: item[1], reverse=True)
)

New_Testament_Chapters_Count = {
    Book_Name: Book_Data["Chapters_Count"]
    for Book_Name, Book_Data in Bible_Books_Data.items()
    if Book_Data["Testament"] == "New"
}
New_Testament_Chapters_Count = dict(
    sorted(New_Testament_Chapters_Count.items(), key=lambda item: item[1], reverse=True)
)

Target_Folder_Name = "Books Translation Order"
Current_Folder_Path = Get_Current_Folder_Path()
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
