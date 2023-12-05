"""from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Bom dia", command=root.destroy).grid(column=1, row=0)
root.mainloop()
"""


class Escola:
    def __init__(self, nome, ano, turno):
        self.nome = nome1
        self.ano = ano1
        self.turno = turno1
nome1 = input("digite seu nome: ")
ano1 = input("digite o ano: ")
turno1 = input("digite o turno: ")

e = Escola(nome1, ano1, turno1)
print(e)

