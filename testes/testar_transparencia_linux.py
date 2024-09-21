import tkinter as tk 
from tkinter import ttk 
from tkinter import *
import os
def main():  
    root = tk.Tk()  
    root.title("Janela com Fundo Transparente")
   

    # Remove a borda da janela  
    root.overrideredirect(True)
    root.geometry("400x300")    

    root.wm_attributes("-transparent", True) 


    f = tk.Frame(root, width=300, height=300, bg="systemTransparent")
   
    f.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")


    # Menu do Menubutton
    menu = tk.Menu(f)
    menu.add_command(label="Menu item 1")
    menu.add_command(label="Menu item 2")
    menu.add_separator()
    menu.add_command(label="Menu item 3")
    menu.add_command(label="Menu item 4")            

    # Menubutton
    menubutton = ttk.Menubutton(f, text="Menubutton", menu=menu, direction="below")
    menubutton.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

    cor_transparente = "#3af30c"
    try:
        root.wm_attributes("-transparentcolor", cor_transparente)            
    except Exception as e:   
        print(f"Erro ao ativar transparencia (class MyTema): {e}")  
  



    root.mainloop()  

if __name__ == "__main__":  
    main()