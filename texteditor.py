import os
import webbrowser
import pandas as pd
import os
from gtts import gTTS
from tkinter import *
from tkinter import colorchooser, font
from tkinter import filedialog as fd
from tkinter import simpledialog
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.messagebox
#Commandsd
def color():
    color=colorchooser.askcolor()
    text_area.config(foreground=color[1])

def darkmode():
    text_area.config(background='#202839', foreground="white")
    window.config(background="gray")
def lightmode():
    text_area.config(background='white', foreground='black')
    window.config(background="gray")
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
        ('Python file', '*.py'),
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
    file = fd.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension=".OPEN",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Python file", ".py")])

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
def spell_suggest():
    sentence = simpledialog.askstring(title="Spelling suggestion", prompt="Enter word: ")
    webbrowser.open("http://suggest.aspell.net/index.php?word=" +
                    sentence+ "&spelling=american&dict=normal&sugmode=slow")
def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def underline():
    text_area.config(font=(font_name.get(), font_size.get(), "underline"))


def about():
    showinfo("OPEN Text editor", "OPEN Text editor v0.0.3 License: MIT License")

def quit():
    window.destroy()
def bullet():
    howmany = simpledialog.askstring(title="How many bullets?", prompt="Enter how many bullets to add: ")
    howmany = int(howmany)
    i = 0
    while(i < howmany):
        text_area.insert("end", "• \n")
        i+=1
def replace():
    to_replace = simpledialog.askstring(title="Replace", prompt="Enter text to be replaced") 
    with_what_to_replace = simpledialog.askstring(title="Replace", prompt="Enter what to replace it with")
    # get content of text box
    text = text_area.get("1.0", "end-1c")
# clear text box
    text_area.delete("1.0", "end")
# insert the replace result back to text box
    text_area.insert("end", text.replace(to_replace, with_what_to_replace))
def update():
    webbrowser.open("https://github.com/Pyth0n2X2/OPEN-text-editor")

def create_sticky():
       #Create a Toplevel window
   top= Toplevel(window)
   top.title("Sticky note")
   top.geometry("480x240")

   #Create an Entry Widget in the Toplevel window
   entry= Text(top, height=480, width=240)

   entry.pack()


def ascii_table():
    tabletop = Toplevel(window)
    tabletop.title("Commercial/trade symbols table")
    tabletop.geometry("400x200")
    def pound():
        text_area.insert("1.0", "£")
    def euro():
        text_area.insert("1.0", "€")
    def yen():
        text_area.insert("1.0", "¥")
    def trademark():
        text_area.insert("1.0", "®")


    poundsymbol = Button(tabletop, text="£", width=100, command=pound)
    eurosymbol = Button(tabletop, text="€", width=100, command=euro)
    yensymbol = Button(tabletop, text="¥", width=100, command=yen)
    trademarksymbol = Button(tabletop, text="®", width=100, command=trademark)
    poundsymbol.pack()
    eurosymbol.pack()
    yensymbol.pack()
    trademarksymbol.pack()

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
edit_menu.add_separator()
edit_menu.add_command(label="Replace", command=replace)
edit_menu.add_command(label="Spell suggest", command=spell_suggest)
home_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="Bold", command=bold)
home_menu.add_command(label="Italic", command=italic)
home_menu.add_command(label="Underline", command = underline)
home_menu.add_command(label="Bullet", command=bullet)
home_menu.add_command(label="ASCII Table", command=ascii_table)
home_menu.add_command(label="Create new sticky notes", command=create_sticky)
home_menu.add_separator()
home_menu.add_command(label="Reset", command=reset)
options_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Dark mode", command=darkmode)
options_menu.add_command(label="Light mode", command=lightmode)
options_menu.add_separator()    
options_menu.add_command(label="Text color", command=color)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=help_menu)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Main", command=update)

window.mainloop()
