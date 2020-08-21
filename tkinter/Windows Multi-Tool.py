import tkinter.font as font
from tkinter import *
from tkinter import messagebox

import GPUtil
import platform
import psutil
import pyautogui
import pyperclip
import re
import requests
import sqlite3
import threading
import time

root = Tk()

root.title("Windows Multi-Tool")
root.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\MAIN.ico")

root.configure(background='white')

titleFont = font.Font(family='Verdana', size=10, weight='bold', slant='italic')

title = Label(root, text="Windows Multi-Tool", padx=10, pady=12, borderwidth=7, bg="white")

title.grid()
title['font'] = titleFont

frame = LabelFrame(root, padx=30, pady=30, bg="gray80", relief="sunken")
frame.grid(padx=10, pady=8)


def notes():
    note = Toplevel()
    note.title("Notes")
    note.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\NOTES.ico")

    conn = sqlite3.connect('notesMemory.db')

    c = conn.cursor()

    c.execute(""" CREATE TABLE if not exists lines (
            line1 text,
            line2 text,
            line3 text,
            line4 text,
            line5 text,
            line6 text,
            line7 text,
            line8 text,
            line9 text,
            line10 text,
            line11 text,
            line12 text,
            line13 text,
            line14 text,
            line15 text,
            line16 text,
            line17 text,
            line18 text,
            line19 text,
            line20 text,
            line21 text,
            line22 text,
            line23 text
            )""")

    def save():
        conn = sqlite3.connect('notesMemory.db')

        c = conn.cursor()

        c.execute("DELETE from lines WHERE oid=1")

        c.execute("INSERT INTO lines VALUES (:line1, :line2, :line3, :line4, :line5, :line6, :line7, :line8, :line9, :line10, :line11, :line12, :line13, :line14, :line15, :line16, :line17, :line18, :line19, :line20, :line21, :line22, :line23)",
                  {
                      'line1': e1.get(),
                      'line2': e2.get(),
                      'line3': e3.get(),
                      'line4': e4.get(),
                      'line5': e5.get(),
                      'line6': e6.get(),
                      'line7': e7.get(),
                      'line8': e8.get(),
                      'line9': e9.get(),
                      'line10': e10.get(),
                      'line11': e11.get(),
                      'line12': e12.get(),
                      'line13': e13.get(),
                      'line14': e14.get(),
                      'line15': e15.get(),
                      'line16': e16.get(),
                      'line17': e17.get(),
                      'line18': e18.get(),
                      'line19': e19.get(),
                      'line20': e20.get(),
                      'line21': e21.get(),
                      'line22': e22.get(),
                      'line23': e23.get()})

        conn.commit()

        conn.close()

    b = Button(note, padx=298, pady=15, state=DISABLED, bg="light grey").grid(row=0, column=0)

    e1 = Entry(note, width=100)
    e1.grid(row=2, column=0)
    e2 = Entry(note, width=100)
    e2.grid(row=3, column=0)
    e3 = Entry(note, width=100)
    e3.grid(row=4, column=0)
    e4 = Entry(note, width=100)
    e4.grid(row=5, column=0)
    e5 = Entry(note, width=100)
    e5.grid(row=6, column=0)
    e6 = Entry(note, width=100)
    e6.grid(row=7, column=0)
    e7 = Entry(note, width=100)
    e7.grid(row=8, column=0)
    e8 = Entry(note, width=100)
    e8.grid(row=9, column=0)
    e9 = Entry(note, width=100)
    e9.grid(row=10, column=0)
    e10 = Entry(note, width=100)
    e10.grid(row=11, column=0)
    e11 = Entry(note, width=100)
    e11.grid(row=12, column=0)
    e12 = Entry(note, width=100)
    e12.grid(row=13, column=0)
    e13 = Entry(note, width=100)
    e13.grid(row=14, column=0)
    e14 = Entry(note, width=100)
    e14.grid(row=15, column=0)
    e15 = Entry(note, width=100)
    e15.grid(row=16, column=0)
    e16 = Entry(note, width=100)
    e16.grid(row=17, column=0)
    e17 = Entry(note, width=100)
    e17.grid(row=18, column=0)
    e18 = Entry(note, width=100)
    e18.grid(row=19, column=0)
    e19 = Entry(note, width=100)
    e19.grid(row=20, column=0)
    e20 = Entry(note, width=100)
    e20.grid(row=21, column=0)
    e21 = Entry(note, width=100)
    e21.grid(row=22, column=0)
    e22 = Entry(note, width=100)
    e22.grid(row=23, column=0)
    e23 = Entry(note, width=100)
    e23.grid(row=24, column=0)

    saveButton = Button(note, text="Save", bg="white", padx=286, pady=5, relief="sunken", command=save).grid(row=26, column=0)

    c.execute("SELECT *, oid FROM lines")

    reeshu = c.fetchall()

    mikail = reeshu[0]

    e1.insert(0, mikail[0])
    e2.insert(0, mikail[1])
    e3.insert(0, mikail[2])
    e4.insert(0, mikail[3])
    e5.insert(0, mikail[4])
    e6.insert(0, mikail[5])
    e7.insert(0, mikail[6])
    e8.insert(0, mikail[7])
    e9.insert(0, mikail[8])
    e10.insert(0, mikail[9])
    e11.insert(0, mikail[10])
    e12.insert(0, mikail[11])
    e13.insert(0, mikail[12])
    e14.insert(0, mikail[13])
    e15.insert(0, mikail[14])
    e16.insert(0, mikail[15])
    e17.insert(0, mikail[16])
    e18.insert(0, mikail[17])
    e19.insert(0, mikail[18])
    e20.insert(0, mikail[19])
    e21.insert(0, mikail[20])
    e22.insert(0, mikail[21])
    e23.insert(0, mikail[22])

    conn.commit()

    conn.close()

    note.mainloop()


