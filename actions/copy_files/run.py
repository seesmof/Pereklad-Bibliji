import os
from shutil import copy2 as copy_file


current_dir: str = os.path.dirname(os.path.abspath(__file__))
Bible_Books_target_dir: str = os.path.join(
    current_dir, "..", "..", "Ukrainian Standard Bible"
)
Bible_project_dir: str = os.path.join("C:\\My Paratext 9 Projects\\USB")

for file in os.listdir(Bible_Books_target_dir):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == ".usfm":
        copy_file(
            os.path.join(Bible_Books_target_dir, file),
            os.path.join(Bible_project_dir, file_name + ".SFM"),
        )
