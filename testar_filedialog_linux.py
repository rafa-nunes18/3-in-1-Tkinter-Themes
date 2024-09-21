 
from tkinter import filedialog  
from TkTema import *
# Função para abrir a caixa de diálogo  
def abrir_caixa_dialogo():  
    # Essa função abre a caixa de diálogo para seleção de arquivos  
    arquivo_selecionado = filedialog.askopenfilename(title="Selecione um arquivo")  
    
    if arquivo_selecionado:  
        print(f"Arquivo selecionado: {arquivo_selecionado}")  

# Inicializa a aplicação tkinter  
root = MyTema("Meu App")
root.set_tema("forest-dark")
# Cria um botão para abrir a caixa de diálogo  
botao_abre_dialogo = ttk.Button(root, text="Abrir Caixa de Diálogo", command=abrir_caixa_dialogo)  
botao_abre_dialogo.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

# Inicia o loop principal  
root.mainloop()