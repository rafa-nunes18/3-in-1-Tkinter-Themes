# Autor:

# Rafael A. Nunes (rafa.nunes2018@hotmail.com) 2024

# Inspiração:
# Repositório no GitHub de rdbende chamado, Tema Azure-ttk. 
# https://github.com/rdbende/Azure-ttk-theme
# License: MIT license
# Source: https://github.com/rdbend

# Importar bibliotecas
from TkTema import *
from exemplo_mypopup import chamar_popups
from exemplo_comando_mytoplevel import exemplo_comando
    
# Iniciar instancias
root = MyTema("*****  Meu projeto de Mudar o tema Tkinter  *****")
top = MyTopManager()

# # Modificar o icone de barra
# root.mudar_icone_barra(r"imagens\icons\controle-de-jogo.ico")

#Definir o layout de grade na janela
# Configuração para 3 colunas
for i in range(3): 
    root.columnconfigure(i, weight=1)
# Configuração para 4 linhas
for i in range(4): 
    root.rowconfigure(i, weight=1)

# Create lists for the Comboboxes
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly Combobox", "Item 1", "Item 2"]

# Lista de temas claros  
temas_light = ["sun-valley", "forest", "azure"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar()
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()
variavel_1 = StringVar()  # Set default theme  
checagem_1 = IntVar(value=0)
titulo_1 = "Menu de temas"
temas_light = ["sun","forest","azure"]

# Create a Frame for the Checkbuttons
check_frame = ttk.Labelframe(root, text="Checkbuttons", padding=(20, 10))
check_frame.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Checkbuttons
check_1 = ttk.Checkbutton(check_frame, text="Unchecked", variable=a)
check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
check_2 = ttk.Checkbutton(check_frame, text="Checked", variable=b)
check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
check_3 = ttk.Checkbutton(check_frame, text="Third state", variable=c)
check_3.state(["alternate"])
check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
check_4 = ttk.Checkbutton(check_frame, text="Disabled", state="disabled")
check_4.state(["disabled !alternate"])
check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Separator
separator = ttk.Separator(root)
separator.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="ew")

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="Radiobuttons", padding=(20, 10))
radio_frame.grid(row=3, column=0, padx=(20, 10), pady=10, sticky="nsew")

# Radiobuttons
radio_1 = ttk.Radiobutton(radio_frame, text="Deselected", variable=d, value=1)
radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
radio_2 = ttk.Radiobutton(radio_frame, text="Selected", variable=d, value=2)
radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="Mixed")
radio_3.state(["alternate"])
radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
radio_4 = ttk.Radiobutton(radio_frame, text="Disabled", state="disabled")
radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=1, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Entry
entry = ttk.Entry(widgets_frame)
entry.insert(0, "Entry")
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

# Spinbox
spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100)
spinbox.insert(0, "Spinbox")
spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

# Combobox
combobox = MyCombobox(widgets_frame, values=combo_list)
combobox.auto_complete(combo_list)
combobox.current(0)
combobox.grid(row=2, column=0, padx=5, pady=10,  sticky="ew")

# Read-only Combobox
readonly_combo = MyCombobox(widgets_frame, values=readonly_combo_list)
readonly_combo.current(0)
readonly_combo.grid(row=3, column=0, padx=5, pady=10,  sticky="ew")

# Menu for the Menubutton
menu = tk.Menu(widgets_frame)
menu.add_command(label="Menu item 1")
menu.add_command(label="Menu item 2")
menu.add_separator()
menu.add_command(label="Menu item 3")
menu.add_command(label="Menu item 4")

# Menubutton
menubutton = ttk.Menubutton(widgets_frame, text="Menubutton", menu=menu, direction="below")
menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

# OptionMenu
optionMenu = ttk.OptionMenu(widgets_frame, variavel_1, titulo_1, *temas_light, command=lambda val: root.escolher_tema(checagem_1, variavel_1, label)) 
optionMenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

# Button
button_1 = ttk.Button(widgets_frame, text="Mudar para proximo tema",command = lambda:root.mudar_proximo_tema(variavel_1, label))
button_1.grid(row=6, column=0, padx=5, pady=10, sticky ="nsew")

# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Aperte para testar modo Dark", style="Accent.TButton")
accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")
accentbutton.bind("<Button-1>",lambda e:root.testar_dark(label))
accentbutton.bind("<ButtonRelease-1>",lambda e:root.testar_dark(label))

# Togglebutton
button_2 = ttk.Checkbutton(widgets_frame, text="Togglebutton", style="Toggle.TButton")
button_2.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

# Switch  
switch = ttk.Checkbutton(widgets_frame, text="Ativar modo Dark", variable=checagem_1, onvalue=1, offvalue=0, command=lambda: root.ativar_dark(checagem_1, label), style="Switch.Checkbutton")  
switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

# definindo as configurações de peso de colunas e linhas no toplevel 1
top.set_toplevel_config('toplevel_1', peso_colunas={1: 1},peso_linhas={4:1})

# definindo as informações os widgets ( nomes, posições) 
top.set_widget_options("rotulo1", ttk.Label, 'toplevel_1', text="Esse é o rótulo 1!")
top.set_widget_grid("rotulo1","grid",row=1, column=1,padx=100, pady=10,sticky="nsew",)

