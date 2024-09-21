import tkinter as tk  
from PIL import Image, ImageTk  

# Função para definir o ícone da janela  
def set_window_icon(window, image_path):  
    # Abre a imagem  
    img = Image.open(image_path)  
    # Redimensiona a imagem para 32x32 pixels  
    img = img.resize((32, 32), Image.LANCZOS)  # Usando LANCZOS para redimensionamento  
    # Converte a imagem para um formato que o Tkinter pode usar  
    icon = ImageTk.PhotoImage(img)  
    # Define o ícone da janela  
    window.iconphoto(False, icon)  
    return icon  # Retorna o ícone para evitar que seja coletado pelo garbage collector  

# Cria a janela principal  
root = tk.Tk()  
root.title("Janela com Ícone Bitmap")  

# Define o tamanho da janela  
root.geometry("300x200")  

# Define o caminho da imagem que será usada como ícone  
image_path = "imagens/icons/icone-padrao.ico"  # Substitua pelo caminho correto da sua imagem  

# Define o ícone da janela  
icon = set_window_icon(root, image_path)  

# Adiciona um rótulo à janela  
label = tk.Label(root, text="Esta é uma janela com ícone bitmap!")  
label.pack(pady=20)  

# Inicia o loop principal da interface  
root.mainloop()