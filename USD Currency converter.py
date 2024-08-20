import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()  # Create the main window application
root.geometry("600x270")
root.title("Currency Converter")
root.iconbitmap("E:\\python projects\\New folder\\icon.ico")
root.maxsize(600, 270)
root.minsize(600, 200)

# Load image and adjust size
image = Image.open("E:\\python projects\\New folder\\currency.png")
zoom = 0.5
pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))

# Add image to the GUI
panel = Label(root, image=img)
panel.place(x=190, y=35)

def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    url = "http://api.currencylayer.com/live?access_key=YOUR_ACCESS_KEY&format=1"

    if not amount:
        messagebox.showerror("Currency Converter", "Please fill the amount")
    elif not to_currency:
        messagebox.showerror("Currency Converter", "Please choose the currency")
    else:
        try:
            data = requests.get(url).json()
            if "quotes" in data:
                currency = from_currency.strip() + to_currency.strip()
                amount = int(amount)
                if currency in data["quotes"]:
                    cc = data["quotes"][currency]
                    cur_conv = cc * amount
                    E2.insert(0, cur_conv)
                    text.insert("end", f"{amount} United States Dollar equals {cur_conv} {to_currency} \n\nLast update --- \t {datetime.now()}")
                else:
                    messagebox.showerror("Currency Converter", "Currency not available in the response.")
            else:
                messagebox.showerror("Currency Converter", "Invalid API response. Check API key or request format.")
        except Exception as e:
            messagebox.showerror("Currency Converter", f"An error occurred: {e}")

def clear():
    E1.delete(0, "end")
    E2.delete(0, "end")
    text.delete(1.0, "end")

# Labels and inputs for amount and currency selection
l1 = Label(root, text="USD Currency Using Python", font=("verdana", 10, "bold"))
l1.place(x=150, y=15)

amt = Label(root, text="Amount", font=("roboto", 10, "bold"))
amt.place(x=20, y=15)

E1 = Entry(root, width=20, borderwidth=1, font=("roboto", 10, "bold"))
E1.place(x=20, y=40)

c1 = tk.StringVar()
c2 = tk.StringVar()

currencychoose1 = ttk.Combobox(root, width=20, textvariable=c1, state="readonly", font=("verdana", 10, "bold"))
currencychoose1["values"] = ("USD",)
currencychoose1.place(x=300, y=40)
currencychoose1.current(0)

E2 = Entry(root, width=20, borderwidth=1, font=("roboto", 10, "bold"))
E2.place(x=20, y=80)

currencychoose2 = ttk.Combobox(root, width=20, textvariable=c2, state="readonly", font=("verdana", 10, "bold"))
currencychoose2["values"] = (
    "ALL", "AFN", "ARS", "AWG", "AUD", "AZN", "BSD", "BBD", "BYN", "BZD", "BMD", "BOB", "BAM", "BWP", "BGN", "BND", 
    "KHR", "CAD", "KYD", "CLP", "CNY", "COP", "CRC", "HRK", "CUP", "CZK", "DKK", "DOP", "XCD", "EGP", "SVC", "EUR", 
    "FKP", "FJD", "GHS", "GIP", "GTQ", "GGP", "GYD", "HNL", "HKD", "HUF", "ISK", "INR", "IDR", "IRR", "IMP", "ILS", 
    "JMD", "JPY", "KZT", "KPW", "KRW", "KGS", "LAK", "MKD", "MUR", "NAD", "ANG", "NZD", "NOK", "PKR", "PAB", "OMR", 
    "PEN"
)
currencychoose2.place(x=300, y=80)
currencychoose2.current(0)

# Text box to display conversion result
text = Text(root, height=7, width=52, font=("verdana", 10, "bold"))
text.place(x=100, y=120)

# Buttons for search and clear functionality
B = Button(root, text="Search", command=show_data, font=("verdana", 10, "bold"), borderwidth=2, bg="red", fg="white")
B.place(x=20, y=120)

clear_btn = Button(root, text="Clear", command=clear, font=("verdana", 10, "bold"), borderwidth=2, bg="blue", fg="white")
clear_btn.place(x=30, y=170)

root.mainloop()
