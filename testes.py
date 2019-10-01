import serial
import tkinter as tk
from tkinter import ttk

ser = serial.Serial('COM3', baudrate=9600, timeout=1)

arduinoDataString = ""
while arduinoDataString == "":
    arduinoData = ser.readline()
    arduinoDataString = arduinoData.decode("utf-8")

    findTemperatura = arduinoDataString.find("Temperatura: ")
    realTemp = arduinoDataString[findTemperatura + 13] + arduinoDataString[findTemperatura + 14]