def weather():
    wet = Toplevel()
    wet.title("Weather")
    wet.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\WEATHER.ico")

    wet.configure(background='white')
    fx = LabelFrame(wet, padx=80, pady=20, bg="light grey", relief="sunken")
    fx.grid(row=3, column=0, padx=10)

    # CONTINUE BUTTON
    def commit():

        city_name = e.get()

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()

        cFont = font.Font(family='Verdana', size=10)

        if x["cod"] != "404":

            y = x["main"]

            current_temperature = y["temp"]

            current_pressure = y["pressure"]

            current_humidity = y["humidity"]

            z = x["weather"]

            weather_description = z[0]["description"]

            def capitalize(name):
                indexOfSpace = 0
                for a in range(len(name)):
                    if name[a].isspace():
                        indexOfSpace = a

                if indexOfSpace != 0:
                    name.lower()
                    firstLetter = name[0:1].upper()
                    secondLetter = name[indexOfSpace+1:indexOfSpace+2].upper()
                    return firstLetter + name[1:indexOfSpace].lower() + " " + secondLetter + name[indexOfSpace+2:].lower()

                elif indexOfSpace == 0:
                    name.lower()
                    firstLetter = name[0:1].upper()
                    return firstLetter + name[1:].lower()

            cityName = capitalize(city_name)

            nFont = font.Font(family='Verdana', size=11, weight='bold')
            nam = Label(fx, text=cityName + "'s Weather", padx=10, pady=5, bg="light grey", font=nFont)
            nam.grid(row=2, column=0)
            cel = Label(fx, text="Temperature: " + str(round(current_temperature - 273.15, 1)) + " °C", padx=10, pady=5, bg="light grey", font=cFont)
            cel.grid(row=3, column=0)
            hum = Label(fx, text="Humidity: " + str(current_humidity) + "%", padx=10, pady=5, bg="light grey", font=cFont)
            hum.grid(row=4, column=0)
            des = Label(fx, text="Description: " + str(weather_description), padx=10, pady=5, bg="light grey", font=cFont)
            des.grid(row=5, column=0)

        else:
            nFont = font.Font(family='Verdana', size=9, slant='italic')
            f2 = LabelFrame(wet, padx=73, pady=10, bg="light grey", relief="sunken")
            f2.grid(row=6, column=0, padx=10,pady=8)

            noLab = Label(f2, text="City not found. Please try again.", padx=10, bg="light grey", font=nFont).grid(row=0, column=0)

    api_key = "5fd50adf4892c33261fe0dd0fc96a951"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    wetFont = font.Font(family='Verdana', size=9, weight='bold', slant="italic")
    bFont = font.Font(family='Verdana', size=9, slant='italic')

    l = Label(wet, text="Enter a city to get it's local weather data",  pady=7, padx=6, font=wetFont, bg='white')
    l.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    f = LabelFrame(wet, padx=10, pady=20, bg="light grey", relief="sunken")
    f.grid(padx=10, pady=8)

    e = Entry(f, width=30, borderwidth=3, font=bFont, bg="white")
    e.grid(row=1, column=0, padx=8)

    b2 = Button(f, text="Submit", command=commit, padx=6, font=bFont, bg="white")
    b2.grid(row=1, column=1, padx=6)

    wet.mainloop()


