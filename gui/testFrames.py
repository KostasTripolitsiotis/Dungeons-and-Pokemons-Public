from tkinter import *

# Create object
root = Tk()
x= False
# Adjust size
root.geometry( "250x250" )
root.resizable(True, True)

# Change the label text
def show():
    root.attributes('-fullscreen', True)
    label.config( text = clicked.get() )

def exitfs():
    root.attributes('-fullscreen', False)

# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Monday" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()
button2 = Button(root, text = 'exit fullscreen', command = exitfs).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()