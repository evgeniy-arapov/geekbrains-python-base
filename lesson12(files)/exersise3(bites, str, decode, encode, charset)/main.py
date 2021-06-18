with open('file.txt', 'w', encoding='utf-8') as f:
    str = 'Привет мир!3'
    f.write(str)

with open('file.txt', 'rb') as f:
    strb = f.read()
    print(strb)
    str = strb.decode('utf-8')
    print(str)
