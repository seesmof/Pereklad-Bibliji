import re


text=r'\v 2 а насолода його в ГОСПОДНЬОМУ\f + \fr 1:2 \ft Коли слово «ГОСПОДЬ» або «БОГ» пишеться УСІМА ВЕЛИКИМИ ЛІТЕРАМИ, воно є перекладом Божого Власного Імені (Євр. «\+wh יהוה\+wh*», зазвичай вимовляється як Ягве).\f* законі.'

def mark_LORD_s_Words_with_ND(text):
    pattern=r'(ГОСПОД.*?(?=-|\s))'
    print(re.findall(pattern,text))

res=mark_LORD_s_Words_with_ND(text)
print(res)