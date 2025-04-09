import tkinter as tk
from tkinter import messagebox
import menuFrame as mf
import spawnPokemonFrame as spf
import showPokemonFrame as shf
import managePokemonFrame as mpf
from backup import Backup

bg_color = "#3d6466"

class App(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        x= (self.winfo_screenwidth() // 2) - 400
        y=int(self.winfo_screenheight() * 0.2)
        self.geometry(width+ 'x'+ height+'+' + str(x) + '+' +  str(y))
        self.title('Dungeons and Pokemons')

        # creating a container
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        #creating frames
        self.frames = {}
        for F in (mf.menuFrame, shf.ShowFrame, spf.SpawnFrame, mpf.ManageFrame):
            frame = F(self.container, self, bg_color, width, height)
            self.frames[F] = frame

        self.reloadWilds = False

        self.menubar = self.init_menu()
        
        self.load_frame(mf.menuFrame)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mainloop()

    def init_menu(self):
        menu = tk.Menu(self)
        filemenu = tk.Menu(menu, tearoff=0)
        filemenu.add_command(label='Close', command=self.on_closing)
        filemenu.add_command(label='Menu', command=lambda:self.load_frame(mf.menuFrame))
        filemenu.add_command(label="See Pokemon", command=lambda:self.load_frame(shf.ShowFrame))
        filemenu.add_command(label="Spawn Pokemon", command=lambda:self.load_frame(spf.SpawnFrame))
        filemenu.add_command(label="Manage Pokemon", command=lambda:self.load_frame(mpf.ManageFrame))

        menu.add_cascade(menu=filemenu, label="File")
        self.config(menu=menu)

        return menu

    def changeReloadWilds(self):
        if self.reloadWilds == True:
            self.reloadWilds = False
        else:
            self.reloadWilds = True

    def load_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Did you have a good time? :)'):
            self.destroy()

def main():
    width = str(820)
    height = str(305)

    App(width, height)

    #Backup.create()
    
if __name__ == "__main__":
    main()