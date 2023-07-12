import requests
import json
import winsound
from tkinter import *

def consult_dolar():
    request = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
    price = json.loads(request.text)
    dolar_max = price["USDBRL"]["high"]
    dolar_price = price["USDBRL"]["bid"]
    dolar_min = price["USDBRL"]["low"]
    dolar_result_label.config(text=f"Valor máximo: {dolar_max}\nValor atual: {dolar_price}\nValor mínimo: {dolar_min}")
    beep()

def consult_euro():
    request = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
    price = json.loads(request.text)
    eur_max = price["EURBRL"]["high"]
    eur_price = price["EURBRL"]["bid"]
    eur_min = price["EURBRL"]["low"]
    
    euro_result_label.config(text=f"Valor máximo: {eur_max}\nValor atual: {eur_price}\nValor mínimo: {eur_min}")
    beep()

def beep():
    winsound.Beep(1800, 200)

app = Tk()
app.title("CONSULTAR DOLAR E EURO")
app.geometry("500x300")
app.configure(background="#008")

txt1 = Label(app, text = "CONSULTAR DOLAR E EURO", background="#ff0", foreground= "#000")
txt1.place(x=100, y=20, width = 300, height = 30)

btn = Button(app, text = "Consultar Dólar", command = consult_dolar).place(x=150, y= 70, width= 200,height= 30)
btn = Button(app, text = "Consultar Euro", command = consult_euro).place(x=150, y= 170, width= 200,height= 30)

dolar_result_label = Label(app, background="#008", foreground="#fff")
dolar_result_label.place(x=100, y=100, width=300, height=60)

euro_result_label = Label(app, background="#008", foreground="#fff")
euro_result_label.place(x=100, y=200, width=300, height=60)

app.mainloop()