top.set_widget_options("botao1", ttk.Button, 'toplevel_1', text="Botão 1", command=lambda:exemplo_comando("Botão 1"))
top.set_widget_grid("botao1", "grid",row=2, column=1,padx=10, pady=10,sticky="nsew",)

top.set_widget_options("botao2", ttk.Button, 'toplevel_1', text="Botão 2", command=lambda:exemplo_comando("Botão 2"))  
top.set_widget_grid("botao2", "grid",row=3, column=1,padx=10, pady=10,sticky="nsew",)
 
# Botão para abrir Toplevel  
button_3 = ttk.Button(widgets_frame, text="Abrir Toplevel 1", command=lambda:top.abrir_mytoplevel(root,"toplevel_1","Nova Janela Personalizada 1"))  
button_3.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")

# definindo as informações os widgets ( nomes, posições) 
top.set_widget_options("rotulo2", ttk.Label, 'toplevel_2', text="Esse é o rótulo 2!")
top.set_widget_grid("rotulo2","grid",row=1, column=1,padx=100, pady=10,sticky="nsew",) 

top.set_widget_options("botao3", ttk.Button, 'toplevel_2', text="Botão 3", command=lambda:exemplo_comando("Botão 3"))
top.set_widget_grid("botao3", "grid",row=2, column=1,padx=10, pady=10,sticky="nsew",)

top.set_widget_options("botao4", ttk.Button, 'toplevel_2', text="Botão 4", command=lambda:exemplo_comando("Botão 4"))  
top.set_widget_grid("botao4", "grid",row=3, column=1,padx=10, pady=10,sticky="nsew",)
 
# Botão para abrir Toplevel  
button_4 = ttk.Button(widgets_frame, text="Abrir Toplevel 2", command=lambda:top.abrir_mytoplevel(root,"toplevel_2","Nova Janela Personalizada 2"))  
button_4.grid(row=11, column=0, padx=5, pady=10, sticky="nsew")

# Panedwindow
paned = ttk.Panedwindow(root)
paned.grid(row=1, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", width=120)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)

# Treeview headings
treeview.heading("#0", text="Column 1", anchor="center")
treeview.heading(1, text="Column 2", anchor="center")
treeview.heading(2, text="Column 3", anchor="center")

# Define Treeview data
treeview_data = [
    ("", "end", 1, "Parent", ("Item 1", "Value 1")),
    (1, "end", 2, "Child", ("Subitem 1.1", "Value 1.1")),
    (1, "end", 3, "Child", ("Subitem 1.2", "Value 1.2")),
    (1, "end", 4, "Child", ("Subitem 1.3", "Value 1.3")),
    (1, "end", 5, "Child", ("Subitem 1.4", "Value 1.4")),
    ("", "end", 6, "Parent", ("Item 2", "Value 2")),
    (6, "end", 7, "Child", ("Subitem 2.1", "Value 2.1")),
    (6, "end", 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
    (8, "end", 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
    (8, "end", 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
    (8, "end", 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
    (6, "end", 12, "Child", ("Subitem 2.3", "Value 2.3")),
    (6, "end", 13, "Child", ("Subitem 2.4", "Value 2.4")),
    ("", "end", 14, "Parent", ("Item 3", "Value 3")),
    (14, "end", 15, "Child", ("Subitem 3.1", "Value 3.1")),
    (14, "end", 16, "Child", ("Subitem 3.2", "Value 3.2")),
    (14, "end", 17, "Child", ("Subitem 3.3", "Value 3.3")),
    (14, "end", 18, "Child", ("Subitem 3.4", "Value 3.4")),
    ("", "end", 19, "Parent", ("Item 4", "Value 4")),
    (19, "end", 20, "Child", ("Subitem 4.1", "Value 4.1")),
    (19, "end", 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
    (21, "end", 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
    (21, "end", 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
    (21, "end", 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
    (19, "end", 25, "Child", ("Subitem 4.3", "Value 4.3"))
    ]

# Insert Treeview data
for item in treeview_data:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    if item[0] == "" or item[2] in (8, 12):
        treeview.item(item[2], open=True) # Open parents

# Select and scroll
treeview.selection_set(10)
treeview.see(7)

# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Notebook
notebook = ttk.Notebook(pane_2)

# Tab #1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)
notebook.add(tab_1, text="Tab 1")

# Scale
scale = ttk.Scale(tab_1, from_=100, to=0, variable=g, command=lambda event: g.set(scale.get()))
scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

# Progressbar
progress = ttk.Progressbar(tab_1, value=0, variable=g, mode="determinate")
progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

# Botão para abrir todos os Popups
button_5 = ttk.Button(tab_1, text="Abrir Popups",command = lambda:chamar_popups(root))
button_5.grid(row=1, column=0, padx=10, pady=10, sticky ="ew")

# Label
label = ttk.Label(tab_1, text="", justify="center")
label.grid(row=1, column=1, pady=10, columnspan=2)

# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")    

# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")
notebook.pack(expand=True, fill="both", padx=5, pady=5)

# icone para arrastar janela
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=3, padx=(5, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.centralizar_janela()
root.mainloop()