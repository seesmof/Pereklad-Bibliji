import os
from rich.console import Console
from rich.traceback import install

from Library import Get_Current_Folder_Path, Load_Bible_Books_Data

install()
console = Console()


Bible_Books_Data = Load_Bible_Books_Data()
Old_Testament_Books_Data = {
    Book_Name: Book_Data
    for Book_Name, Book_Data in Bible_Books_Data.items()
    if Book_Data["Testament"] == "Old"
}
New_Testament_Books_Data = {
    Book_Name: Book_Data
    for Book_Name, Book_Data in Bible_Books_Data.items()
    if Book_Data["Testament"] == "New"
}
console.print(New_Testament_Books_Data)

Current_Folder_Path = Get_Current_Folder_Path()
Bible_Root_Folder_Path = os.path.join(Current_Folder_Path, "Bible")

"""
for Testament_Name in ["Old", "New"]:
    Target_Folder_Path = os.path.join(
        Bible_Root_Folder_Path, f"{Testament_Name}_Testament"
    )
    if not os.path.exists(Target_Folder_Path):
        os.mkdir(Target_Folder_Path)

    Books_Data = (
        Old_Testament_Books_Data
        if Testament_Name == "Old"
        else New_Testament_Books_Data
    )
"""
