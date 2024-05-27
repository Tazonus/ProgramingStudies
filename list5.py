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

        #Label displaying Origin Curency
        firstCurency_Label = ttk.Label(self.root, text="First Curency:", font=('Helvetica', 12))
        firstCurency_Label.grid(row=0, column=0, columnspan=1000)

        #Label displaying category
        secondCurency_Label = ttk.Label(self.root, text="Second Curency:", font=('Helvetica', 12))
        secondCurency_Label.grid(row=1, column=90, columnspan=1000)


if __name__ == "__main__":
    app = CurencyConverter()
    