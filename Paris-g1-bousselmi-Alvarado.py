#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Import all the databases
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
 
#Create a Tkinter window
root = tk.Tk()
root.title("CASIO")
 
#Define the dimensions of the graph
width = 5
height = 2
 
#The best companies returns----------------------------------------------------------------------------------------------------------------------
 
dow_jones_companies = {"Apple": "AAPL", "American Express": "AXP", "Caterpillar": "CAT", "Cisco": "CSCO", "Chevron": "CVX", "Disney": "DIS", "Goldman Sachs": "GS", "Home Depot": "HD", "IBM": "IBM", "Intel": "INTC", "Johnson & Johnson": "JNJ", "JPMorgan Chase": "JPM", "Coca-Cola": "KO", "McDonald's": "MCD", "3M": "MMM", "Merck": "MRK", "Microsoft": "MSFT", "Nike": "NKE", "Pfizer": "PFE", "Procter & Gamble": "PG", "Travelers": "TRV", "UnitedHealth Group": "UNH", "Raytheon Technologies": "RTX", "Verizon": "VZ", "Visa": "V", "Walgreens Boots Alliance": "WBA", "Walmart": "WMT"}
cac40_companies = {"Airbus SE": "AIR", "BNP Paribas": "BNP", "Carrefour": "CA", "Crédit Agricole": "ACA", "Danone": "BN","L'Oréal": "OR", "LVMH": "MC", "Orange": "ORA", "Peugeot": "UG", "Sanofi": "SAN", "Schneider Electric": "SU", "Unibail-Rodamco-Westfield": "URW"}
 
#Define the start and end dates of the desired period
start_date = "2017-01-01"
end_date = "2018-12-31"
 
#Choose 10 companies at random
random_companies_dow_jones = random.sample(list(dow_jones_companies.items()), 10)
random_companies_cac40 = random.sample(list(cac40_companies.items()), 10)
 
#Store the randomly selected companies in a list
stock_symbols = []
for company, symbol in random_companies_dow_jones:
    stock_symbols.append(symbol)
stock_symbols2 = []
for company, symbol in random_companies_cac40:
    stock_symbols2.append(symbol)
 
#Print the names and symbols of the randomly selected companies
print("The companies we have chosen in the Dow Jones are:")
for company, symbol in random_companies_dow_jones:
    print(f"{company} --> {symbol}")
print("")
print("The companies we have chosen in the CAC40 are:")
for company, symbol in random_companies_cac40:
    print(f"{company} --> {symbol}")
 
#Get the adjusted close prices for each stock during the desired period
adj_close_dow_jones = yf.download([symbol for _, symbol in random_companies_dow_jones], start=start_date, end=end_date)["Adj Close"]
adj_close_cac40 = yf.download([symbol for _, symbol in random_companies_cac40], start=start_date, end=end_date)["Adj Close"]
 
#Calculate the daily returns for each stock
daily_returns_dow_jones = adj_close_dow_jones.pct_change()
daily_returns_cac40 = adj_close_cac40.pct_change()
 
#Calculate the annualized average daily return for each stock
annualized_returns_dow_jones = (1 + daily_returns_dow_jones.mean()) ** 252 - 1
annualized_returns_cac40 = (1 + daily_returns_cac40.mean()) ** 252 - 1
 
#Sort the stocks by their annualized average daily return in descending order
sorted_returns_dow_jones = annualized_returns_dow_jones.sort_values(ascending=False)[:3]
sorted_returns_cac40 = annualized_returns_cac40.sort_values(ascending=False)[:3]
sorted_returns = pd.concat([sorted_returns_dow_jones, sorted_returns_cac40]).sort_values(ascending=False)[:6]
 
#Print the 3 best stocks sorted by their annualized average return
print("Top 3 annualized average returns of randomly selected stocks in the Dow Jones:")
for i, (symbol, avg_return) in enumerate(sorted_returns_dow_jones.items()):
    print(f"{i+1}. {symbol} --> {avg_return:.2%}")
print("")
print("Top 3 annualized average returns of randomly selected stocks in the CAC40:")
for i, (symbol, avg_return) in enumerate(sorted_returns_cac40.items()):
    print(f"{i+1}. {symbol} --> {avg_return:.2%}")
 
#Create a plot of the adjusted close prices of the 6 best stocks
fig = plt.Figure(figsize=(width, height), dpi=100)
ax = fig.add_subplot(111)
 
for symbol in sorted_returns.index:
    if symbol in adj_close_dow_jones.columns:
        ax.plot(adj_close_dow_jones[symbol], label=symbol + " ({:.2%})".format(sorted_returns[symbol]))
    else:
        ax.plot(adj_close_cac40[symbol], label=symbol + " ({:.2%})".format(sorted_returns[symbol]))
 
#Add the stock symbols to the legend
ax.legend()
 
#Create a canvas for the graph and add it to the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 
#Define new values for x- and y-axes
new_xticks = ["Jan17", "Avr17", "Juil17", "Oct17", "Jan18", "Avr18", "Juil18", "Oct18", "Dec18"]
new_yticks = ["10%", "20%", "30%", "40%", "50%"]
 
#Changing the x- and y-axis values
ax.set_xticklabels(new_xticks)
ax.set_yticklabels(new_yticks)
 
ax.set_title("Best returns for 6 randoms of the CAC40 & the Dow Jones")
 
#The calculatrice value--------------------------------------------------------------------------------------------------------------------------
 
#Create a canvas for the rectangles and the numbers
canvas = tk.Canvas(root, width=525, height=525, bg="light grey")
canvas.pack(fill="both", expand=True)
 
# Define button coordinates and labels
button_data = [
    (25, 25, 125, 125, "7"),
    (150, 25, 250, 125, "8"),
    (275, 25, 375, 125, "9"),
    (400, 25, 500, 125, "÷"),
    (25, 160, 125, 260, "4"),
    (150, 160, 250, 260, "5"),
    (275, 160, 375, 260, "6"),
    (400, 160, 500, 260, "x"),
    (25, 285, 125, 385, "1"),
    (150, 285, 250, 385, "2"),
    (275, 285, 375, 385, "3"),
    (400, 285, 500, 385, "-"),
    (25, 410, 125, 510, "0"),
    (150, 410, 250, 510, "."),
    (275, 410, 375, 510, "="),
    (400, 410, 500, 510, "+")
]
 
# Create buttons
for x1, y1, x2, y2, label in button_data:
    rect = canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    x_center, y_center = (x1 + x2) / 2, (y1 + y2) / 2
    canvas.create_text(x_center, y_center, text=label, fill="white", font=("Arial", 40))
 
#Start the Tkinter event loop
root.mainloop()
