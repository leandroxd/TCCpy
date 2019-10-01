import tkinter as tk
from tkinter import ttk  # Um tipo de CSS para Tkinter
import serial
from datetime import datetime
from threading import Timer

ser = serial.Serial('COM3', baudrate=9600, timeout=1)

LARGE_FONT = ("Verdana", 12)
TITLE = ("Verdana", 32)



def find_Temp():
    arduinoDataString = ""
    while arduinoDataString == "":
        arduinoData = ser.readline()
        arduinoDataString = arduinoData.decode("utf-8")

    findTemperatura = arduinoDataString.find("Temperatura: ")
    realTemp = arduinoDataString[findTemperatura + 13] + arduinoDataString[findTemperatura + 14]
    svTemp = realTemp

    return svTemp


def find_Umi():
    arduinoDataString = ""
    while arduinoDataString == "":
        arduinoData = ser.readline()
        arduinoDataString = arduinoData.decode("utf-8")

    findUmidade = arduinoDataString.find("Umidade: ")
    realUmi = arduinoDataString[findUmidade + 9] + arduinoDataString[findUmidade + 10] + arduinoDataString[
        findUmidade + 11] + arduinoDataString[findUmidade + 12] + arduinoDataString[findUmidade + 13]
    svUmi = realUmi

    return svUmi


def atualiza():
    find_Temp()
    find_Umi()




### Configurações basicas para ter telas multiplas


class ControleEstufa(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="006-gear.ico")  # Altera o incone do app (precisa converter para ICO)
        tk.Tk.wm_title(self, "Controle de Estufa")  # Adiciona titulos

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ConfPage, HistPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


#############################################################

# Tela que apresenta as estatisticas atuais

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Status da Estufa", font=TITLE)
        label.grid(row=0, column=1, columnspan=3)

        space = tk.Frame(self, height=50)
        space.grid(row=1, column=0, columnspan=3)


        labelTemp = ttk.Label(self, text="Temperatura", font=LARGE_FONT, relief="groove")
        labelTemp.grid(row=1, column=0)
        aTemp = find_Temp()
        svTemp = tk.StringVar()
        svTemp.set(aTemp)
        varTemp = ttk.Label(self, textvariable=svTemp, font=LARGE_FONT)
        varTemp.grid(row=2, column=0)

        space = tk.Frame(self, height=50, width=10)
        space.grid(row=1, column=1)

        labemUmi = ttk.Label(self, text="Umidade", font=LARGE_FONT, relief="groove")
        labemUmi.grid(row=1, column=2)
        svUmi = tk.StringVar()
        aUmi = find_Temp()
        svUmi.set(aUmi)
        varUmi = ttk.Label(self, textvariable=svUmi, font=LARGE_FONT)
        varUmi.grid(row=2, column=2)

        space = tk.Frame(self, height=50, width=10)
        space.grid(row=1, column=3)


        labelATemp = ttk.Label(self, text="Temperatura Agua", font=LARGE_FONT, relief="groove")
        labelATemp.grid(row=1, column=4)
        varATemp = ttk.Label(self, text="25", font=LARGE_FONT)
        varATemp.grid(row=2, column=4)

        space = tk.Frame(self, height=50)
        space.grid(row=3, column=0, columnspan=3)

        button = ttk.Button(self, text="Configurações", command=lambda: controller.show_frame(
            ConfPage))  # Precisa usar o lambda para passar parametros ou se nao executa apenas uma vez
        button.grid(row=4, column=0, ipady=3)

        button = ttk.Button(self, text="Historico", command=lambda: controller.show_frame(
            HistPage))  # Precisa usar o lambda para passar parametros ou se nao executa apenas uma vez
        button.grid(row=4, column=4, ipady=3)

        t = Timer(2, atualiza)
        t.start()


##############################################

### Tela de configuração

class ConfPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Configurações", font=TITLE)
        label.grid(row=0, column=1, columnspan=3)

        space = tk.Frame(self, height=20)
        space.grid(row=1, column=0, columnspan=3)

        labelTemp = ttk.Label(self, text="Temperatura", font=LARGE_FONT)
        labelTemp.grid(row=2, column=0, ipadx=5)
        varTempE = ttk.Entry(self)
        varTempE.grid(row=3, column=0, ipadx=5)

        space = tk.Frame(self, height=50, width=10)
        space.grid(row=2, column=1)

        labemUmi = ttk.Label(self, text="Umidade", font=LARGE_FONT)
        labemUmi.grid(row=2, column=2, ipadx=5)
        varUmiE = ttk.Entry(self)
        varUmiE.grid(row=3, column=2, ipadx=5)

        space = tk.Frame(self, height=50, width=10)
        space.grid(row=2, column=3)

        labelATemp = ttk.Label(self, text="Temperatura Agua", font=LARGE_FONT)
        labelATemp.grid(row=2, column=4, ipadx=5)
        varATempE = ttk.Entry(self)
        varATempE.grid(row=3, column=4, ipadx=5)

        space = tk.Frame(self, height=50)
        space.grid(row=4, column=0, columnspan=3)

        button1 = ttk.Button(self, text="Status", command=lambda: controller.show_frame(
            StartPage))  # Precisa usar o lambda para passar parametros ou se nao executa apenas uma vez
        button1.grid(row=5, column=0, ipadx=5, ipady=5)

        button3 = ttk.Button(self, text="Historico", command=lambda: controller.show_frame(
            HistPage))  # Precisa usar o lambda para passar parametros ou se nao executa apenas uma vez
        button3.grid(row=5, column=4, ipadx=5, ipady=5)


### Tela de historico
class HistPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Historico", font=TITLE)
        label.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Configuração", command=lambda: controller.show_frame(
            ConfPage))  # Precisa usar o lambda para passar parametros ou se nao executa apenas uma vez
        button2.pack()

        button4 = ttk.Button(self, text="Status", command=lambda: controller.show_frame(
            StartPage))  # Precisa usar o lambda para passar parametros ou se nao executa apenas uma vez
        button4.pack()


## Inicializando o app
app = ControleEstufa()

app.mainloop()
