# Importar bibliotecas
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk ,ImageGrab  
import sys
import os
import Dicionarios_Mytema as dicio 

if sys.platform == "win32":
    from ctypes import windll
elif sys.platform == "darwin":
    import AppKit
    from AppKit import NSImage, NSCursor, NSSize
    from pynput import mouse
    import Quartz  
elif sys.platform.startswith("linux"): 
    import tkXcursor as tx 
    from IconLinux import MyIcon  


class MyTema(tk.Tk):

        
    def __init__(self,title, *args, **kwargs):  
        super().__init__(*args, **kwargs)                                       
        self.titulo = title                       
        self.menus = []
        self.tema = None        
        self.estilo = ttk.Style()       
        self.mycombo = MyCombobox(self)
        if sys.platform == "win32":
            self.icone_padrao = r"imagens\icons\icone-padrao64.ico"    
        else:    
            self.icone_padrao = r"imagens/icons/icone-padrao.ico"   
        self.cursor_padrao = "arrow" 
        self.maximized = False  
        self.minimized = False  
        self.normal_size = self.geometry()
        self.mybar1 = MyBar(self)      
        self.default_tema_config()     
                     
    def default_tema_config(self):                
        self.option_add("*tearOff", False)
        self.overrideredirect(True)        
        self.centralizar_janela()      
        self.criar_temas()
        self.ativar_tema()           
        self.mudar_titulo(self.titulo) 
        self.focus_force()                 
        if sys.platform == "win32":
            self.ativar_tema_transparencia()
            self.manter_icone()
            self.iconbitmap(self.icone_padrao)
        elif sys.platform == "darwin":
            self.cursor_mac_ativo = False
            self.overrideredirect(False)
            self.menus_button= []
            self.loc = Quartz.CGEventGetLocation                    
            MacAPIManager.hide_window_buttons(self)
            self.set_icon_mac()
            AppKit.NSApplication.sharedApplication()                                              
        elif sys.platform.startswith("linux"):
            self.menus_button= []
            self.screenshot_path = "tema_screenshot.png"
            self.criar_atalho_linux()           
            self.master_linux = True

    def set_icon_mac(self):
        image = Image.open(self.icone_padrao)  
        icon = image.resize((64, 64), Image.LANCZOS) 
        icon_mac = ImageTk.PhotoImage(icon)
        self.iconphoto(False, icon_mac)
    
    def set_tema(self,tema):
        temas = ["azure-light", "azure-dark", "forest-light",
                "forest-dark", "sun-valley-light", "sun-valley-dark"
                ]
        if tema in temas:
            self.tema = tema
        else:
            print("Escolha um tema entre : ", temas) 

    def capture_master_window(self):  
        # Captura a janela master e salva como imagem
        if not self.minimized:  
            x = self.winfo_rootx()  
            y = self.winfo_rooty()  
            width = self.winfo_width()  
            height = self.winfo_height()  
            ImageGrab.grab(bbox=(x, y, x + width, y + height)).save(self.screenshot_path)
    
    def deletar_print(self):        
        if os.path.exists(self.screenshot_path) and self.minimized:  
            os.remove(self.screenshot_path)
    
    def mudar_titulo(self,titulo):  
        self.title(titulo)
        if not sys.platform == "darwin":        
            self.mybar1.titulo_barra.config(text=titulo)

    def mudar_cursores(self,tema):
        if sys.platform == "win32":
            if tema in dicio.cursores_windows:            
                cursor = dicio.cursores_windows[tema]
                self.cursor_padrao = cursor
                MyTema.mudar_cursor(self,cursor)          
            else:
                self.cursor_padrao = "arrow"
                MyTema.mudar_cursor(self,self.cursor_padrao)
        elif sys.platform == "darwin":
            if tema in dicio.cursores_mac:            
                cursor = dicio.cursores_mac[tema]
                self.cursor_padrao = cursor               
                MyTema.mudar_cursor(self,cursor)                         
            else:
                self.cursor_padrao = "arrow"
                MyTema.mudar_cursor(self,self.cursor_padrao)      
        elif sys.platform.startswith("linux"):
            self.cursor_padrao = "arrow"
            MyTema.mudar_cursor(self,self.cursor_padrao) 
            if tema in dicio.cursores_windows:
                cursor = dicio.cursores_linux[tema]
                self.cursor_padrao = cursor           
                MyTema.mudar_cursor_linux(self,cursor)
            
    def criar_atalho_linux(self):                                
        self.ico = MyIcon(self)
        self.ico.iniciar()

    @staticmethod
    def mudar_cursor(janela,cursor):
        janela.config(cursor=cursor)
        for child in janela.winfo_children():  
                child.config(cursor=cursor) 

    @staticmethod  
    def mudar_cursor_linux(janela, cursor):         
        cursor_linux = tx.x_load_cursor(janela, cursor)  
        tx.x_set_cursor(janela, cursor_linux)
        for child in janela.winfo_children():          
            id = child.winfo_id()  
            try:   
                cursor_linux = tx.x_load_cursor(child, cursor)  
                tx.x_set_cursor(child, cursor_linux)  
            except Exception as e:  
                print(f"Erro ao colocar o cursor no child {child} (ID: {id}), erro: {e}")                   

    def mudar_icone_barra(self,imagem):       
            self.mybar1.mudar_icone(imagem)            
            self.icone_padrao = imagem
            if sys.platform == "win32":
                self.iconbitmap(imagem)
            elif sys.platform == "darwin":
                self.set_icon_mac()
            elif sys.platform.startswith("linux"):
                self.ico.mudar_icone_linux(imagem)                              

    def manter_icone(self):         
            try:                       
                WindowsAPIManager.manter_icone_bar_windows(self) 
            except Exception as e:   
                print(f"Erro ao manter icone na barra de tarefas em {self}: {e}")

    def ativar_tema_transparencia(self):        
            cor_transparente = "#3af30c"
            try:
                self.wm_attributes("-transparentcolor", cor_transparente)            
            except Exception as e:   
                print(f"Erro ao ativar transparencia (class MyTema): {e}")
  
    def buscar_botoes_menu(self):
        def buscar_recursivo(widget):             
            if isinstance(widget, (ttk.Menubutton,ttk.OptionMenu)):  
                self.menus_button.append(widget)            
            for child in widget.winfo_children():  
                buscar_recursivo(child)
        buscar_recursivo(self)
        
    def enter_button_menu_mac(self, event):       
        tema = ttk.Style().theme_use()
        if tema in dicio.cursores_mac:
            self.cursor_mac_os = dicio.cursores_mac[tema].replace("@","")                 
            self.after(50, MacAPIManager.set_custom_cursor,self.cursor_mac_os) 

    def enter_button_menu_linux(self,event):
        self.after(50, self.set_all_menu_cursor_linux)
            

    def set_all_buttons_menu(self):
        for button in self.menus_button:
            if sys.platform == "darwin":                
                button.bind("<Button-1>",self.enter_button_menu_mac)
                button.bind("<ButtonRelease-1>",self.enter_button_menu_mac)
            elif sys.platform.startswith("linux"):
                button.bind("<Button-1>",self.enter_button_menu_linux)

    def set_all_menu_cursor_linux(self):        
        for menu in self.menus:
            tema = ttk.Style().theme_use()
            if tema in dicio.cursores_mac:          
                MyTema.mudar_cursor_linux(menu,self.cursor_padrao)
            else:
                MyTema.mudar_cursor(menu,self.cursor_padrao)         

    def mainloop(self, *args, **kwargs):
        if sys.platform == "win32" :            
            self.buscar_menus()
        elif sys.platform == "darwin": 
            self.buscar_botoes_menu()
            self.set_all_buttons_menu()                          
        elif sys.platform.startswith("linux"):
            self.buscar_botoes_menu()
            self.buscar_menus_linux()
            self.set_all_buttons_menu()         
        self.ativar_tema() 
        super().mainloop(*args, **kwargs)             
   
    def criar_temas(self):        
        caminho = os.getcwd()
        pasta_temas = os.path.join(caminho, 'temas')
        lista_temas = [file for file in os.listdir(pasta_temas) if file.endswith('.tcl')]     
        for tema in lista_temas:
            caminho_tema = os.path.join(pasta_temas, tema)          
            self.call('source', caminho_tema)        

    def ativar_tema(self): 
        if self.tema == None:
            tema='sun-valley-light'
        else:
            tema = self.tema     
        self.estilo.theme_use(tema)  
        self.mudar_cor_fundo(tema)  
        self.atualizar_widgets(tema)
        self.mudar_cursores(tema)  

    def mudar_proximo_tema(self,variavel_1,label):
        lista_temas_light = ["sun-valley","forest","azure"] 
        tema_atual = self.estilo.theme_use()
        tema = tema_atual.replace("-light", "").replace("-dark", "")   
        current_index = lista_temas_light.index(tema)  
        next_index = (current_index + 1) % len(lista_temas_light)  
        proximo_tema = lista_temas_light[next_index]  
        sufixo = "-dark" if tema_atual.endswith("dark") else "-light"  
        tema = proximo_tema + sufixo         
        self.atualizar_menu_temas(proximo_tema, variavel_1)  
        self.atualizar_cores_e_texto(tema, label)     

    def escolher_tema(self, checagem_1, variavel_1, label):  
        tema = f"{variavel_1.get()}{'-light' if checagem_1.get() == 0 else '-dark'}"  
        self.atualizar_cores_e_texto(tema, label)  

    def testar_dark(self,label):
        tema= self.estilo.theme_use()
        novo_tema = tema.replace("light", "dark") if "light" in tema else tema.replace("dark", "light")  
        self.atualizar_cores_e_texto(novo_tema, label)                                   

    def ativar_dark(self, checagem_1,label):  
        tema = self.estilo.theme_use()
        novo_tema = tema.replace("light", "dark") if checagem_1.get() == 1 else tema.replace("dark", "light")                 
        self.atualizar_cores_e_texto(novo_tema,label)                          

    def ativar_modo_dark_mac(self,tema):
        modo = "dark" if tema.endswith("dark") else "light"
        MacAPIManager.set_window_appearance(self,modo)

    def mudar_cor_fundo(self, tema):          
        if str(tema).endswith('dark'):             
            bg_color = self.estilo.lookup(ttk.Labelframe, 'background')  
        else:            
            bg_color = self.estilo.lookup(tema, 'background')       
        self.configure(bg=bg_color) 
 
    def buscar_menus(self):        
        def buscar_recursivo(widget):             
            if isinstance(widget, tk.Menu):  
                self.menus.append(widget)            
            for child in widget.winfo_children():  
                buscar_recursivo(child)
        buscar_recursivo(self)

    def buscar_menus_linux(self, parent=None):  
        if parent is None:  
            parent = self
        if isinstance(parent, (tk.Tk, tk.Toplevel)):  
            menu = parent.config().get('menu')  
            if isinstance(menu, tk.Menu):  
                self.menus.append(menu)
        for child in parent.winfo_children():
            if isinstance(child, tk.Menubutton):  
                menu = child['menu']  
                if isinstance(menu, tk.Menu): 
                    self.menus.append(menu)           
            elif isinstance(child, tk.Menu):
                menu = child
                self.menus.append(menu)
            self.buscar_menus_linux(child)            
    
    def update_menubutton_styles(self, **kwargs):        
        for menu in self.menus:         
            menu.config(**kwargs)                    

    def atualizar_widgets(self, tema):  
        if tema in dicio.cores_temas: 
            cor = dicio.cores_temas[tema]
            # Atualiza as cores do menu em MenuButton  
            self.update_menubutton_styles(  
                    bg=cor['bg'],  
                    fg=cor['fg'],  
                    activebackground=cor['activebg'],  
                    activeforeground=cor['activefg']  
                )             
                
            # Atualiza as cores do Combobox
            self.mycombo.update_combobox_styles(  
                    bg=cor['bg'],  
                    fg=cor['fg'],  
                    highlightcolor=cor['highlightcolor'],  
                    selectbackground=cor['selectbackground']  
                )
            
            # Atualiza os estilos da barra  
            self.mybar1.titulo_barra.configure(  
                background=cor['bg'],  
                foreground=cor['fg']  
            )  
            self.mybar1.icone_barra.configure(  
                background=cor['bg']  
            )  
        else:  
            print(f"Tema {tema} não encontrado em dicio.cores_temas.")    

    def atualizar_menu_temas(self,tema,variavel_1):
        variavel_1.set(tema)
    
    def atualizar_texto(self,tema,label):          
        texto = f"Tema atualizado para: {tema}"  
        label.config(text=texto)

    def atualizar_cores_e_texto(self,tema,label):
        self.estilo.theme_use(tema)
        self.atualizar_texto(tema,label)
        self.mudar_cor_fundo(tema)
        self.atualizar_widgets(tema)
        self.mudar_cursores(tema)
        if sys.platform == "darwin":
            self.ativar_modo_dark_mac(tema)                             

    def centralizar_janela(self):
        self.minsize(self.winfo_width(), self.winfo_height())
        x_cordinate = int((self.winfo_screenwidth()/2) - (self.winfo_width()/2))
        y_cordinate = int((self.winfo_screenheight()/2) - (self.winfo_height()/2))
        self.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    
