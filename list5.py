import tkinter as tk
from tkinter import ttk
import requests
from datetime import date

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
        info_var = "NULL"
        if(str(date.today()) == self.lastDownload):
            info_var = 'Database: up-to-date'
        else:
            info_var = f"Database: {self.lastDownload}"
        info_Label = ttk.Label(self.root, text=info_var, font=('Helvetica', 12))
        info_Label.grid(row=0, column=1, columnspan=1000)

        add_currency_button = ttk.Button(self.root, text="Add Currency", command=self.instantiateCurrency)
        add_currency_button.grid(row=0, column=0, pady=10)

        self.onScreenCurency = []
        self.instantiateCurrency()
        self.instantiateCurrency()
        

    def instantiateCurrency(self):
        self.curencyTrack += 1
        Currency_Label = ttk.Label(self.root, text=f"Curency no. {self.curencyTrack}:", font=('Helvetica', 12))
        Currency_Label.grid(row = self.curencyTrack, column = 0)
        Currency_Choice = ttk.Combobox(self.root, values = list(self.rates.keys()))
        Currency_Choice.grid(row = self.curencyTrack, column = 1)
        amount = tk.Entry(self.root)
        amount.grid(row = self.curencyTrack, column = 2)
        
        #Default
        Currency_Choice.current(list(self.rates.keys()).index("PLN (Polski Zloty)"))
        amount.insert(0, "1")
        
        self.onScreenCurency.append({self.curencyTrack,"PLN (Polski Zloty)",1})
        print(self.onScreenCurency)

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
    