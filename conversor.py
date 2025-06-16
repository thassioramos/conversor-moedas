import tkinter as tk
from tkinter import ttk
import requests

# Lista de moedas suportadas
MOEDAS = ["USD", "BRL", "EUR", "JPY", "GBP", "AUD", "CAD"]

def converter():
    try:
        valor = float(entrada_valor.get())
        de = combo_de.get()
        para = combo_para.get()

        if de == para:
            resultado_var.set(f"{valor:.2f} {de} = {valor:.2f} {para}")
            return

        url = f"https://economia.awesomeapi.com.br/json/last/{de}-{para}"
        response = requests.get(url)
        data = response.json()

        taxa = float(data[f"{de}{para}"]["bid"])
        convertido = valor * taxa
        resultado_var.set(f"{valor:.2f} {de} = {convertido:.2f} {para}")
    except Exception as e:
        resultado_var.set("Erro na conversão.")

# Interface com Tkinter
janela = tk.Tk()
janela.title("Conversor de Moedas")

# Estilo
janela.geometry("300x220")
janela.resizable(False, False)

tk.Label(janela, text="Valor:").pack()
entrada_valor = tk.Entry(janela)
entrada_valor.pack()

tk.Label(janela, text="De:").pack()
combo_de = ttk.Combobox(janela, values=MOEDAS)
combo_de.set("USD")
combo_de.pack()

tk.Label(janela, text="Para:").pack()
combo_para = ttk.Combobox(janela, values=MOEDAS)
combo_para.set("BRL")
combo_para.pack()

tk.Button(janela, text="Converter", command=converter).pack(pady=10)

resultado_var = tk.StringVar()
tk.Label(janela, textvariable=resultado_var, font=("Arial", 12, "bold")).pack()

janela.mainloop()
