import string
import time
import os
import re

root_folder_path=os.path.dirname(os.path.abspath(__file__))
web_folder_path=os.path.join(root_folder_path,'WEBU_Strongs')

for file_name in os.listdir(web_folder_path):
    file_path=os.path.join(web_folder_path,file_name)
    with open(file_path,encoding='utf-8',mode='r') as f:
        lines=f.readlines()
    lines=[l.strip() for l in lines]
    with open(file_path,encoding='utf-8',mode='w') as f:
        f.write('\n'.join(lines))