class MyCombobox(ttk.Combobox):
    instances = []
   
    def __init__(self, master=None, **kwargs):  
        self.readonly_status = kwargs.pop('status', False)  
        super().__init__(master, **kwargs)  
        MyCombobox.instances.append(self)  
        self.options = list(self['values'])  
        self.filtered_options = []  
        self.configure(state='readonly' if self.readonly_status else 'normal')  
        self.ativar_auto_complete()
        self.default_popdown_config()  
       
    def default_popdown_config(self):  
        self.config_popdown( justify= "center", relief= "flat",bg= "white", fg= 'black',
                             highlightthickness= 1, highlightcolor= "#737373",  
                             selectbackground= "#0560b6", selectforeground= "white"  
        )                                

    def config_popdown(self, **kwargs):            
        options_str_list = []  
        for key, value in kwargs.items():  
            options_str_list.append(f"-{key} {value}")  
        options_str = ' '.join(options_str_list)  
        self.tk.eval('[ttk::combobox::PopdownWindow {}].f.l configure {}'.format(self, options_str))    
     
    def update_combobox_styles(self, **kwargs):  
        for combobox in self.__class__.instances:  
            combobox.config_popdown(**kwargs)
      
    def auto_complete(self, completion_list):  
        self.options = sorted(completion_list)  
        self['values'] = self.options  

    def show_all_values(self, event):         
        self['values'] = self.options   
        self.set('')  

    def on_keyrelease(self, event):  
        if event.keysym == 'Return':  
            if self.get() in self.options:  
                self.set(self.get())  
                return  
        
        if event.keysym in ['BackSpace', 'Left', 'Right', 'Up', 'Down']:  
            return  

        typed = self.get()  
        if typed:  
            self.filtered_options = [option for option in self.options if option.lower().startswith(typed.lower())]  
            if self.filtered_options:  
                self['values'] = self.filtered_options  
                self.current(0)  
                self.event_generate('<Down>')  
            else:  
                self['values'] = []  
        else:  
            self['values'] = self.options  

    def on_selection(self, event):  
        selected_value = self.get()  
        if selected_value in self.options:  
            self.set(selected_value)
   
    def ativar_auto_complete(self):  
        if not self.readonly_status:  
            self.bind('<KeyRelease>', self.on_keyrelease)  
            self.bind('<Button-1>', self.show_all_values)  
            self.bind('<<ComboboxSelected>>', self.on_selection)                 


