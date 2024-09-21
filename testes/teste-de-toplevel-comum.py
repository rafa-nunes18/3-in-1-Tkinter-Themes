import tkinter as tk  
from tkinter import Toplevel, messagebox  

def abrir_toplevel():  
    # Cria uma nova janela Toplevel  
    nova_janela = Toplevel(root)  
    nova_janela.title("Nova Janela")  
    nova_janela.geometry("300x200")  

    # Cria um Frame dentro do Toplevel  
    frame = tk.Frame(nova_janela)  
    frame.pack(pady=20)  

    # Função para mostrar qual botão foi apertado  
    def mostrar_mensagem(botao):  
        messagebox.showinfo("Botão Apertado", f"O botão '{botao}' foi apertado!")  

    # Cria botões dentro do Frame  
    botao1 = tk.Button(frame, text="Botão 1", command=lambda: mostrar_mensagem("Botão 1"))  
    botao1.pack(side=tk.LEFT, padx=5)  

    botao2 = tk.Button(frame, text="Botão 2", command=lambda: mostrar_mensagem("Botão 2"))  
    botao2.pack(side=tk.LEFT, padx=5)  

    botao3 = tk.Button(frame, text="Botão 3", command=lambda: mostrar_mensagem("Botão 3"))  
    botao3.pack(side=tk.LEFT, padx=5)  

root = tk.Tk()  
root.title("Janela Principal")  
root.geometry("400x300")  

# Botão para abrir o Toplevel  
botao_abrir = tk.Button(root, text="Abrir Toplevel", command=abrir_toplevel)  
botao_abrir.pack(pady=20)  

root.mainloop()