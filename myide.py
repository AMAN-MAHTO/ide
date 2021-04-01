from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess

ide = Tk()

ide.maxsize()
ide.title('ide')


file_path=''
def set_file_path(path):
    global file_path
    file_path = path

def Open():
    path = askopenfilename(filetype=[('Python','*.py')])
    with open(path,'r') as file:
        editor.delete('1.0',END)
        editor.insert('1.0',file.read())
        set_file_path(path)

def run():
    if file_path=='':
        save_as()
    else:
        command = f'python "{file_path}"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        output ,error = process.communicate()
        code_output.delete('1.0',END)
        code_output.insert('1.0',f'Path: {file_path}\nOutput:\n\n')
        code_output.insert('4.0',output)
        code_output.insert('1.0',error)
    
def save_as():
    if file_path=='':
        path = asksaveasfilename(filetype=[('Python','*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        file.write(editor.get('1.0',END))
        set_file_path(path)
def Exit():
    exit()

editor =Text(ide)
editor.pack(expand=True, fill=BOTH)

code_output = Text(height=10)
code_output.pack(expand=True, fill=BOTH)

navbar = Menu(ide)
file_menu=Menu(navbar,tearoff=0)

file_menu.add_command(label='Run',command=run)
file_menu.add_command(label='Open',command=Open)
file_menu.add_command(label="Save",command=save_as)
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label="Exit",command=Exit)
navbar.add_cascade(label='File',menu=file_menu)

ide.configure(menu=navbar)

ide.mainloop()