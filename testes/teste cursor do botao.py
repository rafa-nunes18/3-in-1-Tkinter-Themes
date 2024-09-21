from tkinter import * 
from tkinter import ttk 

# Criar a janela principal  
root = Tk()  

# Caminho para o cursor personalizado com o símbolo @  
cursor_imagem = "@imagens/cursores/cursor-cry-x.cur"  # Certifique-se de que o caminho está correto  

# Criar o botão e configurar o cursor  
botao = ttk.Button(root, text='Anything')  
botao.config(cursor=cursor_imagem)  # Definindo o cursor no botão específico  
botao.pack(padx=10, pady=10)  # Adicionando o botão à janela  

# Iniciar o loop da aplicação  
root.mainloop()