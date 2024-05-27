import tkinter as tk
from tkinter import ttk



class CurencyConverter:
    def __init__(self):

        self.root = tk.Tk()
        self.setup()
        #Main loop:
        self.root.mainloop()


### GRAPHICAL INTERFACE ###
    def setup(self):
        self.root.title("Curency Converter")
        self.root.geometry("500x450")
        self.curencyTrack = 0

        self.instantiateCurency()
        self.instantiateCurency()
        

    def instantiateCurency(self):
        self.curencyTrack += 1
        Curency_Label = ttk.Label(self.root, text=f"Curency no.{self.curencyTrack}:", font=('Helvetica', 12))
        Curency_Label.grid(row=self.curencyTrack, column=0, columnspan=1000)
if __name__ == "__main__":
    app = CurencyConverter()
    