class MyBar(tk.Frame):

    def __init__(self,master, *args, **kwargs):
        super().__init__(master,*args, **kwargs)        
        self.master = master
        self.icone_padrao = master.icone_padrao
        self.titulo = master.titulo
        self.cursor_botao_x = "@imagens/cursores/cursor-cry-x.cur"                                    
        self.default_mybar_config()            

    def default_mybar_config(self):
        self.nova_barra = ttk.Frame(self.master,style="Card.TFrame")  
        self.nova_barra.grid(row=0, column=0, sticky="ew",columnspan=5)             

        self.nova_barra.grid_columnconfigure(0, weight=0)  # Coluna do ícone  
        self.nova_barra.grid_columnconfigure(1, weight=1)  # Coluna do título expande  
        self.nova_barra.grid_columnconfigure(2, minsize=30)  # Botão de minimizar  
        self.nova_barra.grid_columnconfigure(3, minsize=30)  # Botão de maximizar  
        self.nova_barra.grid_columnconfigure(4, minsize=30)  # Botão de fechar

        self.icone_imagem = MyBar.criar_icone(self.icone_padrao)
        self.icone_barra = ttk.Label(self.nova_barra,image=self.icone_imagem)  
        self.icone_barra.grid(row=0, column=0, padx=(5, 0),sticky="w")  
        self.icon = self.icone_imagem
        
        # Adiciona um título à barra  
        self.titulo_barra = ttk.Label(self.nova_barra, text=self.titulo ,style="Titulo.TLabel")  
        self.titulo_barra.grid(row=0, column=1) 
               
         # Botão para minimizar a janela  
        self.minimize_button = ttk.Button(self.nova_barra, text="🗕")  
        self.minimize_button.grid(row=0, column=2, sticky="e")  

        # Botão para maximizar/restaurar a janela  
        self.maximize_button = ttk.Button(self.nova_barra, text="🗖", command=self.maximize_window)  
        self.maximize_button.grid(row=0, column=3, sticky="e")   

        # Botão para fechar a janela  
        self.botao_fechar = ttk.Button(self.nova_barra, text=" X ", command=self.master.destroy)  
        self.botao_fechar.grid(row=0, column=4, sticky="e")

        if sys.platform == "win32":
            self.minimize_button.config(command=self.minimize_windows)
            self.botao_fechar.config(cursor=self.cursor_botao_x,
                                     style="Redbutton.TButton",
                                     command=self.master.destroy
                                     )
            self.nova_barra.config(style="Dialog_buttons.TFrame")       
            self.master.bind("<FocusIn>",self.deminimize)
            self.master.bind("<FocusOut>",self.focus_out)
        elif sys.platform == "darwin":
            self.minimize_button.config(text="_", command=self.minimize_mac)
            self.cursor_botao_x = "@imagens/cursores/cursores-mac/cursor-cry-x32.cur"
            self.titulo_barra.config(text='',style=None)
            self.botao_fechar.config(cursor=self.cursor_botao_x, style="Redbuttonlinux.TButton")
            self.maximize_button.config(text="▢")                
        elif sys.platform.startswith("linux"):
            self.minimize_button.config(command=self.minimeze_linux)
            self.botao_fechar.config(command=self.fechar_linux,style="Redbuttonlinux.TButton")
            self.mudar_cursor_fechar_linux()        
        
        self.apply_drag_events(self.nova_barra)  
        self.apply_drag_events(self.titulo_barra)              

    def minimize_mac(self):
        self.master.iconify()

    def mudar_cursor_fechar_linux(self):
        cursor_path = "imagens/cursores/cursores-linux/cursor-cry-x25"
        xcursor = tx.x_load_cursor(self.botao_fechar, cursor_path)

        def my_set_cursor(event):
            self.botao_fechar.config(cursor="arrow")   
            tx.x_set_cursor(self.botao_fechar,xcursor)

        def reset_cursor(event):
            tema = ttk.Style().theme_use()
            MyTema.mudar_cursor(self.master,"arrow") 
            if tema in dicio.cursores_windows:
                cursor = dicio.cursores_linux[tema]
                self.master.cursor_padrao = cursor           
                MyTema.mudar_cursor_linux(self.master,cursor)                   

        self.botao_fechar.bind('<Enter>', my_set_cursor)  
        self.botao_fechar.bind('<Leave>', reset_cursor) 

    def focus_out(self,event=None):
        self.minimize_windows

    def apply_drag_events(self, widget):  
        widget.bind("<B1-Motion>", self.move_window)  
        widget.bind("<ButtonPress-1>", self.start_move)

    def start_move(self, event):
        # Define offset para o movimento  
        self.offset_x = event.x  
        self.offset_y = event.y  

    def move_window(self, event):  
        # Move a janela com base nas coordenadas do mouse  
        x = self.master.winfo_x() - self.offset_x + event.x  
        y = self.master.winfo_y() - self.offset_y + event.y  
        self.master.geometry(f"+{x}+{y}")  

    def fechar_linux(self):        
        self.master.ico.stop()
        for child in self.master.winfo_children():
            if hasattr(child, 'ico'):  
                child.ico.stop()
            if hasattr(child, 'screenshot_path'): 
                child.deletar_print()     
            child.destroy() 
        self.master.destroy()

    def minimize_windows(self):
        self.master.attributes('-alpha', 0)
        WindowsAPIManager.tirar_foco(self.master)                       
        self.master.minimized = True       

    def minimeze_linux(self):
        self.master.capture_master_window()
        self.master.withdraw()
        self.master.minimized = True                                        
        
    def deminimize(self,event=None):
        self.master.attributes('-alpha', 1) 
        self.master.minimized = False

    def maximize_window(self):
        if self.master.maximized == False: 
            self.master.normal_size = self.master.geometry()
            self.maximize_button.config(text="🗗")
            self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}+0+0")
            self.master.maximized = not self.master.maximized 
        else: 
            self.maximize_button.config(text="🗖")
            self.master.geometry(self.master.normal_size)
            self.master.maximized = not self.master.maximized             

    @staticmethod
    def criar_icone(caminho_icone):
        icone = Image.open(caminho_icone)   
        icone_dimensionado= icone.resize((25,25), Image.LANCZOS)  
        icone_imagem = ImageTk.PhotoImage(icone_dimensionado)
        return  icone_imagem    
    
    def mudar_icone(self,imagem):         
        icone_imagem = MyBar.criar_icone(imagem)         
        self.icone_barra.config(image=icone_imagem)
        self.icon_image = icone_imagem       


