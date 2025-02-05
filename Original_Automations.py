import glob
import shutil
import time 
import os
import re

root_folder_path=os.path.dirname(os.path.abspath(__file__))
revision_folder_path=os.path.join(root_folder_path,'Revision')
revision_files = glob.glob(revision_folder_path + "\\*.USFM")
paratext_projects_folder_path=os.path.join(r'C:\My Paratext 9 Projects')

def copy_files_to_paratext_project(
    project_abbreviation: str = 'UFB',
    local_files_folder_path: str = revision_folder_path,
    remove_comenting_rem_tags: bool = True,
):
    paratext_project_folder_path=os.path.join(paratext_projects_folder_path,project_abbreviation)
    for file_name in os.listdir(local_files_folder_path):
        if 'GLO' in file_name or 'FRT' in file_name: continue

        paratext_file_path=os.path.join(paratext_project_folder_path,file_name)
        local_file_path=os.path.join(local_files_folder_path,file_name)
        shutil.copy2(local_file_path,paratext_file_path)

        if remove_comenting_rem_tags:
            with open(paratext_file_path,encoding='utf-8',mode='r') as f:
                lines=f.readlines()
            lines=[l for l in lines if not l.startswith(r'\rem ')]
            with open(paratext_file_path,encoding='utf-8',mode='w') as f:
                f.write('\n'.join([l.strip() for l in lines]))

def form_markdown_output(
    source_folder_path:str = revision_folder_path,
    local_output_file_path:str = os.path.join(root_folder_path,'Formatted_Output.md'),
    vault_output_file_path:str = None,
):
    def remove_footnotes_with_contents(verse: str):
        footnote_pattern=r'\\(\+*)f(.*?)\\(\+*)f\*'
        return re.sub(footnote_pattern,'',verse)

    def format_text_line(line):
        QT_tags_handled=re.sub(r'\\(\+?)qt\s',f'<span style="font-variant: small-caps">',line)
        ND_tags_handled=re.sub(r'\\(\+?)nd\s',f'<span style="font-variant: small-caps; font-weight:bold">',QT_tags_handled)
        WJ_tags_handled=re.sub(r'\\(\+?)wj\s',f'<span style="color: {WJ_COLOR}">',ND_tags_handled)
        add_opening_tags=re.sub(r'\\(\+?)add\s','<em>',WJ_tags_handled)
        add_closing_tags=add_opening_tags.replace('\\add*','</em>').replace('\\+add*','</em>')
        footnotes_removed=remove_footnotes_with_contents(add_closing_tags)
        other_tags_closed=re.sub(r'\\(\+?)\w+\*','</span>',footnotes_removed)
        return other_tags_closed

    WJ_COLOR='#7e1717'
    output_lines=[]

    for file_name in os.listdir(source_folder_path):
        file_path=os.path.join(source_folder_path,file_name)
        with open(file_path,encoding='utf-8',mode='r') as f:
            lines=f.readlines()
        
        Book_name=file_name[2:].split('.')[0]
        output_lines.append(f'# {Book_name}')
        last_verse_number=1
        
        for line in lines:
            if r'\c ' in line:
                chapter_number=line[3:].strip()
                res=f'### {Book_name} {chapter_number}'
                output_lines.append(res)
            elif r'\p' in line or '\\b' in line:
                line=line[3:].strip()
                res=f'\n{line}' if line else ''
                output_lines.append(res)
            elif r'\v ' in line:
                line=line[3:].strip()
                last_verse_number,contents=line.split(maxsplit=1)
                formatted_line=format_text_line(contents)
                res=f'<sup>{last_verse_number}</sup> {formatted_line}'
                output_lines.append(res)
            elif '\\q' in line:
                line=line[3:].strip()
                if not line: continue
                formatted_line=format_text_line(line)
                res=f'   {formatted_line}'
                output_lines.append(res)

    try:
        if local_output_file_path:
            with open(local_output_file_path,encoding='utf-8',mode='w') as f:
                f.write('\n'.join(output_lines))
        if 'Notatnyk' not in vault_output_file_path:
            vault_output_file_path=os.path.join(r'E:\Notatnyk',vault_output_file_path)
        with open(vault_output_file_path,encoding='utf-8',mode='w') as f:
            f.write('\n'.join(output_lines))
    except: pass

def perform_automations():
    try:
        print("Markdown")
        form_markdown_output()
    except: print('NO Markdown')
    print('Paratext')
    copy_files_to_paratext_project()

def monitor_files_for_changes():
    latest_file = max(revision_files, key=os.path.getmtime)
    last_modification_time = os.path.getmtime(latest_file)
    perform_automations()
    while 1:
        latest_file = max(revision_files, key=os.path.getmtime)
        current_modification_time = os.path.getmtime(latest_file)
        if last_modification_time != current_modification_time:
            perform_automations()
            last_modification_time = current_modification_time
        time.sleep(1)

if __name__ == "__main__":
    monitor_files_for_changes()