# Widgets: Labels(), Button(), Entry(), LabelFrame(), Radiobutton(), Scale(), Checkbutton(), OptionMenu()
# Functions: .pack(), .grid(row, column, columnspan), .get(), .insert(0, default text), .delete(0, END)

# text=, width=, state=, padx= and pady=, command=, fg="color",
# bg="color", borderwidth=, image=, relief=, sticky=W+E (stretch NSEW), anchor= (direction of text)

# Can paste with pack() and grid()
# Aesthetics: Icon, Quit Button (command=root.quit), root.geometry("starting size")

# Image Template:
# myImg = ImageTk.PhotoImage(Image.open(r'path'))
# myLabel = Label(image=myImg)
# myLabel.pack()

# Radio Button Template:
# r = IntVar()  # or StringVar()
# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()

# Message Box Templates:
# (showinfo, showwarning, showerror, askquestion, askokcancel, askyesno)
# response = messagebox.showinfo("title", "prompt")
# we do things with response variable. response == 1 or 0

# New Windows use Toplevel(), Tk() is the godfather.
# When outputting widgets to new window set to global.
# When closing secondary windows use top.destroy instead of top.quit.

# File Template:
# root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Karimi\Desktop", title="boosted", filetypes=(("png files", "*.png"),("all files", "*.*"))).pack()
# ^ this returns a file path combine with os and other file modules and its OP.

# Slider Template:
# vertical = Scale(root, from_=0, to=1200, orient=HORIZONTAL)

# Checkboxes Template:
# var = IntVar()
# c = Checkbutton(root, text="Check Mate", variable=var, onvalue="On", offvalue="Off")
# c.deselect()

# Dropdown Template:
# clicked = StringVar()
# clicked.set("Pick a day!")
# d = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday") If we use lists use *LISTNAME.

"""

Starting Template:

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import sqlite3

root = Tk()
root.title("")
root.iconbitmap(r'')

root.mainloop()


"""