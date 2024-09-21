import tkinter as tk
from tkinter import ttk  
from PIL import ImageFont  

class MyDialog(tk.Toplevel):  
    def __init__(self, master, title, details, icon, *, buttons,font=None):  
        super().__init__(master)  
        self.master = master  
        self.title(title)
        self.fonte = font       
        self.font_name = "arial.ttf"   
        self.font_size_title = 30  
        self.font_size_details = 20  
        self.initialize_fonts()  
    
    def initialize_fonts(self):
        """  
        Inicializa as fontes de acordo com a configuração fornecida.     
        Espera-se que `self.fonte` siga uma das duas formas:  

        1. Uma tupla com 3 elementos na seguinte ordem para mudar a fonte e os tamanhos:   
            - `font_name` (str): Nome do arquivo da fonte (ex: "impact.ttf").  
            - `font_size_title` (int): Tamanho da fonte para o título.  
            - `font_size_details` (int): Tamanho da fonte para os detalhes.  

        2. Uma tupla com 2 elementos na seguinte ordem para mudar os tamanhos:  
            - `font_size_title` (int): Tamanho da fonte para o título.  
            - `font_size_details` (int): Tamanho da fonte para os detalhes.  
        
        Se `self.fonte` não for fornecido ou não corresponder a nenhum formato esperado,  
        será usada a fonte padrão "arial.ttf" com os tamanhos de titulo 30 e detalhes 20.  
        """ 

        if self.fonte is not None:  
            # Verifica se a fonte é uma tupla e ajusta conforme necessário  
            if isinstance(self.fonte, tuple):  
                if len(self.fonte) == 3:  # Espera-se que a tupla tenha nome da fonte, tamanho do título, tamanho dos detalhes  
                    self.font_name, self.font_size_title, self.font_size_details = self.fonte  
                elif len(self.fonte) == 2:  # Apenas tamanhos  
                    self.font_size_title, self.font_size_details = self.fonte
                else:    
                    print("Erro: `font` deve ser uma tupla com 3 ou 2 objetos: "  
                        "(nome da fonte, tamanho do título, tamanho dos detalhes).")             
        self.font = ImageFont.truetype(self.font_name, self.font_size_title)  
        self.font2 = ImageFont.truetype(self.font_name, self.font_size_details)
        print(f" Fonte {self.font_name}\n",f"Tamanho titulo {self.font_size_title}\n",f"Tamanho detalhe {self.font_size_details}")                        
 
root = tk.Tk()

font_config = ("arial.ttf", 40, 24)  # Nome da fonte, tamanho do título e tamanho dos detalhes  
dialog = MyDialog(root, "Título Personalizado", "Detalhes", None, buttons=[], font=("impact.ttf", 20,15))   
label = ttk.Label(dialog, text="Minha Casa", font=("arial.ttf", 24))  # Configurando o label  
label.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")  

# Exemplo 2: Mudando apenas os tamanhos  
dialog2 = MyDialog(root, "Título Padrão", "Detalhes padrão", None, buttons=[], font=(25, 15))   
label2 = ttk.Label(dialog2, text="Minha Casa Padrão", font=("arial.ttf", 15))  # Configurando o label  
label2.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

root.mainloop()