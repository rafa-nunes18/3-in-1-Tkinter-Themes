import tkinter as tk  
from tkinter import ttk  

root = tk.Tk()  

# Caminho para o arquivo de cursor  
cursor_path = "@/home/rafael/Documentos/GitHub/barra-titulo-oculta-Linux/imagens/cursores/cursores-linux/xcursor"  

# Criação do botão  
botao_fechar = ttk.Button(root, text="Fechar", command=root.destroy)  
botao_fechar.pack(pady=20)  

# Definindo o cursor  
try:  
    botao_fechar.config(cursor=cursor_path)  # Usar o cursor com o prefixo '@'  
except Exception as e:  
    print(f"Erro ao configurar o cursor: {e}")  

root.mainloop()