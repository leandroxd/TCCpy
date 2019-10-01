import serial
import tkinter as tk
import time
import os
from multiprocessing import Process, current_process

ser = serial.Serial('COM3', baudrate=9600, timeout=1)

LARGE_FONT = ("Verdana", 12)
TITLE = ("Verdana", 32)

HEIGHT = 700
WIDTH = 800

processos = []

i=0

def find_Temp(svTemp):
    arduinoDataString = ""
    while arduinoDataString == "":
        arduinoData = ser.readline()
        arduinoDataString = arduinoData.decode("utf-8")

    findTemperatura = arduinoDataString.find("Temperatura: ")
    realTemp = arduinoDataString[findTemperatura + 13] + arduinoDataString[findTemperatura + 14]
    svTemp = realTemp
    print(realTemp)
    return svTemp


def find_Umi(svUmi):
    arduinoDataString = ""
    while arduinoDataString == "":
        arduinoData = ser.readline()
        arduinoDataString = arduinoData.decode("utf-8")

    findUmidade = arduinoDataString.find("Umidade: ")
    realUmi = arduinoDataString[findUmidade + 9] + arduinoDataString[findUmidade + 10] + arduinoDataString[
        findUmidade + 11] + arduinoDataString[findUmidade + 12] + arduinoDataString[findUmidade + 13]
    svUmi = realUmi
    print(realUmi)
    return svUmi


def atualiza():
    a = find_Temp(svTemp)
    svTemp.set(a)
    b = find_Umi(svUmi)
    svUmi.set(b)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label1 = tk.Label(frame, text="Temperatura", bg='yellow')
label1.place(relx=0.01, rely=0, relwidth=0.15, relheight=0.05)

svTemp = tk.StringVar()
temp = find_Temp(svTemp)
svTemp.set(temp)
label2 = tk.Label(frame, textvariable=svTemp, bg='yellow')
label2.place(relx=0.01, rely=0.06, relwidth=0.15, relheight=0.05)

label3 = tk.Label(frame, text="Umidade", bg='yellow')
label3.place(relx=0.18, rely=0, relwidth=0.15, relheight=0.05)

svUmi = tk.StringVar()
umi = find_Umi(svUmi)
svUmi.set(umi)
label4 = tk.Label(frame, textvariable=svUmi, bg='yellow')
label4.place(relx=0.18, rely=0.06, relwidth=0.15, relheight=0.05)

buttom1 = tk.Button(frame, text="Atualiza", command=atualiza)
buttom1.place(relx=0.1, rely=0.13, relwidth=0.15, relheight=0.05)

while 1:
    while i<100000:
        root.update()
        i = i+1
    atualiza()
    i=0