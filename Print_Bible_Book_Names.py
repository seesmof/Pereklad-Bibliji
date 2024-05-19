import os
from rich.console import Console
from rich.traceback import install

from Library import Get_Current_Folder_Path, Load_Bible_Books_Data

install()
console = Console()

Bible_Books_Data = Load_Bible_Books_Data()
Current_Folder_Path = Get_Current_Folder_Path()
Target_File_Path = os.path.join(Current_Folder_Path, "Book_Names.md")

with open(Target_File_Path, "w", encoding="utf-8") as Target_File:
    for Book_Name in Bible_Books_Data:
        Target_File.write(f"{Book_Name}: \n")
