# Importar bibliotecas
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
root = tk.Tk()
estilo = ttk.Style()
   
caminho = os.getcwd()
print(caminho)
pasta_temas = os.path.join(caminho, 'temas')
lista_temas = [file for file in os.listdir(pasta_temas) if file.endswith('.tcl')]     
for tema in lista_temas:
    caminho_tema = os.path.join(pasta_temas, tema)
    print(caminho_tema)           
    root.call('source', caminho_tema)
print(estilo.theme_names())
estilo.theme_use('sun-valley-light')

root.mainloop()