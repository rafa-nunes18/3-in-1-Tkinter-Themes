# Iniciar importações
from TkTema import *
from pynput import mouse


def create_image(width, height):  
    icon_path = "imagens/icons/icone-padrao.ico"  # Substitua pelo caminho do seu ícone  
    image = Image.open(icon_path)  
    return image  

def on_quit(icon, item):  
    icon.stop()  
    root.destroy()  

def show_window():  
    root.deiconify()  # Mostra a janela  

# Cria a janela Tkinter   
root = MyTema("Meu App")  

# Definir o layout de grade na janela  
for i in range(2):   
    root.columnconfigure(i, weight=1)          

# Cria o ícone  
icon = Icon("test_icon", create_image(64, 64), "Meu App", menu=pystray.Menu(  
    MenuItem("Show", show_window),  
    MenuItem("Quit", on_quit)  
))  

# Função chamada ao clicar no ícone  
def on_icon_click(icon, item):  
    show_window()  # Mostra a janela ao clicar no ícone  

# Adiciona a função de clique ao menu  
icon.menu = pystray.Menu(  
    MenuItem("Show", show_window),  
    MenuItem("Quit", on_quit)  
)  

# Inicia o ícone em uma thread separada  
def run_icon():  
    icon.run()
    show_window()   

# Start the icon in a separate thread  
import threading  
thread = threading.Thread(target=run_icon, daemon=True)  
thread.start()  

# Inicia a janela  
root.mainloop()