

file_name = "file.text"

def write_files():
    with open(file_name,'w',encoding='utf-8') as file:
        file.writelines("name \n")

def add_text(text):
    with open(file_name,'a',encoding='utf-8') as file:
        file.write(text + '\n')

def read_text():
    with open(file_name,'r',encoding='utf-8') as file:
        return file.readlines()