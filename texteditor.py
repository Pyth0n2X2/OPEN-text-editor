import os
from tkinter import *
from tkinter import colorchooser, font
from tkinter import filedialog as fd
from tkinter.messagebox import *
from tkinter.filedialog import *
#Commands
def change_color():
    color = colorchooser.askcolor(title="Choose")
    text_area.config(fg=color[1])
def bold():
    text_area.config(font=(font_name.get(),font_size.get(), "bold"))
def italic():
    text_area.config(font=(font_name.get(), font_size.get(), "italic"))
def reset():
    text_area.config(font=(font_name.get(), font_size.get()))
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def open_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
 
    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()

def save_file():
    file = fd.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("ERROR: Failed to save file")

        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("OPEN Text editor", "OPEN Text editor v0.0.2 License: MIT License")

def quit():
    window.destroy()

    

window = Tk()
window.title("OPEN Text editor")

file = None

#Window geometry
window_width = 1920
window_height = 1080
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

#Font and text area 
font_name = StringVar(window)
font_name.set("Open Sans")

font_size = StringVar(window)
font_size.set("20")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=1, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=1, column=2)

#Creating the menus and bars
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
color_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Home", menu=color_menu)
color_menu.add_command(label="Color", command=change_color)
color_menu.add_command(label="Bold", command=bold)
color_menu.add_command(label="Italic", command=italic)
color_menu.add_command(label="Reset", command=reset)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
