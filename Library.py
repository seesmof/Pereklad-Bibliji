import json
import os


def Get_Current_Folder_Path() -> str:
    Current_Folder_Path = os.path.dirname(os.path.abspath(__file__))
    return Current_Folder_Path


def Load_Bible_Books_Data() -> dict:
    Current_Folder_Path = Get_Current_Folder_Path()
    Bible_Books_Data_File_Path = os.path.join(
        Current_Folder_Path, "Bible_Books_Data.json"
    )

    try:
        with open(
            Bible_Books_Data_File_Path, "r", encoding="utf-8"
        ) as Bible_Books_Data_File:
            Bible_Books_Data = json.load(Bible_Books_Data_File)
    except:
        Bible_Books_Data = {}

    return Bible_Books_Data
