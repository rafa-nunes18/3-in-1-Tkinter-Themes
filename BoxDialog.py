# Autor:

# Rafael A. Nunes (rafa.nunes2018@hotmail.com) 2024 

# Inspiração:

# Repositório no GitHub de rdbende chamado Sun Valley messageboxes
# https://github.com/rdbende/Sun-Valley-messageboxes
# rdbende (rdbende@proton.me)
# https://matrix.to/#/@rdbende:matrix.org
# @rdbende@mastodon.social

# MIT License

# Copyright (c) 2021 rdbende

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Introdução:
 
# A classe "MyPopup" é uma ferramenta que utiliza "MyDialog" para exibir diálogos interativos no aplicativo.
# Ela permite a exibição de ícone, título e mensagem, bem como a solicitação de resposta do usuário, como confirmações e cancelamentos.  

# Importações
import sys  
import tkinter as tk  
from tkinter import ttk 
from PIL import Image, ImageDraw, ImageTk, ImageFont
import Dicionarios_Mytema as dicio
if sys.platform.startswith("linux"):
    import tkXcursor as tx    

    
class MyDialog(tk.Toplevel):
    """
    Classe que representa um diálogo personalizado utilizando a biblioteca Tkinter.  

    Este diálogo é uma subclasse de Toplevel que oferece uma interface para exibir informações e botões.    
    """
    def __init__(self, master, title, details, icon, *,buttons, font):
        """
        Inicializa o diálogo com as configurações fornecidas e define o tema e estilo.  
        
        :param master: A janela pai (ou mestre) na qual o diálogo será exibido.  
        :param title: O título do diálogo.  
        :param details: Detalhes ou informações a serem exibidos no diálogo.  
        :param icon: O ícone a ser exibido na janela do diálogo.  
        :param buttons: Uma lista de botões a serem incluídos no diálogo.  
        :param font: Fonte a ser utilizada para o texto no diálogo.  
        """  
        super().__init__(master)           
        self.master = master  
        self.title = title  
        self.details = details  
        self.icon = icon  
        self.buttons = buttons
        self.fonte = font          
        self.font_size_title = 30  
        self.font_size_details = 20  
        self.result = [None]  
        self.estilo = ttk.Style()
        self.tema =self.estilo.theme_use()
        self.bg_color = self.estilo.lookup(ttk.Labelframe, 'background')  
        self.default_tema_config()
      
    def default_tema_config(self):
        """  
        Configura os elementos padrões do tema e do layout do diálogo.  

        Este método cria a estrutura do diálogo, incluindo frames, canvas e botões.
        """
        self.master.minimized = True
          
        self.big_frame = tk.Frame(self)  
        self.big_frame.pack(fill="both", expand=True)  
        self.big_frame.columnconfigure(0, weight=1)  

        self.imagem_fundo, self.imagem_icon = self.atualizar_imagem()        
        self.imagem = self.create_rounded_image(self.imagem_fundo, radius=10)  

        self.canvas = tk.Canvas(self.big_frame,
                                width=self.imagem.size[0],
                                height=self.imagem.size[1],
                                background=self.bg_color,
                                highlightbackground=self.bg_color,
                                highlightcolor=self.bg_color
                            )  
        self.canvas.grid(row=0, column=0, sticky="nsew") 

        self.button_frame = ttk.Frame(self.big_frame, padding=(22, 22, 12, 22), style="Card.TFrame")  
        self.button_frame.grid(row=2, column=0, sticky="nsew")
                
        self.overrideredirect(True)
        self.initialize_fonts()       
        self.criar_titulo_imagem(self.title, self.imagem)  
        self.criar_detalhes_imagem(self.details, self.imagem)  
        self.criar_imagem_canvas(self.imagem, self.canvas)  
        self.criar_icone(self.imagem_icon, self.canvas)
        self.criar_botoes(self.button_frame,self.buttons)         
        self.update_idletasks()  
        self.center_dialog(self.master)
        if sys.platform == "win32":   
            self.ativar_transparencia()
            self.mudar_cursor()
        elif sys.platform == "darwin":
            pass
        elif sys.platform.startswith("linux"):
            self.mudar_cursor_linux()          

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

        Atenção: Cuidado com os tamanhos de titulo e detalhes, tamanhos grandes podem ultrapassar o tamanho
        da janela de mensagem, escolha o tamanho e teste antes de usar.    
        """            
        if self.fonte != None: 
            if isinstance(self.fonte, tuple):  
                if len(self.fonte) == 3:  
                    self.font_name, self.font_size_title, self.font_size_details = self.fonte
                    try:  
                        self.font = ImageFont.truetype(self.font_name, self.font_size_title)  
                        self.font2 = ImageFont.truetype(self.font_name, self.font_size_details)  
                    except OSError:  
                        print(f"Não foi possível abrir a fonte {self.font_name}, utilizando fonte padrão.")  
                        self.set_font()  
                elif len(self.fonte) == 2:  
                    self.font_size_title, self.font_size_details = self.fonte
                    self.set_font() 
                else:    
                    print("Erro: `font` deve ser uma tupla com 2 ou 3 objetos.")  
                    return               
        else:            
            self.set_font()

    def set_font(self):
        """  
        Define a fonte a ser utilizada na interface do diálogo com base no sistema operacional em uso.   
        A fonte é escolhida de acordo com a plataforma (Windows, macOS ou Linux) e aplicada a diferentes tamanhos   
        para título e detalhes.  
        """  
        if sys.platform == "win32":   
            self.font_name = r"C:\\Windows\\Fonts\\Arial.ttf"
        elif sys.platform == "darwin":
            self.font_name = "/System/Library/Fonts/Helvetica.ttc"
        elif sys.platform.startswith("linux"):               
            self.font_name = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        self.font = ImageFont.truetype(self.font_name, self.font_size_title)  
        self.font2 = ImageFont.truetype(self.font_name, self.font_size_details)                   
        
    def mudar_cursores(self,cursor):
        """  
        Altera o cursor do ponteiro para um especificado no diálogo e em todos os seus filhos.   
        Isso aplica um cursor consistente em toda a interface.  

        :param cursor: O nome do cursor a ser aplicado.  
        """         
        self.config(cursor=cursor)
        for child in self.winfo_children():  
                child.config(cursor=cursor)

    def mudar_cursor(self):
        """  
        Atualiza o cursor do diálogo de acordo com o tema atual, utilizando um dicionário pré-definido   
        de cursores para Windows. Se o tema não estiver no dicionário, o cursor padrão é utilizado.  
        """ 
        if self.tema in dicio.cursores_windows:
            cursor = dicio.cursores_windows[self.tema]
            self.mudar_cursores(cursor)
        else:
            self.mudar_cursores("arrow") 

    def mudar_cursor_linux(self):
        """  
        Altera o cursor em sistemas Linux utilizando um dicionário de cursores.   
        Se o tema especificado não estiver disponível, o cursor padrão é utilizado.  
        Se houver falha ao carregar um cursor para um filho, uma mensagem de erro é exibida.  
        """ 
        if self.tema in dicio.cursores_linux:
            cursor = dicio.cursores_linux[self.tema]                    
            cursor_linux = tx.x_load_cursor(self, cursor)  
            tx.x_set_cursor(self, cursor_linux)
            for child in self.winfo_children():          
                id = child.winfo_id()  
                try:   
                    cursor_filho_linux = tx.x_load_cursor(child, cursor)  
                    tx.x_set_cursor(child, cursor_filho_linux)  
                except Exception as e:  
                    print(f"Erro ao colocar o cursor no child {child} (ID: {id}), erro: {e}")
        else:
            self.mudar_cursores("arrow")

    def ativar_transparencia(self):
        """  
        Ativa a transparência na janela do diálogo, definindo uma cor específica   
        (neste caso, verde claro) como a cor de fundo transparente.   
        Isso melhora a estética do diálogo removendo o fundo.  
        """           
        cor_transparente = "#3af30c"                                   
        self.master.attributes('-alpha', 0)            
        self.wm_attributes("-transparentcolor", cor_transparente)  
        self.canvas.config(background=cor_transparente,  
                    highlightbackground=cor_transparente,  
                    highlightcolor=cor_transparente)  
        self.button_frame.config(style="Dialog_buttons.TFrame")        
          
    def criar_botoes(self,button_frame, buttons):
        """  
        Cria botões no frame especificado com base em uma lista de valores.   
        Cada botão pode ter um estado e estilo específicos, permitindo criar   
        botões com ações definidas pelos usuários.  

        :param button_frame: O frame onde os botões serão colocados.  
        :param buttons: Uma lista de tuplas, onde cada tupla contém   
                        (texto_do_botão, comando_associado, estado_opcional).  
        """   
        for index, button_value in enumerate(buttons):  
            style = None  
            state = None  
            default = False  
            sticky = "nse" if len(buttons) == 1 else "nsew"
            if len(button_value) > 2:  
                if button_value[2] == "accent":  
                    style = "Accent.TButton"  
                    default = True  
                elif button_value[2] == "disabled":  
                    state = "disabled"  
                elif button_value[2] == "default":  
                    default = True
            button = ttk.Button(  
                button_frame,  
                text=button_value[0],  
                width=17,  
                command=lambda value=button_value[1]: self.on_button(value),  
                style=style,  
                state=state,  
            )  
            if default:  
                button.bind("<Return>", button["command"])  
                button.focus() 

            button.grid(row=0, column=index, sticky=sticky, padx=(0, 10))  
            button_frame.columnconfigure(index, weight=1)      

    def on_button(self,value):
        """  
        Trata a ação de um botão quando clicado. Define o resultado da ação e   
        destrói a janela do diálogo. Isso também permite restaurar a visibilidade do   
        elemento pai do diálogo.  

        :param value: O valor associado ao botão, que será retornado quando o diálogo for fechado.  
        """ 
        try:
            self.master.attributes('-alpha', 1) 
        except Exception as e:   
            print(f"Erro ao mostrar a barra padrão : {e}")
            pass      
        self.result[0] = value  
        self.destroy()

    def show(self):
        """  
        Exibe o diálogo como uma janela modal, permitindo que o usuário interaja   
        até que a janela seja fechada. Retorna o resultado da interação ao   
        usuário quando o diálogo é fechado.  

        :return: O valor resultante da interação do usuário com o diálogo.  
        """          
        self.transient(self.master)  
        self.grab_set() 
        self.wait_window(self)         
        return self.result[0]     

    def create_rounded_image(self,image, radius):  
        """  
        Cria uma nova imagem com bordas arredondadas com base em uma imagem original,   
        utilizando um raio de arredondamento especificado. Isso é utilizado para   
        dar um estilo visual mais suave e moderno ao diálogo.  

        :param image: A imagem original que será arredondada.  
        :param radius: O raio para as bordas arredondadas.  

        :return: A imagem original com bordas arredondadas.  
        """ 
        rounded_mask = Image.new('L', image.size, 0)  
        draw = ImageDraw.Draw(rounded_mask)  
        draw.rounded_rectangle((0, 0, image.size[0], image.size[1]), radius, fill=255)   
        rounded_image = Image.new('RGBA', image.size)  
        rounded_image.paste(image, (0, 0), rounded_mask)        
        return rounded_image

    def atualizar_imagem(self):
        """  
        Atualiza a imagem de fundo e o ícone do diálogo de acordo com o tema atual.   
        A imagem é carregada de acordo com o sistema operacional em uso e a configuração do tema.  
        Se um ícone for especificado, também é carregada uma imagem de ícone correspondente.  
        Caso contrário, uma mensagem de aviso é exibida.  
        """         
        if self.tema in dicio.fundos_tema:
            if sys.platform == "win32": 
                imagem = Image.open(dicio.fundos_tema[self.tema]["imagem-fundo"])
            else:
                imagem = Image.open(dicio.fundos_tema[self.tema]["imagem-fundo"].replace('\\','/')) 
        else:
            if sys.platform == "win32":
                imagem = Image.open(r"imagens\fundos\tema-light.png")
            else:
                imagem = Image.open(r"imagens\fundos\tema-light.png".replace('\\','/'))    
        if self.icon != None:                
            icone = "imagem-" + str(self.icon) + "-icon"
            tema_icon = str(self.tema).replace("-light","").replace("-dark","")
            if sys.platform == "win32":
                imagem_icon = Image.open(dicio.icons_box[tema_icon][icone])
            else:   
                imagem_icon = Image.open(dicio.icons_box[tema_icon][icone].replace('\\','/'))              
            return  imagem ,imagem_icon
        else:
            print("escolha um ícone")
    
    def rolagem_texto(self, text, max_width):
        """  
        Divide o texto em várias linhas, garantindo que cada linha não exceda a largura máxima especificada.  
            
        :param text: O texto a ser dividido em linhas.  
        :param max_width: A largura máxima que cada linha pode ocupar.  
            
        :return: Uma lista de linhas resultantes.  
        """   
        linhas = []  
        palavras = text.split()  
        linha_atual = ""
        for palavra in palavras:   
            linha_teste = f"{linha_atual} {palavra}".strip()  
            bbox = self.font.getbbox(linha_teste)  
            largura = bbox[2] - bbox[0]  
            if largura <= max_width:  
                linha_atual = linha_teste 
            else:  
                if linha_atual:  
                    linhas.append(linha_atual) 
                palavra_bbox = self.font.getbbox(palavra)  
                largura_palavra = palavra_bbox[2] - palavra_bbox[0]
                if largura_palavra <= max_width:  
                    linha_atual = palavra
                else:   
                    print(f"Palavra '{palavra}' não coube na largura máxima e será ignorada") 
        if linha_atual:  
            linhas.append(linha_atual)
        return linhas 

    def desenhar_contorno_texto(self,draw, text, position, font, cor_texto, cor_contorno):  
        """  
        Desenha o texto com um contorno ao redor, aumentando a legibilidade.  

        :param draw: O objeto de desenho onde o texto será desenhado.  
        :param text: O texto que será desenhado.  
        :param position: A posição (x, y) onde o texto será desenhado.  
        :param font: A fonte a ser utilizada para desenhar o texto.  
        :param cor_texto: A cor do texto.  
        :param cor_contorno: A cor do contorno do texto.  
        """  
        offset_positions = [(-1, -1),  # Cima à esquerda  
                            (1, -1),   # Cima à direita  
                            (-1, 1),   # Baixo à esquerda  
                            (1, 1),    # Baixo à direita  
                            (-1, 0),   # Esquerda  
                            (1, 0),    # Direita  
                            (0, -1),   # Cima  
                            (0, 1)]    # Baixo 
        for offset in offset_positions:  
            offset_x, offset_y = offset  
            draw.text((position[0] + offset_x, position[1] + offset_y), text, fill=cor_contorno, font=font)
        draw.text(position, text, fill=cor_texto, font=font)  

    def criar_titulo_imagem(self, title, image):
        """  
        Cria um título na imagem fornecida.  

        :param title: O texto do título a ser desenhado.  
        :param image: A imagem onde o título será desenhado.  
        """         
        draw = ImageDraw.Draw(image)  
        x = 40  
        y = 15  
        cor_texto ,cor_contorno = self.set_color_font()      
        self.desenhar_contorno_texto(draw, title, (x, y), self.font, cor_texto, cor_contorno)  

    def criar_detalhes_imagem(self, detalhes, image):
        """  
        Adiciona detalhes a uma imagem, dividindo o texto conforme necessário para caber na largura especificada.  

        :param detalhes: O texto de detalhes a ser adicionado à imagem.  
        :param image: A imagem na qual os detalhes serão desenhados.  
        """          
        draw = ImageDraw.Draw(image)  
        margem_esquerda = 160  
        max_largura_detalhes = image.size[0] - 60 
        y_position = 70  
        espaco_linha = 10
        cor_texto ,cor_contorno = self.set_color_font()
        wrapped_details = self.rolagem_texto(detalhes, max_largura_detalhes)  
        for i, line in enumerate(wrapped_details):  
            position = (margem_esquerda, y_position + i *  self.font_size_details + espaco_linha)  
            self.desenhar_contorno_texto(draw, line, position, self.font2, cor_texto, cor_contorno)
    
    def set_color_font(self):
        """  
        Define as cores do texto e do contorno com base no tema atual.  

        :return: As cores do texto e do contorno.  
        """ 
        if self.tema in dicio.fundos_tema:  
            cor_texto = (255, 255, 255, 255)  
            cor_contorno = (0, 0, 0)    
        else:  
            cor_texto = (0, 0, 0, 255)    
            cor_contorno = (255, 255, 255)
        return  cor_texto ,cor_contorno         

    def criar_imagem_canvas(self,imagem,canvas):
        """  
        Converte uma imagem em um formato que pode ser exibido em um canvas do Tkinter.  

        :param imagem: A imagem a ser convertida.  
        :param canvas: O canvas onde a imagem será exibida.  
        """ 
        fundo_imagem = ImageTk.PhotoImage(imagem)  
        canvas.create_image(0, 0, anchor=tk.NW, image=fundo_imagem)  
        canvas.image1 = fundo_imagem

    def criar_icone(self,imagem,canvas):
        """  
        Adiciona um ícone a um canvas sobre uma imagem de fundo.  

        :param imagem: A imagem do ícone a ser adicionada.  
        :param canvas: O canvas onde o ícone será desenhado.  
        """      
        icon_image = imagem.resize((100, 100), Image.LANCZOS)  
        icon_tk = ImageTk.PhotoImage(icon_image)      
        canvas.create_image(30, 60, anchor=tk.NW, image=icon_tk)   
        canvas.image2 = icon_tk                                      

    def center_dialog(self,master):
        """  
        Centraliza o diálogo na tela ou em relação à janela pai fornecida.  

        :param master: A janela pai em relação à qual o diálogo será centralizado.  
        """    
        self.update_idletasks()
        dialog_width = self.winfo_width()  
        dialog_height = self.winfo_height()
        if master is None:  
            master_width = self.winfo_screenwidth()  
            master_height = self.winfo_screenheight()  
            master_x = 0  
            master_y = 0  
        else:  
            master_width = master.winfo_width()  
            master_height = master.winfo_height()  
            master_x = master.winfo_x()  
            master_y = master.winfo_y()
        x_coord = int(master_width / 2 + master_x - dialog_width / 2)  
        y_coord = int(master_height / 2 + master_y - dialog_height / 2)
        self.geometry("+{}+{}".format(x_coord, y_coord))  
        self.minsize(320, dialog_height)    

class MyPopup():
    """  
    Classe responsável por exibir MyDialog em diferentes tipos de popups para interagir com o usuário, com configurações personalizáveis.    
    """  

    def __init__(self, master):
        """  
        Inicializa a classe MyPopup com uma referência à janela principal.    

        :param master: A janela principal onde o popup será exibido.  
        """  
        self.master = master

    def show_mensagem(self, title="Title", details="Description", *, icon="info", font=None): 
        """  
        Mostra uma mensagem de informação com um botão "Ok".  
        
        Este método exibe uma caixa de diálogo com um título e uma descrição fornecidos, permitindo ao usuário   
        reconhecer a informação apresentada.  

        :param title: O título da mensagem.  
        :param details: A descrição da mensagem.  
        :param icon: O ícone a ser exibido (padrão é "info").  
        :param font: A fonte a ser utilizada no texto.  
        
        :return: O resultado da interação com o diálogo.  
        """   
        dialog = MyDialog(  
            self.master,  
            title,  
            details,  
            icon,
            font = font,  
            buttons=[("Ok", None, "default")],  
        )  
        dialog.show()   
        return dialog.result[0] 

    def ask_sim_cancelar(self, title="Title", details="Description", *, icon="pergunta", font=None):
        """  
        Solicita ao usuário uma confirmação com opções "Sim" e "Cancelar".  
        
        Este método é utilizado para perguntar ao usuário se ele deseja prosseguir ou não, oferecendo uma   
        escolha clara entre duas opções.  

        :param title: O título da pergunta.  
        :param details: A descrição da pergunta.  
        :param icon: O ícone a ser exibido (padrão é "pergunta").  
        :param font: A fonte a ser utilizada no texto.  
        
        :return: True se o usuário escolher "Sim", caso contrário None.  
        """   
        dialog = MyDialog(  
            self.master,  
            title,  
            details,  
            icon,
            font = font,  
            buttons=[("Sim", True, "accent"), ("Cancelar", None)],  
        )  
        dialog.show()  
        return dialog.result[0]  

    def ask_sim_nao(self, title="Title", details="Description", *, icon="pergunta", font=None):
        """  
        Solicita ao usuário uma confirmação com opções "Sim" e "Não".  
        
        Este método é projetado para permitir que o usuário tome decisões claras através de respostas diretas.   

        :param title: O título da pergunta.  
        :param details: A descrição da pergunta.  
        :param icon: O ícone a ser exibido (padrão é "pergunta").  
        :param font: A fonte a ser utilizada no texto.  
        
        :return: True se o usuário escolher "Sim", False se escolher "Não".  
        """   
        dialog = MyDialog(  
            self.master,  
            title,  
            details,  
            icon,  
            font = font,
            buttons=[("Sim", True, "accent"), ("Não", False)],  
        )  
        dialog.show()  
        return dialog.result[0]  

    def ask_sim_nao_cancelar(self, title="Title", details="Description", *, icon="pergunta", font=None):
        """  
        Solicita ao usuário uma confirmação com opções "Sim", "Não" e "Cancelar".  

        Este método oferece uma escolha mais completa ao usuário, permitindo que ele tente interromper uma ação proposta.  

        :param title: O título da pergunta.  
        :param details: A descrição da pergunta.  
        :param icon: O ícone a ser exibido (padrão é "pergunta").  
        :param font: A fonte a ser utilizada no texto.  
        
        :return: True se o usuário escolher "Sim", False se escolher "Não", caso contrário None.  
        """   
        dialog = MyDialog(  
            self.master,  
            title,  
            details,  
            icon,
            font = font,  
            buttons=[("Sim", True, "accent"), ("Não", False), ("Cancelar", None)],  
        )  
        dialog.show()  
        return dialog.result[0]  

    def ask_repetir_cancelar(self, title="Title", details="Description", *, icon="pergunta", font=None):
        """  
        Solicita ao usuário uma confirmação com opções "Repetir" e "Cancelar".  
        
        Este método é útil para situações onde o usuário pode optar por repetir uma ação anterior ou cancelá-la.  

        :param title: O título da pergunta.  
        :param details: A descrição da pergunta.  
        :param icon: O ícone a ser exibido (padrão é "pergunta").  
        :param font: A fonte a ser utilizada no texto.  
        
        :return: True se o usuário escolher "Repetir", caso contrário None.  
        """   
        dialog = MyDialog(  
            self.master,  
            title,  
            details,  
            icon,
            font = font,  
            buttons=[("Repetir", True, "accent"), ("Cancelar", None)],  
        )  
        dialog.show()  
        return dialog.result[0]  

    def ask_aceitar_recusar(self, title="Title", details="Description", *, icon="pergunta", font=None):
        """  
        Solicita ao usuário uma confirmação com opções "Aceitar" e "Recusar".  
        
        Este método permite que o usuário decida se aceita ou recusa uma ação proposta, com a possibilidade de   
        feedback claro.  

        :param title: O título da pergunta.  
        :param details: A descrição da pergunta.  
        :param icon: O ícone a ser exibido (padrão é "pergunta").  
        :param font: A fonte a ser utilizada no texto.  
        
        :return: True se o usuário escolher "Aceitar", False se escolher "Recusar".  
        """   
        dialog = MyDialog(  
            self.master,  
            title,  
            details,  
            icon,
            font = font,  
            buttons=[("Aceitar", True, "accent"), ("Recusar", False)],  
        )  
        dialog.show()  
        return dialog.result[0]