class MyTopLevel(Toplevel):       
   
    def __init__(self,master, title, nome_toplevel, widgets_informacoes, posicao_informacoes,toplevel_configs, *args, **kwargs):  
        super().__init__(master,*args, **kwargs)                   
        self.master = master
        self.titulo = title
        self.icone_padrao = master.icone_padrao               
        self.mybar2 = MyBar(self) 
        self.tm = MyTema        
        self.toplevels_instancias= {}        
        self.widgets_info = widgets_informacoes
        self.posicao_info = posicao_informacoes
        self.configs_info = toplevel_configs
        self.nome_toplevel = nome_toplevel
        self.widgets = {}
        self.minimized = False 
        self.maximized = False 
        self.normal_size = self.geometry()
        self.default_mytoplevel_config()      

    def default_mytoplevel_config(self):
        self.overrideredirect(True)                        

        self.grid_rowconfigure(1, weight=1)  
        self.grid_columnconfigure(0, weight=1)                           
  
        self.default_frame = ttk.Frame(self,style="Card.TFrame")  
        self.default_frame.grid(row=1, column=0, sticky="nsew")

        self.toplevels_instancias[self.nome_toplevel] = (self, self.default_frame )                  
        self.criar_widgets(self.nome_toplevel)   
       
        self.update_idletasks()
        self.tm.centralizar_janela(self) 

        if sys.platform == "win32":
            self.protocol("WM_DELETE_WINDOW", lambda: self.deletar_toplevel())
            self.mybar2.botao_fechar.configure(command=self.fechar_barra_windows) 
            self.iconbitmap(self.icone_padrao)
            self.tm.manter_icone(self)
            self.ativar_top_transparencia()
        elif sys.platform == "darwin":
            self.title(self.titulo)    
            self.overrideredirect(False)
            self.focus_force()
            MacAPIManager.hide_window_buttons(self)  
            self.mybar2.botao_fechar.configure(command=self.fechar_barra_mac)
            self.mybar2.minimize_button.configure(command=self.minimizar_barra_mac)
        elif sys.platform.startswith("linux"):
            self.nome_print = "top_screenshot.png"
            self.screenshot_path = None 
            self.tm.criar_atalho_linux(self)
            self.mybar2.botao_fechar.configure(command=self.fechar_barra_linux)                   
        return self

    def get_unique_name(self,nome):  
        base_name, extension = os.path.splitext(nome)  
        count = 1           
        while self.nome_print == nome:  
            nome = f"{base_name}_{count}{extension}"  
            count += 1        
        return nome 
    
    def deletar_print(self): 
        self.tm.deletar_print(self) 

    def capture_master_window(self):
        self.tm.capture_master_window(self)  

    def restaurar_janela(self):
        self.deiconify()  
        self.focus_force()

    def ativar_top_transparencia(self):  
        cor_transparente = "#3af30c"      
        try:            
            self.wm_attributes("-transparentcolor", cor_transparente)  
        except Exception as e:   
            print(f"Erro ao ativar transparencia (class toplevel): {e}") 
        else:                  
            self.default_frame.config(style="Dialog_buttons.TFrame")           
    
    def minimizar_barra_mac(self):
        self.withdraw()

    def fechar_barra_windows(self):
        self.attributes('-alpha', 0)
        self.master.attributes('-alpha', 1)
        self.master.focus_force() 

    def fechar_barra_mac(self):
        self.master.deiconify()
        self.withdraw()

    def fechar_barra_linux(self):    
        self.withdraw()
        self.tm.capture_master_window(self)
        self.minimized = True
        self.master.deiconify()             
        self.master.deletar_print()
        self.master.minimized = False 

    def deletar_toplevel(self):    
        """Destrói a instância do toplevel e limpa suas referências."""         
        self.destroy()
        del self.toplevels_instancias[self.nome_toplevel]
        MyTopManager.excluir_toplevel(self.nome_toplevel)      

    def criar_widgets(self, nome_toplevel):  
        """Cria todos os widgets associados à instância do toplevel fornecida."""  
        if nome_toplevel in self.toplevels_instancias:  
            for nome_widget, info in self.widgets_info[nome_toplevel].items():  
                tipo_widget = info["widget_class"]  
                widget = tipo_widget(self.toplevels_instancias[nome_toplevel][1], **info["kwargs"])
                if nome_widget not in self.widgets:                
                    self.widgets[nome_widget] = widget              
            for nome_widget in self.widgets_info[nome_toplevel]:  
                self.aplicar_posicao(nome_widget)  
            self.configurar_toplevel(nome_toplevel)               
        else:  
            raise KeyError(f"Nenhum widget encontrado para a instância: '{nome_toplevel}'.")      

    def aplicar_posicao(self, nome_widget):  
        """Aplica as opções de posicionamento ao widget pelo nome."""  
        if nome_widget in self.widgets:  
            widget = self.widgets[nome_widget]  
            try:  
                tipo = self.posicao_info[nome_widget]["type"]              
                opcoes = self.posicao_info[nome_widget]["kwargs"]                
                if tipo == "grid":  
                    widget.grid(**opcoes)  
                elif tipo == "pack":  
                    widget.pack(**opcoes)  
                elif tipo == "place":  
                    widget.place(**opcoes)  
                else:  
                    raise ValueError("Tipo de posicionamento não reconhecido.")                 
            except KeyError as e:  
                print(f"Erro ao aplicar posição: {e}")  
        else:  
            raise KeyError(f"Widget não encontrado para: '{nome_widget}'.")

    def configurar_toplevel(self, nome_toplevel):  
        """Configura o 'toplevel' com pesos dinâmicos para colunas e linhas coletados no dicionário self.configuracoes."""
        if nome_toplevel in self.configs_info:
            toplevel = self.toplevels_instancias[nome_toplevel][1]         
            pesos_colunas = self.configs_info.get(nome_toplevel, {}).get('peso_colunas', {})  
            for col, peso in pesos_colunas.items():  
                toplevel.grid_columnconfigure(col, weight=peso)   
            pesos_linhas = self.configs_info.get(nome_toplevel, {}).get('peso_linhas', {})  
            for row, peso in pesos_linhas.items():  
                toplevel.grid_rowconfigure(row, weight=peso)
        else:
            pass


