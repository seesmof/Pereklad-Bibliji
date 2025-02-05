import time
import os
import re

root_folder_path=os.path.dirname(os.path.abspath(__file__))
revision_folder_path=os.path.join(root_folder_path,'Revision')
target_file_path=os.path.join(revision_folder_path,'58PHM.USFM')

def mark_text(
    given_text:str,
):
    PUNCTUATION=r"!”#’$%&'()*+,-./:;<?=@>[\]^_`{|}~"

    def make_dashes_typographical(text):
        text=re.sub(r'(\s)-',r'\1—',text)
        text=re.sub(r'-(\s)',r'—\1',text)
        return text

    def render_accent_marks(text):
        ACCENT_MARK='\u0301'
        ACCENT_TRIGGER='#'
        return re.sub(rf'([аеєиіїоуюяАЕЄИІЇОУЮЯ])[{ACCENT_TRIGGER}№]([\w{PUNCTUATION}])',rf'\1{ACCENT_MARK}\2',text)

    def make_apostrophes_typographical(text):
        return re.sub(rf'(\w)\'([\w{PUNCTUATION}])',r'\1ʼ\2',text)

    def make_quotes_typographical(text):
        '''
        SINGLE_OPENING='‹'
        SINGLE_CLOSING='›'
        '''
        SINGLE_OPENING='“'
        SINGLE_CLOSING='”'
        DOUBLE_OPENING='«'
        DOUBLE_CLOSING='»'

        '''
        SINGLE_OPENING='‚'
        SINGLE_CLOSING='‛'
        DOUBLE_OPENING='„'
        DOUBLE_CLOSING='‟'
        '''

        '''
        SINGLE_OPENING='‘'
        SINGLE_CLOSING='’'
        DOUBLE_OPENING='“'
        DOUBLE_CLOSING='”'
        '''

        def replace_at_index(text,index=0,replacement=''):
            return f'{text[:index]}{replacement}{text[index+1:]}'

        single_last_closing=False
        double_last_closing=False
        for i,symbol in enumerate(text):
            if symbol==DOUBLE_OPENING: double_last_closing=True
            elif symbol==SINGLE_OPENING: single_last_closing=True
            if symbol==DOUBLE_CLOSING: double_last_closing=False
            elif symbol==SINGLE_CLOSING: single_last_closing=False

            elif symbol=="'":
                if not single_last_closing: 
                    text=replace_at_index(text,i,SINGLE_OPENING)
                    single_last_closing=True
                else: 
                    text=replace_at_index(text,i,SINGLE_CLOSING)
                    single_last_closing=False
            elif symbol=='"':
                if not double_last_closing: 
                    text=replace_at_index(text,i,DOUBLE_OPENING)
                    double_last_closing=True
                else: 
                    text=replace_at_index(text,i,DOUBLE_CLOSING)
                    double_last_closing=False
        return text

    def add_strong_tags(text: str):
        text=text.split(' ')
        opens_count=0
        closes_count=0
        for i,word in enumerate(text):
            if '\\w*' in word: closes_count+=1
            elif '\\w' in word: opens_count+=1

            if not '|strong=' in word: continue
            try:
                if opens_count!=closes_count and text[i-1]!='\\w':
                    text[i]='\\w '+word
                    closes_count+=1
            except: pass

            if 1<=word.count('"')<2:
                text[i]=re.sub(r'(\"[GH]\d*)',r'\1"\\w*',text[i])

        text=' '.join(text)
        return text

    def remove_trailing_whitespaces(text: str):
        return '\n'.join([l.strip() for l in text.split('\n')])

    dashes_fixed=make_dashes_typographical(given_text)
    apostrophes_fixed=make_apostrophes_typographical(dashes_fixed)
    # quotes_fixed=make_quotes_typographical(apostrophes_fixed)
    accents_fixed=render_accent_marks(apostrophes_fixed)
    strongs_handled=add_strong_tags(accents_fixed)
    whitespaces_removed=remove_trailing_whitespaces(strongs_handled)
    return whitespaces_removed

with open(target_file_path,encoding='utf-8',mode='r') as f:
    read_text=f.read()
with open(target_file_path,encoding='utf-8',mode='w') as f:
    f.write(mark_text(read_text))
print('Text marked')

while 1:
    with open(target_file_path,encoding='utf-8',mode='r') as f:
        new_read_text=f.read()
    if new_read_text!=read_text:
        marked_text=mark_text(new_read_text)
        with open(target_file_path,encoding='utf-8',mode='w') as f:
            f.write(marked_text)
        print('\nText marked')
        read_text=marked_text
    else: read_text=new_read_text
    time.sleep(1)