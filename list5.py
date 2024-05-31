import tkinter as tk
from tkinter import ttk
from datetime import date
import requests
import os
import json
import logging


class CurencyConverter:
    def __init__(self):

        self.root = tk.Tk()
        self.setup()
        #Main loop:
        self.root.mainloop()

### GRAPHICAL INTERFACE ###
    def setup(self):
        """
        Setups the window in tk
        """
        #Window Setup
        self.root.title("Curency Converter")
        self.root.geometry("500x450")
        exit_button = tk.Button( text="Exit", command=self.root.quit)
        exit_button.grid(row = 0, column = 300)

        #Curently used database info
        self.storage_path='exchange_rates.json'
        self.get_exchange_rates()
        info_var = "NULL"
        if(str(date.today()) == self.lastDownload):
            info_var = 'Database: up-to-date'
        else:
            info_var = f"Database: {self.lastDownload}"
        info_Label = ttk.Label(self.root, text=info_var, font=('Helvetica', 12))
        info_Label.grid(row=0, column=1)

        #Displayed Currencies and buttons to add more
        add_currency_button = ttk.Button(self.root, text="Add Currency", command=self.instantiateCurrency)
        add_currency_button.grid(row=0, column=0)

        self.currencyTrack = 0
        self.currencyBuffor = []
        self.instantiateCurrency()
        self.instantiateCurrency()
        
    def instantiateCurrency(self):
        """
        Instantate additional currency to compare
        """
        currencyTrack = self.currencyTrack
        self.currencyTrack += 1

        Currency_Label = ttk.Label(self.root, text=f"Currency no. {currencyTrack + 1}:", font=('Helvetica', 12))
        Currency_Label.grid(row=currencyTrack+1, column=0)
        Currency_Choice = ttk.Combobox(self.root, values=list(self.rates.keys()))
        Currency_Choice.grid(row=currencyTrack+1, column=1)
        amount = tk.Entry(self.root)
        amount.grid(row=currencyTrack+1, column=2)

        #binding Caclulating to changing Values/Curencies
        amount.bind("<KeyRelease>",                  lambda event, index=currencyTrack, curency=Currency_Choice, entry=amount: self.convert_from(index, curency, entry))
        Currency_Choice.bind("<<ComboboxSelected>>", lambda event, index=currencyTrack, curency=Currency_Choice, entry=amount: self.convert_from(index, curency, entry))
       
        # Default
        Currency_Choice.current(list(self.rates.keys()).index("PLN (Polski Zloty)"))
        amount.insert(0, "1.0")

        self.currencyBuffor.append([Currency_Choice.get(), amount])

    def convert_from(self, id, currency, amount):
        """
        Converts every value based on the value interacted with
        """
        base_value = float(amount.get())
        new_currency = str(currency.get())

        base_value *= float(self.rates[new_currency])
        # Update all currencies on screen
        for i, (cur_choice, cur_entry) in enumerate(self.currencyBuffor):
            if i != id:
                result = base_value / float(self.rates[cur_choice])  
                cur_entry.delete(0, tk.END)
                cur_entry.insert(0, f"{result:0.10}")
        self.currencyBuffor[id] = (currency.get(), amount)

    def get_exchange_rates(self):
        """
        Downloads rates from NBP
        """
        try:
            url = "http://api.nbp.pl/api/exchangerates/tables/A?format=json"
            response = requests.get(url)
            data = response.json()
            
            rates = {f"{item['code']} ({item['currency']})": item['mid'] for item in data[0]['rates']}
            rates['PLN (Polski Zloty)'] = 1.0
            self.rates = rates
            self.lastDownload = data[0]['effectiveDate']
            
            self.save_rates()

        except:
            self.load_rates()


    def save_rates(self):
        """
        Saves the current rates to a file.
        """
        try:
            with open(self.storage_path, 'w') as file:
                json.dump({'rates': self.rates, 'lastDownload': self.lastDownload}, file)
        except IOError as e:
            logging.error("Error saving exchange rates to storage: %s", e)

    def load_rates(self):
        """
        Loads the rates from last download.
        """
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as file:
                    data = json.load(file)
                    self.rates = data['rates']
                    self.lastDownload = data['lastDownload']
            except IOError as e:
                logging.error("Error loading exchange rates from storage: %s", e)
        else:
            logging.warning("No storage file found. Unable to load exchange rates.")


if __name__ == "__main__":
    app = CurencyConverter()
    