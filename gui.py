import serial
import tkinter as tk
from tkinter import ttk

ser = serial.Serial('COM3', baudrate=9600, timeout=1)
def find_Temp():

    arduinoDataString = ""
    while arduinoDataString == "":
        arduinoData = ser.readline()
        arduinoDataString = arduinoData.decode("utf-8")

    findTemperatura = arduinoDataString.find("Temperatura: ")
    realTemp = arduinoDataString[findTemperatura + 13] + arduinoDataString[findTemperatura + 14]
    return realTemp


def find_Umi():
    arduinoDataString = ""
    while arduinoDataString == "":
        arduinoData = ser.readline()
        arduinoDataString = arduinoData.decode("utf-8")

    findUmidade = arduinoDataString.find("Umidade: ")
    realUmi = arduinoDataString[findUmidade + 9] + arduinoDataString[findUmidade + 10] + arduinoDataString[
        findUmidade + 11] + arduinoDataString[findUmidade + 12] + arduinoDataString[findUmidade + 13]

    return realUmi

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx= 0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, text="Temperatura", bg='yellow')
label.place(relx=0.01, rely=0, relwidth=0.15, relheight=0.05)


label = tk.Label(frame, text="Umidade", bg='yellow')
label.place(relx=0.30, rely=0, relwidth=0.15, relheight=0.05)

label = tk.Label(frame, text="Temperatura\nda\nagua", bg='yellow', justify='center')
label.place(relx=0.57, rely=0, relwidth=0.15, relheight=0.1)


root.mainloop()