def text():
    text = Toplevel()
    text.title("Text Filter")

    text.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\EPD SEARCH.ico")

    text.configure(background='white')

    cFont = font.Font(family='Verdana', size=8)
    epdFont = font.Font(family='Verdana', size=10, weight='bold', slant='italic')

    fr = LabelFrame(text, padx=50, pady=10, bg="light grey", relief="sunken")
    fr.grid(row=2, padx=10, pady=8)

    phone = re.compile(r'''(
    (\d{3}|\(\d\))?
    (\s|-|\.)
    (\d{3})
    (\s|-|\.)
    (\d{4})
    )''', re.VERBOSE)

    email = re.compile(r'''(
    [a-zA-Z0-9.]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

    date = re.compile(r'''
    (\d\d)
    (/|-)
    (\d\d)
    (/|-)
    (\d\d\d\d)
    ''', re.VERBOSE)

    input = str(pyperclip.paste())

    def checkForText():
        results = []
        for groups in phone.findall(input):
            results.append('-'.join([groups[1], groups[3], groups[5]]))
        for groups in email.findall(input):
            results.append(groups[0])
        for groups in date.findall(input):
            day = int(groups[0])
            month = int(groups[2])
            year = int(groups[4])
            if 31 >= day > 27:
                if 12 >= month > 0:
                    if 2999 >= year > 0:
                        results.append('/'.join([groups[0], groups[2], groups[4]]))

        if len(results) > 0:
            pyperclip.copy('\n'.join(results))
            resultLabel = Label(fr, text="I found " + str(len(results)) + " result(s).", borderwidth=5, bg="light grey",font=cFont).grid(
                row=0, column=0)

            tracker = 1
            for result in results:
                e = Entry(fr, width=35)
                e.insert(0, result)
                e.grid(row=tracker, column=0, pady=5, padx=10)
                tracker += 1
            endingLabel = Label(fr, text="I copied them all in your clipboard!", bg="light grey", borderwidth=5, font=cFont).grid(
                row=tracker, column=0)

        else:
            noLabel = Label(fr, text="I couldn't find anything, make sure you\nhave what you want searched copied.", bg="light grey", font=cFont).grid(row=2,
                                                                                                                  column=0)

    f = LabelFrame(text, padx=90, pady=10, bg="light grey", relief="sunken")
    f.grid(row=1, padx=10, pady=6)

    textFont = font.Font(family='Verdana', size=9, weight='bold', slant='italic')

    l = Label(text, text="Check for emails, phone numbers and dates\nwith what's copied on your clipboard.", bg="white", padx=18, pady=9, font=textFont)
    l.grid(row=0, column=0, pady=8, padx=10)

    bFont = font.Font(family='Verdana', size=9, slant='italic')
    inputButton = Button(f, text="Search the clipboard", command=checkForText, font=bFont, bg="white")
    inputButton.grid(row=1, column=0, padx=10, pady=5)

    text.mainloop()


def calculator():
    top = Toplevel()
    top.title("Calculator")
    top.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\CALCULATOR.ico")

    top.configure(background='white')

    e = Entry(top, width=55, borderwidth=5, bg="light gray")
    e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear():
        e.delete(0, END)

    def button_equal():
        second_number = e.get()
        e.delete(0, END)
        if prev_cond == "+":
            e.insert(0, f_num + int(second_number))
        elif prev_cond == "-":
            e.insert(0, f_num - int(second_number))
        elif prev_cond == "x":
            e.insert(0, f_num * int(second_number))
        elif prev_cond == "/":
            e.insert(0, int(f_num / int(second_number)))

    def button_add():
        first_number = e.get()
        global f_num
        global prev_cond
        f_num = int(first_number)
        prev_cond = "+"
        e.delete(0, END)

    def button_subtract():
        first_number = e.get()
        global f_num
        global prev_cond
        f_num = int(first_number)
        prev_cond = "-"
        e.delete(0, END)

    def button_multiply():
        first_number = e.get()
        global f_num
        global prev_cond
        f_num = int(first_number)
        prev_cond = "x"
        e.delete(0, END)

    def button_divide():
        first_number = e.get()
        global f_num
        global prev_cond
        f_num = int(first_number)
        prev_cond = "/"
        e.delete(0, END)

    button_1 = Button(top, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="white")
    button_2 = Button(top, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="white")
    button_3 = Button(top, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="white")
    button_4 = Button(top, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="white")
    button_5 = Button(top, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="white")
    button_6 = Button(top, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="white")
    button_7 = Button(top, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="white")
    button_8 = Button(top, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="white")
    button_9 = Button(top, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="white")
    button_0 = Button(top, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="white")

    button_equal = Button(top, text="=", padx=39, pady=20, command=button_equal, bg="white")
    button_clear = Button(top, text="CE", padx=36, pady=20, command=button_clear, bg="white")

    button_add = Button(top, text="+", padx=39, pady=20, command=button_add, bg="light gray")
    button_sub = Button(top, text="–", padx=40, pady=20, command=button_subtract, bg="light gray")
    button_mul = Button(top, text="x", padx=40, pady=20, command=button_multiply, bg="light gray")
    button_div = Button(top, text="÷", padx=39, pady=20, command=button_divide, bg="light gray")

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)

    button_clear.grid(row=4, column=1)
    button_equal.grid(row=4, column=2)

    button_add.grid(row=1, column=4)
    button_sub.grid(row=2, column=4)
    button_mul.grid(row=3, column=4)
    button_div.grid(row=4, column=4)

    top.mainloop()


def drawing():
    x, y = 0, 0

    def xy(event):
        global x, y
        x, y = event.x, event.y

    def addLine(event):
        global x, y
        c.create_line((x, y, event.x, event.y))
        x, y = event.x, event.y

    draw = Toplevel()

    draw.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\DRAWING.ico")
    draw.geometry("800x600")
    draw.columnconfigure(0, weight=1)
    draw.rowconfigure(0, weight=1)

    c = Canvas(draw)
    c.grid(column=0, row=0, sticky=(N, W, E, S))
    c.bind("<Button-1>", xy)
    c.bind("<B1-Motion>", addLine)

    root.mainloop()


def reminder():
    rem = Toplevel()
    rem.title("Reminder")
    rem.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\REMINDER.ico")

    rem.configure(background='white')

    remFont = font.Font(family='Verdana', size=10, weight='bold', slant='italic')
    bFont = font.Font(family='Verdana', size=9, slant='italic')

    f = LabelFrame(rem, padx=30, pady=18, bg="light grey", relief="sunken")
    f.grid(padx=10, pady=8, row=1)

    start = Label(rem, text="Set Reminders! Time is in Minutes.", font=remFont, pady=8, bg="white")
    start.grid(row=0, pady=5)
    l1 = Label(f, text="Reminder", padx=20, bg="light grey", font=bFont).grid(row=0, column=0, padx=10)
    l2 = Label(f, text="Time", padx=5, bg="light grey", font=bFont).grid(row=0, column=1, padx=10)
    e1 = Entry(f, width=30, borderwidth=3)
    e2 = Entry(f, width=9, borderwidth=3)

    e1.grid(row=1, column=0, padx=15)
    e2.grid(row=1, column=1, padx=10)

    fx = LabelFrame(rem, padx=100, pady=15, bg="light grey", relief="sunken")
    fx.grid(padx=10, pady=8)

    cFont = font.Font(family='Verdana', size=10)

    def receive():
        def temp():
            r = e1.get()
            t = int(e2.get()) * 60

            initial = round(time.time(), 0)

            Label(fx, text="Reminder: " + r + " in " + str(t / 60) + " minute(s)", bg="light grey", font=cFont).grid()

            while True:
                if round(time.time(), 0) - t == initial:
                    response = messagebox.showinfo("Reminder", r)
                    break

            e1.delete(0, END)
            e2.delete(0, END)

        thread = threading.Thread(target=temp)
        thread.daemon = True
        thread.start()

    b1 = Button(f, text="Submit", padx=10, command=receive, font=bFont, bg="white")
    b1.grid(row=1, column=2, padx=15)

    rem.mainloop()


def system():
    si = Toplevel()
    si.title("System Information")
    si.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\settings.ico")

    si.configure(background='white')

    def refresh():
        while True:
            def get_size(bytes, suffix="B"):
                factor = 1024
                for unit in ["", "K", "M", "G", "T", "P"]:
                    if bytes < factor:
                        return f"{bytes:.2f}{unit}{suffix}"
                    bytes /= factor

            remFont = font.Font(family='Verdana', size=10, weight='bold', slant='italic')
            bFont = font.Font(family='Verdana', size=9, slant='italic')

            uname = platform.uname()
            swap = psutil.swap_memory()
            partitions = psutil.disk_partitions()
            partition_usage = psutil.disk_usage(partitions[0].mountpoint)

            Label(si, text="CPU", pady=8, bg="white", font=remFont).grid(row=2, column=0, padx=8)
            Label(si, text="Memory", pady=8, bg="white", font=remFont).grid(row=2, column=1, padx=8)
            Label(si, text="GPU", pady=8, bg="white", font=remFont).grid(row=2, column=2, padx=8)

            ayu = LabelFrame(si, padx=10, pady=18, bg="LightBlue1", relief="sunken")
            ayu.grid(padx=10, pady=8, row=3, columnspan=1, column=0)

            psutil.cpu_count(logical=False)
            cpufreq = psutil.cpu_freq()
            Label(ayu, text="Physical cores: " + str(psutil.cpu_count(logical=False)), pady=8, bg="LightBlue1", font=bFont).grid(row=1, padx=8)
            Label(ayu, text=f"Current Frequency: {cpufreq.current:.2f}Mhz", pady=8, bg="LightBlue1", font=bFont).grid(row=2, padx=8)
            Label(ayu, text=f"Max Frequency: {cpufreq.max:.2f}Mhz", pady=8, bg="LightBlue1", font=bFont).grid(row=3, padx=8)
            Label(ayu, text=f"Total CPU Usage: {psutil.cpu_percent()}%", pady=8, bg="LightBlue1", font=bFont).grid(row=4, padx=8)

            ayo = LabelFrame(si, padx=10, pady=18, bg="indianred1", relief="sunken")
            ayo.grid(padx=10, pady=8, row=3, columnspan=1, column=1)

            svmem = psutil.virtual_memory()
            Label(ayo, text=f"Total: {get_size(svmem.total)}", pady=8, bg="indianred1", font=bFont).grid(row=0, padx=8)
            Label(ayo, text=f"Percentage: {svmem.percent}%", pady=8, bg="indianred1", font=bFont).grid(row=3, padx=8)
            Label(ayo, text=f"Available: {get_size(svmem.available)}", pady=8, bg="indianred1", font=bFont).grid(row=2, padx=8)
            Label(ayo, text=f"Used: {get_size(svmem.used)}", pady=8, bg="indianred1", font=bFont).grid(row=1, padx=8)

            aya = LabelFrame(si, padx=10, pady=18, bg="pale green", relief="sunken")
            aya.grid(padx=10, pady=8, row=3, columnspan=1, column=2)

            gpus = GPUtil.getGPUs()
            list_gpus = []
            for gpu in gpus:
                # name of GPU
                gpu_name = gpu.name
                # get % percentage of GPU usage of that GPU
                gpu_load = f"{gpu.load * 100}%"
                # get free memory in MB format
                gpu_free_memory = f"{gpu.memoryFree}MB"
                # get used memory
                gpu_used_memory = f"{gpu.memoryUsed}MB"
                # get total memory
                gpu_total_memory = f"{gpu.memoryTotal}MB"
                # get GPU temperature in Celsius
                gpu_temperature = f"{gpu.temperature} °C"

            Label(aya, text=f"Name: " + gpu.name, pady=8, bg="pale green", font=bFont).grid(row=0, padx=8)
            Label(aya, text=f"Memory: {gpu.memoryTotal}MB", pady=8, bg="pale green", font=bFont).grid(row=1, padx=8)
            Label(aya, text=f"Temperature: {gpu.temperature} °C", pady=8, bg="pale green", font=bFont).grid(row=2, padx=8)
            Label(aya, text=f"Percentage: {int(gpu.load * 100)}%", pady=8, bg="pale green", font=bFont).grid(row=3, padx=8)
            time.sleep(4)

    thread = threading.Thread(target=refresh)
    thread.daemon = True
    thread.start()

    si.mainloop()


def clicker():
    dev = Toplevel()
    dev.title("Screen Clicker")
    dev.configure(background='white')
    dev.iconbitmap(r"C:\Users\mikai\Desktop\Mikail\Coding\PycharmProjects\Main\tkinter\Icons\tap.ico")

    remFont = font.Font(family='Verdana', size=10, weight='bold', slant='italic')
    bFont = font.Font(family='Verdana', size=9, slant='italic')

    Label(dev, padx=30, pady=6, font=remFont, text="Screen Clicker", bg="white").grid(row=0, pady=5)

    f = LabelFrame(dev, padx=50, pady=18, bg="light grey", relief="sunken")
    f.grid(padx=10, pady=8, row=2)

    Label(dev, padx=5, pady=0, font=bFont, text="This program simulates a mouse click.\nIt will click at every desired interval.\nMove the mouse to the desired location.\nPress 'q' to stop the automation.", bg="white").grid(row=1, columnspan=2)

    Label(f, padx=2, pady=10, font=bFont, text="How often:", bg="light gray").grid(row=1, column=0)

    e1 = Entry(f, width=10, borderwidth=3)

    e1.grid(row=1, column=1, padx=5)

    temp = True
    def rec():
        interval = int(e1.get())

        def deltaClick():
            while temp:
                time.sleep(interval)
                pyautogui.click(pyautogui.position())

        thread = threading.Thread(target=deltaClick)
        thread.daemon = True
        thread.start()

    def cer():
        root.destroy()

    b1 = Button(f, text="Start", padx=53, command=rec, font=bFont, bg="white")
    b1.grid(row=2, columnspan=2, padx=5, pady=8)

    b2 = Button(f, text="Stop", padx=55, command=cer, font=bFont, bg="white")
    b2.grid(row=3, columnspan=2, padx=5, pady=8)

    dev.mainloop()


buttonFont = font.Font(family='Verdana', size=8, slant='italic')

noteButton = Button(frame, text="Notes Page", padx=13, pady=20, borderwidth=2, command=notes, bg="white", font=buttonFont)
weatherButton = Button(frame, text="Weather", padx=21, pady=20, borderwidth=2, command=weather, bg="white", font=buttonFont)
textButton = Button(frame, text="Text Filter", padx=19, pady=20, borderwidth=2, command=text, bg="white", font=buttonFont)
calculatorButton = Button(frame, text="Calculator", padx=19, pady=20, borderwidth=2, command=calculator, bg="white", font=buttonFont)
drawingButton = Button(frame, text="Drawing", padx=22, pady=20, borderwidth=2, command=drawing, bg="white", font=buttonFont)
reminderButton = Button(frame, text="Reminders", padx=17, pady=20, borderwidth=2, command=reminder, bg="white", font=buttonFont)
systemInfoButton = Button(frame, text="System Info", padx=13, pady=20, borderwidth=2, command=system, bg="white", font=buttonFont)
clickerButton = Button(frame, text="Screen Clicker", padx=4, pady=20, borderwidth=2, command=clicker, bg="white", font=buttonFont)

noteButton.grid(row=0, column=1)
weatherButton.grid(row=2, column=1)
textButton.grid(row=3, column=0)
calculatorButton.grid(row=0, column=0)
drawingButton.grid(row=3, column=1)
reminderButton.grid(row=1, column=0)
systemInfoButton.grid(row=2, column=0)
clickerButton.grid(row=1, column=1)


root.mainloop()
