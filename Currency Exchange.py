import tkinter as tk
import requests

supported_currencies = [
    "USD", "CAD", "GBP", "EUR", "EGP", "BRL", "COP", "DKK",
    "HKD", "INR", "JPY", "NZD", "LTC", "BCH", "XRP", "DAI",
    "DOGE", "TRX", "BTC", "BNB", "SOL", "SHIB", "ETH"
]


class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('300x200')

        self.from_var = tk.StringVar(self.root)
        self.from_var.set('USD')
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *supported_currencies)
        self.from_menu.pack(pady=5)

        self.to_var = tk.StringVar(self.root)
        self.to_var.set('EUR')
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *supported_currencies)
        self.to_menu.pack(pady=5)

        self.amount_label = tk.Label(self.root, text='Amount:')
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert_currency)
        self.convert_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)

        self.root.mainloop()

    def convert_currency(self):
        from_currency = self.from_var.get()
        to_currency = self.to_var.get()

        try:
            amount = float(self.amount_entry.get())
            url = f"https://api.coingate.com/api/v2/rates/merchant/{from_currency}/{to_currency}"
            headers = {"accept": "text/plain"}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                conversion_rate = float(response.text)
                converted_amount = amount * conversion_rate
                self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                self.result_label.config(text="Error: Unable to fetch data.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
        except Exception as e:
            self.result_label.config(text=f"An error occurred: {str(e)}")


if __name__ == "__main__":
    CurrencyConverter()