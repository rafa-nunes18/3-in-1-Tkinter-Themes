# Autor:

# Rafael A. Nunes (rafa.nunes2018@hotmail.com) 2024

# Inspiração:
# Repositório no GitHub de rdbende chamado, Tema Azure-ttk. 
# https://github.com/rdbende/Azure-ttk-theme
# License: MIT license
# Source: https://github.com/rdbend


from TkTema import *
from exemplo_mypopup import chamar_popups
from exemplo_comando_mytoplevel import exemplo_comando

# Iniciar instancias
root = MyTema("Meu App")
top = MyTopManager()

# # Modificar o icone de barra
# root.mudar_icone_barra(r"imagens\icons\controle-de-jogo.ico")

# Definir o layout de grade na janela
for i in range(2): 
    root.columnconfigure(i, weight=1)         

# Controle de variáveis
variavel_1 = StringVar() 
checagem_1 = IntVar(value=0)
titulo_1 = "Menu temas"
temas_light = ["sun-valley","forest","azure"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly Combobox", "Item 1", "Item 2"]
texto = "Mude o tema!"

# Frame para Menu e Comboboxs
frame1 = ttk.LabelFrame(root,text= "Menu e Comboboxs",)
frame1.grid(row=1, column=0, padx=5, pady=(30,10))

# Menu do Menubutton
menu = tk.Menu(frame1)
menu.add_command(label="Menu item 1")
menu.add_command(label="Menu item 2")
menu.add_separator()
menu.add_command(label="Menu item 3")
menu.add_command(label="Menu item 4")           

# Menubutton
menubutton = ttk.Menubutton(frame1, text="Menubutton", menu=menu, direction="below")
menubutton.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

# Combobox
combobox = MyCombobox(frame1, values=combo_list)
combobox.auto_complete(combo_list)
combobox.current(0)
combobox.grid(row=2, column=0, padx=5, pady=10,  sticky="nsew")

# Read-only Combobox
readonly_combo = MyCombobox(frame1, values=readonly_combo_list,state='readonly')
readonly_combo.current(0)
readonly_combo.grid(row=3, column=0, padx=5, pady=10,  sticky="nsew")

# Create a Frame for input widgets
frame2 = ttk.LabelFrame(root,text='Botões de mudar o tema')
frame2.grid(row=2, column=0,columnspan=2, padx=(10,0), pady=(5, 10), sticky="ew")
frame2.columnconfigure(index=0, weight=1)

# OptionMenu
optionMenu = ttk.OptionMenu(frame2, variavel_1, titulo_1, *temas_light, command=lambda val: root.escolher_tema(checagem_1, variavel_1, label)) 
optionMenu.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
                
# Button
button1 = ttk.Button(frame2, text="Mudar para proximo tema",command = lambda: root.mudar_proximo_tema(variavel_1, label))
button1.grid(row=1, column=0, padx=5, pady=10, sticky ="nsew")

# Accentbutton
accentbutton = ttk.Button(frame2, text="Aperte para testar modo Dark", style="Accent.TButton")
accentbutton.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
accentbutton.bind("<Button-1>",lambda e:root.testar_dark(label))
accentbutton.bind("<ButtonRelease-1>",lambda e:root.testar_dark(label))

# Switch 
switch = ttk.Checkbutton(frame2, text="Ativar o modo Dark", variable=checagem_1, onvalue=1, offvalue=0, command=lambda: root.ativar_dark(checagem_1, label), style="Switch.Checkbutton")  
switch.grid(row=3, column=0, padx=5, pady=10, sticky="ns")

# Frame para Popups e Toplevels
frame3 = ttk.LabelFrame(root,text= "Popups e Toplevels")
frame3.grid(row=1, column=1, padx=(0,0), pady=(30,10), sticky="ew")
frame3.columnconfigure(index=0, weight=1)

# Botão 
botao_2 = ttk.Button(frame3, text="Abrir popups",command=lambda:chamar_popups(root))
botao_2.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

# definindo as configurações de peso de colunas e linhas no toplevel 
top.set_toplevel_config('toplevel_1', peso_colunas={1: 1},peso_linhas={4:1})

# definindo as informações os widgets ( nomes, posições) 
top.set_widget_options("rotulo1", ttk.Label, 'toplevel_1', text="Esse é o rótulo 1!")
top.set_widget_grid("rotulo1","grid",row=1, column=1,padx=100, pady=10,sticky="nsew") 

top.set_widget_options("botao1", ttk.Button, 'toplevel_1', text="Botão 1", command=lambda:exemplo_comando("Botão 1"))
top.set_widget_grid("botao1", "grid",row=2, column=1,padx=10, pady=10,sticky="nsew")

top.set_widget_options("botao2", ttk.Button, 'toplevel_1', text="Botão 2", command=lambda:exemplo_comando("Botão 2"))  
top.set_widget_grid("botao2", "grid",row=3, column=1,padx=10, pady=10,sticky="nsew")
 
# Botão para abrir Toplevel  
button_3 = ttk.Button(frame3, text="Abrir Toplevel 1", command=lambda:top.abrir_mytoplevel(root,"toplevel_1","Nova Janela Personalizada 1"))  
button_3.grid(row=1, column=0, padx=5, pady=7, sticky="nsew")

# definindo as informações os widgets ( nomes, posições) 
top.set_widget_options("rotulo2", ttk.Label, 'toplevel_2', text="Esse é o rótulo 2!")
top.set_widget_grid("rotulo2","grid",row=1, column=1,padx=100, pady=10,sticky="nsew",) 

top.set_widget_options("botao3", ttk.Button, 'toplevel_2', text="Botão 3", command=lambda:exemplo_comando("Botão 3"))
top.set_widget_grid("botao3", "grid",row=2, column=1,padx=10, pady=10,sticky="nsew",)

top.set_widget_options("botao4", ttk.Button, 'toplevel_2', text="Botão 4", command=lambda:exemplo_comando("Botão 4"))  
top.set_widget_grid("botao4", "grid",row=3, column=1,padx=10, pady=10,sticky="nsew",)
 
# Botão para abrir Toplevel  
button_4 = ttk.Button(frame3, text="Abrir Toplevel 2", command=lambda:top.abrir_mytoplevel(root,"toplevel_2","Nova Janela Personalizada 2"))  
button_4.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

# Label
label = ttk.Label(root, text=texto, justify="center")
label.grid(row=3, column=0, columnspan=2 ,padx=150, pady=(0,10))

# Ícone para arrastar janela
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=3, column=3, padx=(5, 5))

# update and loop 
root.update()
root.mainloop()
