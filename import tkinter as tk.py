import tkinter as tk  

def main():  
    # Criar a janela principal  
    root = tk.Tk()  
    root.title("Exemplo de Toplevel com Grid")  

    # Criar o Toplevel  
    top = tk.Toplevel(root)  
    top.title("Toplevel com Frame e Botões")  

    # Criar o Frame  
    frame = tk.Frame(top)  
    frame.grid(row=0, column=0, padx=10, pady=10)  

    # Criar 3 botões dentro do Frame  
    button1 = tk.Button(frame, text="Botão 1")  
    button1.grid(row=0, column=0, padx=5, pady=5)  

    button2 = tk.Button(frame, text="Botão 2")  
    button2.grid(row=0, column=1, padx=5, pady=5)  

    button3 = tk.Button(frame, text="Botão 3")  
    button3.grid(row=0, column=2, padx=5, pady=5)  

    # Criar um botão abaixo do Frame  
    button4 = tk.Button(top, text="Botão Abaixo do Frame")  
    button4.grid(row=1, column=0, padx=10, pady=10)  

    # Criar um segundo Frame abaixo do botão  
    frame2 = tk.Frame(top)  
    frame2.grid(row=2, column=0, padx=10, pady=10)  

    # Criar um botão dentro do segundo Frame  
    button5 = tk.Button(frame2, text="Botão no Segundo Frame")  
    button5.grid(row=0, column=0, padx=5, pady=5)  

    # Iniciar o loop principal  
    root.mainloop()  

if __name__ == "__main__":  
    main()