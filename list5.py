import tkinter as tk
from tkinter import ttk
import requests

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

        self.get_exchange_rates()
        self.instantiateCurency()
        self.instantiateCurency()
        

    def instantiateCurency(self):
        self.curencyTrack += 1
        Curency_Label = ttk.Label(self.root, text=f"Curency no.{self.curencyTrack}:", font=('Helvetica', 12))
        Curency_Label.grid(row=self.curencyTrack, column=0, columnspan=1000)

    def get_exchange_rates(self):
        try:
            url = "http://api.nbp.pl/api/exchangerates/tables/A?format=json"
            response = requests.get(url)
            data = response.json()
            
            rates = {item['code']: f"{item['mid']}({item['currency']})" for item in data[0]['rates']}
            rates['PLN (Polski Zloty)'] = 1.0
            self.rates = rates
            self.lastDownload = data[0]['effectiveDate']
        except:
            #takesfromStorage
            print("WIP")
if __name__ == "__main__":
    app = CurencyConverter()
    