class MyTopManager:
    toplevel_instances = {}

    def __init__(self):
        self.toplevels = []
        self.widgets_informacoes = {}   
        self.posicao_informacoes = {}
        self.toplevel_configs = {}

    @classmethod
    def excluir_toplevel(cls,nome_toplevel):
        if nome_toplevel in cls.toplevel_instances:
            del cls.toplevel_instances[nome_toplevel]

    def abrir_mytoplevel(self, master, nome_toplevel,title):
        if nome_toplevel in self.toplevels:               
            if sys.platform == "win32":
                master.attributes('-alpha', 0)
                master.minimized = True
                if nome_toplevel in MyTopManager.toplevel_instances:
                    toplevel = MyTopManager.toplevel_instances[nome_toplevel]
                    toplevel.restaurar_janela()                         
                else:
                    toplevel = self.criar_toplevel_windows(master, title, nome_toplevel)                            
                try:  
                    MyTema.mudar_cursor(toplevel, master.cursor_padrao)            
                except Exception as e:  
                    print(f"Erro: Não foi possível mudar o cursor do toplevel {nome_toplevel}. {e}")
            elif sys.platform == "darwin":    
                master.iconify()
                if nome_toplevel in MyTopManager.toplevel_instances:
                    toplevel = MyTopManager.toplevel_instances[nome_toplevel]
                    toplevel.restaurar_janela()                         
                else:
                    toplevel = self.criar_toplevel_windows(master, title, nome_toplevel)
                try:  
                    self.mudar_top_cursor_mac(master,toplevel)            
                except Exception as e:  
                    print(f"Erro: Não foi possível mudar o cursor do toplevel {nome_toplevel}. {e}")                
            elif sys.platform.startswith("linux"):
                master.withdraw()
                master.capture_master_window()    
                master.minimized = True
                if nome_toplevel in MyTopManager.toplevel_instances:
                    toplevel = MyTopManager.toplevel_instances[nome_toplevel]
                    toplevel.restaurar_janela()                         
                else:
                    toplevel = self.criar_toplevel_linux(master, title, nome_toplevel)               
                try:  
                    self.mudar_top_cursor_linux(toplevel)            
                except Exception as e:  
                    print(f"Erro: Não foi possível mudar o cursor do toplevel {nome_toplevel}. {e}")    
        else:
            print(f"O toplevel {nome_toplevel} não foi encontrado, para abrir o toplevel é necessário executar antes os métodos, set_widget_options e set_widget_grid")
    
    def mudar_top_cursor_mac(self,master,toplevel):
        self.cursor_padrao = master.cursor_padrao.replace("@","")
        tema = ttk.Style().theme_use()
        if tema in dicio.cursores_mac:           
            MyTema.mudar_cursor(toplevel,master.cursor_padrao)
            self.toplevel =toplevel
            self.listener2 = mouse.Listener(on_move=self.on_top_global_move)  
            self.listener2.start()                                              
        else:
            self.cursor_padrao = "arrow"
            MyTema.mudar_cursor(toplevel,self.cursor_padrao)
        self.ativar_modo_dark_mac(toplevel,tema)           
                    
    def on_top_global_move(self, x, y):  
        try:  
            x1 = self.toplevel.winfo_rootx()  
            y1 = self.toplevel.winfo_rooty()  
            x2 = x1 + self.toplevel.winfo_width()  
            y2 = y1 + self.toplevel.winfo_height()  
            if (x1 <= x <= x2 and y1 <= y <= y2):  
                MacAPIManager.set_custom_cursor(self.cursor_padrao)               
                self.listener2.stop() 
                return                  
        except Exception as e:  
            print(f"Ocorreu um erro no Listener: {e}")
            self.listener2.stop()

    def ativar_modo_dark_mac(self,toplevel,tema):
        modo = "dark" if tema.endswith("dark") else "light"
        MacAPIManager.set_window_appearance(toplevel,modo)

    def mudar_top_cursor_linux(self,toplevel):
        tema = ttk.Style().theme_use()
        if tema in dicio.cursores_windows:
            cursor = dicio.cursores_linux[tema]                
            MyTema.mudar_cursor_linux(toplevel,cursor)  
        else:
            MyTema.mudar_cursor(toplevel,"arrow") 

    def criar_toplevel_linux(self, master, title, nome_toplevel):   
        count = 1  
        unique_screenshot_path = "top_screenshot.png"   
        for toplevel in MyTopManager.toplevel_instances.values():
            while toplevel.screenshot_path == unique_screenshot_path:   
                unique_screenshot_path = f"top_screenshot_{count}.png"  
                count += 1  
        toplevel = MyTopLevel(master, title, nome_toplevel, self.widgets_informacoes, 
                              self.posicao_informacoes, self.toplevel_configs
                              )  
        toplevel.screenshot_path = unique_screenshot_path   
        MyTopManager.toplevel_instances[nome_toplevel] = toplevel
        return toplevel       

    def criar_toplevel_windows(self,master, title, nome_toplevel):
        toplevel = MyTopLevel(master, title, nome_toplevel, self.widgets_informacoes,
                              self.posicao_informacoes, self.toplevel_configs
                              )
        MyTopManager.toplevel_instances[nome_toplevel] = toplevel 
        return toplevel

    def set_widget_options(self,nome_widget, widget_class, nome_toplevel, **kwargs):
        if nome_toplevel not in self.toplevels:
            self.toplevels.append(nome_toplevel)  
        if nome_toplevel not in self.widgets_informacoes:  
            self.widgets_informacoes[nome_toplevel] = {}   
        self.widgets_informacoes[nome_toplevel][nome_widget] = {  
            'widget_class': widget_class,  
            'kwargs': kwargs  
        }  

    def set_widget_grid(self,nome_widget,tipo_posicao,**kwargs):    
        if nome_widget not in self.posicao_informacoes:  
            self.posicao_informacoes[nome_widget] = {} 
        self.posicao_informacoes[nome_widget] = {
            "type": tipo_posicao,
            "kwargs": kwargs 
        }
    def set_toplevel_config(self, nome_toplevel, peso_colunas=1, peso_linhas=1):  
        """Coleta as informações do usuário e armazena no dicionário de configurações."""  
        if nome_toplevel not in self.toplevel_configs:  
            self.toplevel_configs[nome_toplevel] = {}  

        # Processar peso_colunas  
        if isinstance(peso_colunas, dict):  
            self.toplevel_configs[nome_toplevel]['peso_colunas'] = peso_colunas  
        elif isinstance(peso_colunas, list):  
            self.toplevel_configs[nome_toplevel]['peso_colunas'] = {i: peso_colunas[i] for i in range(len(peso_colunas))}  
        else:  
            self.toplevel_configs[nome_toplevel]['peso_colunas'] = {i: peso_colunas for i in range(1)}   

        # Processar peso_linhas  
        if isinstance(peso_linhas, dict):  
            self.toplevel_configs[nome_toplevel]['peso_linhas'] = peso_linhas  
        elif isinstance(peso_linhas, list):  
            self.toplevel_configs[nome_toplevel]['peso_linhas'] = {i: peso_linhas[i] for i in range(len(peso_linhas))}  
        else:  
            self.toplevel_configs[nome_toplevel]['peso_linhas'] = {i: peso_linhas for i in range(1)}      
                            
                            
