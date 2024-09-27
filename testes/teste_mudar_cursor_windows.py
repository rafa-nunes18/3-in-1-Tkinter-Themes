import ctypes  
import tkinter as tk  
from tkinter import messagebox 

# Defina aqui o caminho para o arquivo do cursor .cur  
CURSOR_PATH = "imagens/cursores/cursor-forest.cur"

# Mudar o cursor global  
def set_cursor(cursor_path):
    if cursor_path:
        cursor_handle = ctypes.windll.user32.LoadCursorFromFileW(cursor_path)   
        ctypes.windll.user32.SetSystemCursor(cursor_handle, 32512)  # 32512 é o ID do cursor de flecha
        messagebox.showinfo("Sucesso", "Cursor alterado com sucesso.")
    else:
        messagebox.showerror("Erro", "Não foi possível carregar o cursor.")    

# Restaura o cursor padrão global  
def restore_default_cursor():  
    # O cursor padrão pode não ser restaurado como esperado; vamos usar um método alternativo para garantir  
    ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0)
    messagebox.showinfo("Sucesso", "Cursor restaurado com sucesso.")


def set_custom_cursor():   
    custom_cursor = ctypes.windll.user32.LoadCursorFromFileW(CURSOR_PATH)  
    if not custom_cursor:  
        raise Exception("Falha ao carregar o cursor do arquivo.")  
    
    ctypes.windll.user32.SetSystemCursor(custom_cursor, 32512)  
    print("Cursor personalizado definido...")  

def reset_cursor_to_original():    
    ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0)  
    print("Redefinido para o cursor padrão do Windows...")  

def on_leave(event):  
    print("Cursor saiu do widget!")  
    reset_cursor_to_original()  

def remove_leave_binding(frame):  
    frame.unbind("<Enter>") 
    frame.unbind("<Leave>") 
    print("Binding eventos removidos.")

class App:  
    def __init__(self, master):  
        self.master = master  

        # Criar um frame onde o evento <Leave> será detectado  
        self.frame = tk.Frame(root, width=300, height=200, bg="lightblue")  
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew") 

        # Definir funções para mouse entrar e sair do frame  
        self.frame.bind("<Enter>", lambda e: set_custom_cursor())  # Quando o mouse entra, define o cursor  
        self.frame.bind("<Leave>", on_leave)  # Quando o mouse sai, chama a função on_leave  

        # Botão para remover o binding do evento <Leave>  
        self.remove_binding_button = tk.Button(root, text="Remover Binding <Leave>", command=lambda:remove_leave_binding(self.frame))  
        self.remove_binding_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  

        # Botão para mudar o cursor  
        self.mudar_cursor_btn = tk.Button(master, text="Mudar Cursor", command=lambda:set_cursor(CURSOR_PATH))  
        self.mudar_cursor_btn.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")   

        # Botão para restaurar o cursor padrão  
        self.restaurar_cursor_btn = tk.Button(master, text="Restaurar Cursor para Padrão", command=restore_default_cursor)  
        self.restaurar_cursor_btn.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")              

   
if __name__ == "__main__":  
    root = tk.Tk()
    root.title("Exemplo de Cursor em Tkinter")  
    root.geometry("320x360")   
    app = App(root)  
    root.mainloop()