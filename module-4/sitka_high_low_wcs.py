# William Stearns
# Module 4.2 
# 4-7-25
# Updated existing code to add a GUI interface using tkinter and choice to view Highs or lows.

import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt


def read_weather_data(column_index): #Updated existing code to add a column index parameter to read the highs or lows.
    filename = 'sitka_weather_2018_simple.csv'
    dates, temps = [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                temp = int(row[column_index])
                dates.append(current_date)
                temps.append(temp)
            except ValueError:
                continue
    return dates, temps


def show_highs(): #Updated existing code to add a function to show highs.
    dates, highs = read_weather_data(5)
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.set_title("Daily High Temperatures - 2018", fontsize=20)
    ax.set_xlabel('')
    ax.set_ylabel("Temperature (F)", fontsize=14)
    fig.autofmt_xdate()
    plt.show()


def show_lows(): #Updated existing code to add a function to show lows.
    dates, lows = read_weather_data(6)
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue') #blue for lows
    ax.set_title("Daily Low Temperatures - 2018", fontsize=20)
    ax.set_xlabel('')
    ax.set_ylabel("Temperature (F)", fontsize=14)
    fig.autofmt_xdate()
    plt.show()


def quit_program(): #Updated existing code to add a function to quit the program.
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()


# --- GUI Setup ---
root = tk.Tk()
root.title("Sitka Weather Viewer")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Sitka Weather Viewer (2018)", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=20)

# Buttons
btn_highs = tk.Button(root, text="View High Temperatures", command=show_highs, width=30)
btn_highs.pack(pady=10)

btn_lows = tk.Button(root, text="View Low Temperatures", command=show_lows, width=30)
btn_lows.pack(pady=10)

btn_quit = tk.Button(root, text="Exit Program", command=quit_program, width=30)
btn_quit.pack(pady=30)

# Run the GUI
root.mainloop()