class WindowsAPIManager:

    def __init__(self):  
        pass 

    @staticmethod    
    def set_window_app_style(janela):    
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        hwnd = windll.user32.GetParent(janela.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
        janela.wm_withdraw()
        janela.after(11, lambda: janela.wm_deiconify())

    @staticmethod
    def manter_icone_bar_windows(janela):       
        try:                       
            WindowsAPIManager.set_window_app_style(janela)
            janela.after(10, lambda: WindowsAPIManager.set_window_app_style(janela))   
        except Exception as e:   
            print(f"Erro ao manter icone na barra de tarefas (classe Tema): {e}")
            pass  

    @staticmethod        
    def tirar_foco(janela):
        hwnd = windll.user32.GetParent(janela.winfo_id())
        windll.user32.ShowWindow(hwnd, 2)
        windll.user32.SetForegroundWindow(windll.user32.GetDesktopWindow())


class MacAPIManager:

    def __init__(self):  
        pass 

    @staticmethod    
    def set_window(janela):
        root_window_id = janela.winfo_id()      
        ns_windows = AppKit.NSApplication.sharedApplication().windows()  
        for window in ns_windows:  
            if window.isVisible():  
                if window.title() == janela.title() or window.identifier() == root_window_id:
                    return window

    @staticmethod
    def hide_window_buttons(janela):          
        window = MacAPIManager.set_window(janela)        
        window.standardWindowButton_(AppKit.NSWindowCloseButton).setHidden_(True)  
        window.standardWindowButton_(AppKit.NSWindowMiniaturizeButton).setHidden_(True)  
        window.standardWindowButton_(AppKit.NSWindowZoomButton).setHidden_(True)                  

    @staticmethod             
    def set_window_appearance(janela, appearance):
        window = MacAPIManager.set_window(janela)   
        if appearance == "dark":  
            window.setAppearance_(AppKit.NSAppearance.appearanceNamed_(AppKit.NSAppearanceNameDarkAqua))  
        elif appearance == "light":  
            window.setAppearance_(AppKit.NSAppearance.appearanceNamed_(AppKit.NSAppearanceNameAqua))             
     
    @staticmethod 
    def set_custom_cursor(cursor_mac):
        image = NSImage.alloc().initWithContentsOfFile_(cursor_mac)  
        if image is None: 
            print("Erro: imagem não pôde ser carregada. Verifique o caminho e o formato.")  
            return 
        hot_spot = NSSize(8, 8)  
        cursor = NSCursor.alloc().initWithImage_hotSpot_(image, hot_spot)  
        cursor.set()    
