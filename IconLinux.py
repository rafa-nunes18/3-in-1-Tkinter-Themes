# Autor:

# Rafael A. Nunes (rafa.nunes2018@hotmail.com) 2024 

# Inspiração:

# Repositório no GitHub de Moisés-Palmer chamada pystray
# https://github.com/moses-palmer/pystray 
# Moisés-Palmer (https://github.com/moses-palmer)

# Copyright (C) 2016-2017 Moses Palmér
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Introdução:
# A classe "MyIcon" é uma ferramenta para exibir um atalho da Janela do Tkinter na barra de tarefas do Linux.
 

# Importar bibliotecas
import contextlib
import functools
import threading
from PIL import Image, ImageTk
import Xlib.display
import Xlib.threaded
import Xlib.XK
import queue
import logging
import tkinter as tk
from tkinter import ttk
from pynput import mouse 

# Cria um display para verificar se tem uma conexão X  
display = Xlib.display.Display()
display.close()
del display

# Define uma exceção personalizada para gerenciar erros relacionados ao X11.  
class XError(Exception):
    pass

# Gerenciador de contexto que lida com a configuração e restauração do manipulador de erros do display X11. 
@contextlib.contextmanager
def display_manager(display):
    errors = []
    def handler(*args):
        errors.append(args)
    old_handler = display.set_error_handler(handler)
    try:
        yield
        display.sync()
    finally:
        display.set_error_handler(old_handler)
    if errors:
        raise XError(errors)

class MyIcon(object):
    """  
    Classe responsável por gerenciar um ícone na barra de tarefas, permitindo a interação   
    com a janela principal da aplicação.  

    Esta classe cria um atalho da janela com ícone na barra de tarefas, gerencia eventos do   
    mouse e fornece funcionalidades adicionais como menus e janelas de tooltip.  
    """  
    
    def __init__(self, master, icon="imagens/icons/icone-padrao64x64.png"):
        """  
        Inicializa uma nova instância da classe MyIcon com os parâmetros fornecidos.  

        Esta inicialização cria um atalho da janela com ícone na barra de tarefas, configurando   
        o ícone que será exibido, além de inicializar diversos componentes e gerenciadores   
        de eventos necessários para a funcionalidade do ícone.  

        :param master: O widget pai associado ao ícone. Deve ser uma instância de um widget Tkinter.  
        :param icon: Caminho para o arquivo de ícone. O valor padrão é "imagens/icons/icone-padrao64x64.png".  
        """  
        self.master = master
        self._name = master.titulo
        self.icon_path = icon
        self._icon = self._criar_icone()
        self._title = master.titulo
        self._visible = False
        self._icon_valid = False
        self._log = logging.getLogger(__name__)
        self._running = False
        self._icon_data = None
        self._systray_manager = None
        self._tooltip_window = None
        self._menu_close_window = None        
        self._XEMBED_VERSION = 0
        self._XEMBED_MAPPED = 1
        self._SYSTEM_TRAY_REQUEST_DOCK = 0
        self._message_handlers = {
            Xlib.X.EnterNotify: self._on_mouse_enter,
            Xlib.X.LeaveNotify: self._on_mouse_leave,
            Xlib.X.ButtonPress: self._on_button_press,
            Xlib.X.ButtonRelease: self._on_button_release,
            Xlib.X.ConfigureNotify: self._on_expose,
            Xlib.X.DestroyNotify: self._on_destroy_notify,
            Xlib.X.Expose: self._on_expose}
        self._queue = queue.Queue()
        self._display = Xlib.display.Display()
        self._create_tooltip_window()
        self._create_menu_window()        
        with display_manager(self._display):            
            self._create_atoms()
            self._window = self._create_window()
            self._gc = self._window.create_gc()                   

    def __del__(self):
        """  
        Libera os recursos utilizados pela instância do MyIcon ao ser destruída.  
        """  
        try:
            if self._running:
                self._stop()
                if threading.current_thread().ident != self._thread.ident:
                    self._thread.join()
        finally:
            self._display.close()

    @property
    def name(self):
        """  
        Retorna o nome do ícone associado ao widget pai.  
        """ 
        return self._name

    @property
    def icon(self):
        """  
        Retorna o ícone atual associado à instância.  
        """
        return self._icon

    @icon.setter
    def icon(self, value):
        """  
        Define um novo ícone para a instância e atualiza a visibilidade se necessário.  

        :param value: Novo caminho do ícone.  
        """  
        self._icon = value
        self._icon_valid = False
        if value:
            if self.visible:
                self._update_icon()
        else:
            if self.visible:
                self.visible = False

    @property
    def title(self):
        """  
        Retorna o título atual do ícone.  
        """  
        return self._title

    @title.setter
    def title(self, value):
        """  
        Define um novo título para o ícone. Atualiza o título visível se necessário.  

        :param value: Novo título do ícone.  
        """  
        if value != self._title:
            self._title = value
            if self.visible:
                self._update_title()

    @property
    def visible(self):
        """  
        Retorna a visibilidade atual do ícone.  
        """ 
        return self._visible

    @visible.setter
    def visible(self, value):
        """  
        Define a visibilidade do ícone, mostrando ou ocultando conforme necessário.  

        :param value: Valor de visibilidade a ser definido.  
        """ 
        if self._visible == value:
            return
        if value:
            if not self._icon:
                raise ValueError('cannot show icon without icon data')
            if not self._icon_valid:
                self._update_icon()
            self._show()
            self._visible = True
        else:
            self._hide()
            self._visible = False

    def mudar_icone_linux(self,imagem):
        """  
        Atualiza o caminho da imagem do ícone para a versão Linux.  

        :param imagem: Novo caminho da imagem do ícone.  
        """  
        self.icon_path = imagem
        
    def _criar_icone(self):
        """  
        Cria o ícone a partir do caminho fornecido e retorna a imagem resultante.  
        """         
        img = Image.open(self.icon_path)
        return img

    def run(self, setup=None):
        """  
        Inicia o ícone, executando o loop principal após a configuração opcional.  

        :param setup: Função de configuração opcional a ser chamada.  
        """  
        def setup_handler():
            self._queue.get()
            if setup:
                setup(self)
            else:
                self.visible = True
        self._setup_thread = threading.Thread(target=setup_handler)
        self._setup_thread.start()
        self._run()
        self._running = True

    def iniciar(self):
        """  
        Inicia o ícone em uma nova thread.  
        """  
        self._running = True
        threading.Thread(target=self.run).start()

    def stop(self):
        """  
        Para a execução do ícone, libera recursos associados e encerra threads relacionadas.  
        """ 
        self._tooltip_window.destroy()
        self._menu_close_window.destroy()        
        self._stop()
        if self._running:               
            if self._setup_thread.ident != threading.current_thread().ident:
                self._setup_thread.join()
        self._running = False
        self._loop = False         
        
    def _mark_ready(self):
        """  
        Marca a instância como pronta, colocando um sinal na fila.  
        """    
        self._queue.put(True)

    def _handler(self, callback):
        """  
        Cria um decorador que envolve a chamada de retorno, passando a instância como argumento.  

        :param callback: Função de retorno a ser decorada.  
        """  
        @functools.wraps(callback)
        def inner(*args, **kwargs):          
            callback(self)
        return inner        

    def _show(self):
        """  
        Exibe o ícone dockado, trata falha na operação se ocorrer.  
        """
        try:
            self._assert_docked()
        except AssertionError:
            self._log.error('Failed to dock icon', exc_info=True)

    def _hide(self):
        """  
        Oculta o ícone se estiver dockado.  
        """  
        if self._systray_manager:
            self._undock_window()

    def _update_icon(self):
        """  
        Atualiza a aparência do ícone e garante que ele esteja dockado corretamente.  
        """ 
        try:
            self._assert_docked()
        except AssertionError:
            self._log.error('Failed to dock icon', exc_info=True)
            return
        self._icon_data = None
        self._draw()
        self._icon_valid = True

    def _update_title(self):
        """  
        Atualiza o título da janela do ícone com base no valor atual.  
        """ 
        self._window.set_wm_name(self.title)

    def _run(self):
        """  
        Marca a instância como pronta e inicia o loop principal.  
        """
        self._mark_ready()
        self._thread = threading.current_thread()
        self._mainloop()

    def _stop(self):
        """  
        Para o ícone, destruindo a janela e liberando recursos.  
        """        
        self._window.destroy()
        self._display.flush()

    def _close(self):
        """  
        Fecha o ícone e libera recursos associados ao widget pai.  
        """ 
        self.master.deletar_print()  
        if hasattr(self.master, 'master_linux'):
            self.master.mybar1.fechar_linux()
        else:    
            self.stop()
            self.master.deletar_toplevel()                

    def _mainloop(self):
        """  
        Executa o loop principal, processando eventos até que o ícone seja destruído.  
        """  
        try:  
            for event in self._events():                               
                if event.type == Xlib.X.DestroyNotify and event.window == self._window:  
                    break
                if self._running:                               
                    self._message_handlers.get(event.type, lambda e: None)(event)  
        except Exception as e:  
            self._log.error('An error occurred in the main loop: %s', e, exc_info=True)  

    def _on_button_press(self, event):
        """  
        Manipula eventos de pressionamento do botão 1 e 3 do mouse.  
        """ 
        if event.detail == 1:
            self.restaurar_window()
        if event.detail == 3:
            self._menu_window(event)         

    def _on_button_release(self, event):
        """  
        Manipula eventos de liberação do botão 1 ao 6 do mouse.  
        """   
        if event.detail  in range(1, 6):  
            self._on_mouse_leave(event)

    def _on_mouse_enter(self, event):
        """  
        Manipula eventos ao entrar no ícone com o mouse, exibindo uma tooltip.  
        """     
        if hasattr(event, 'root_x') and hasattr(event, 'root_y'):  
            if self.master.minimized:  
                self.show_screenshot()  
                x = event.root_x - 100  # Ajuste a posição X para centralizar acima do ícone  
                y = event.root_y - 181  # Ajuste a posição Y para aparecer acima do ícone 
                self._tooltip_window.geometry(f"+{x}+{y}")  # Posiciona a janela  
                self._tooltip_window.deiconify()
                self._tooltip_window.lift()           

    def _on_mouse_leave(self,event):
        """  
        Manipula eventos ao sair do ícone com o mouse, ocultando a tooltip.  
        """   
        if self._tooltip_window : 
            self._tooltip_window.withdraw()

    def _fechar_menu_window(self):
        """  
        Oculta a janela do menu, se estiver visível.  
        """   
        if self._menu_close_window:  
            self._menu_close_window.withdraw() 

    def _menu_window(self,event):
        """  
        Exibe a janela do menu na posição do cursor do mouse quando o botão direito é pressionado.  
        """  
        if hasattr(event, 'root_x') and hasattr(event, 'root_y'):
            x = event.root_x - 50  # Ajuste a posição X para centralizar acima do ícone  
            y = event.root_y - 55  # Ajuste a posição Y para aparecer acima do ícone 
            self._menu_close_window.geometry(f"+{x}+{y}")  # Posiciona a janela  
            self._menu_close_window.deiconify()        
            self._menu_close_window.lift()
            self.listener = mouse.Listener(on_click=self.on_global_click)  
            self.listener.start()           

    def restaurar_window(self):
        """  
        Restaura a janela principal se estiver minimizada, ou a minimiza caso contrário.  
        """  
        self._on_mouse_leave(None)         
        if self.master.minimized == True:
            self.master.deletar_print()  
            self.master.deiconify()
            self.master.lift()
            self.master.minimized = False  
        else:
            self.master.capture_master_window()  
            self.master.withdraw()
            self.master.minimized = True 

    def _create_tooltip_window(self):
        """  
        Cria uma nova janela para a tooltip.  
        """        
        self._tooltip_window = tk.Toplevel(self.master)  
        self._tooltip_window.overrideredirect(True)  # Remove bordas da janela  
        self._tooltip_window.geometry("210x160")  # Define um tamanho apropriado  
        self._tooltip_window.withdraw()  # Inicialmente oculta a janela  

        # Adiciona um LabelFrame para título e imagem  
        self.tooltip_frame = ttk.Labelframe(self._tooltip_window, text=self._title)  
        self.tooltip_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5) 

        # Label para exibir a imagem  
        self.image_label = tk.Label(self.tooltip_frame, bg='white')  
        self.image_label.pack(pady=1)
    
    def _create_menu_window(self):
        """  
        Cria uma nova janela para o menu.  
        """   
        self._menu_close_window= tk.Toplevel(self.master)  
        self._menu_close_window.overrideredirect(True)  # Remove bordas da janela  
        self._menu_close_window.geometry("100x33")  # Define um tamanho apropriado  
        self._menu_close_window.withdraw()
    
        # Definir o layout de grade na janela
        for i in range(2): 
            self._menu_close_window.columnconfigure(i, weight=1)

        # Botão para fechar a janela
        self.button_close = ttk.Button(self._menu_close_window,text="Fechar",command=lambda:self._close())
        self.button_close.grid(columnspan= 2, sticky ="ew")  

    def on_global_click(self, x, y, button, pressed):
        """  
        Manipula cliques globais, verificando se o clique ocorreu fora da janela do menu.  
        """  
        if pressed:  
            # Obtém as coordenadas da janela 2  
            x1 = self._menu_close_window.winfo_rootx()  
            y1 = self._menu_close_window.winfo_rooty()  
            x2 = x1 + self._menu_close_window.winfo_width()  
            y2 = y1 + self._menu_close_window.winfo_height()  

            # Verifica se o clique ocorreu dentro da janela 2  
            if not (x1 <= x <= x2 and y1 <= y <= y2):                 
                self._fechar_menu_window()
            self.listener.stop() 

    def show_screenshot(self):
        """  
        Exibe uma captura de tela redimensionada na interface de usuário.  
        """  
        img = Image.open(self.master.screenshot_path)
        img = img.resize((200, 160), Image.LANCZOS)  
        img_tk = ImageTk.PhotoImage(img)  
        self.image_label.config(image=img_tk)  
        self.image_label.image = img_tk   

    def _on_destroy_notify(self, event):
        """  
        Lida com a notificação de destruição da janela, verificando se o evento é do ícone da bandeja do sistema.  
        """  
        if event.window.id != self._systray_manager.id:
            return
        self._systray_manager = None
        try:
            self._assert_docked()
        except AssertionError:
            self._log.error('Failed to dock icon', exc_info=True)

    def _on_expose(self, event):
        """  
        Lida com eventos de exposição da janela, executando a função de desenho.  
        """  
        if event.window.id != self._window.id:
            return
        self._draw()

    def _create_atoms(self):
        """  
        Cria e registra átomos necessários para o ícone da bandeja do sistema.  
        """         
        self._xembed_info = self._display.intern_atom(
            '_XEMBED_INFO')  
        self._net_system_tray_sx = self._display.intern_atom(  
            '_NET_SYSTEM_TRAY_S%d' % (self._display.get_default_screen()))  
        self._net_system_tray_opcode = self._display.intern_atom(  
            '_NET_SYSTEM_TRAY_OPCODE')         

    def _create_window(self):
        """  
        Cria a janela do ícone da bandeja do sistema com as configurações apropriadas.  
        """   
        with display_manager(self._display):  
            screen = self._display.screen()  
            window = screen.root.create_window(  
                -1, -1, 1, 1, 0, screen.root_depth,  
                event_mask=Xlib.X.ExposureMask | Xlib.X.StructureNotifyMask,  
                window_class=Xlib.X.InputOutput  
            )  
            window.set_wm_class('%sSystemTrayIcon' % self.name, self.name)  
            window.set_wm_name(self.title)  
            window.set_wm_normal_hints(  
                flags=(Xlib.Xutil.PPosition | Xlib.Xutil.PSize | Xlib.Xutil.PMinSize),  
                min_width=24,  
                min_height=24  
            )  
            window.change_property(self._xembed_info, self._xembed_info, 32, [  
                self._XEMBED_VERSION,  
                self._XEMBED_MAPPED  
            ])  
            return window

    def _draw(self):
        """  
        Desenha o ícone na janela do sistema, tratando exceções se a janela não for válida.  
        """ 
        try:
            dim = self._window.get_geometry()
            self._assert_icon_data(dim.width, dim.height)
            self._window.put_pil_image(self._gc, 0, 0, self._icon_data)
        except Xlib.error.BadDrawable:
            pass

    def _assert_icon_data(self, width, height):
        """  
        Verifica se os dados do ícone estão corretos em relação às dimensões fornecidas.  
        """  
        if self._icon_data and self._icon_data.size == (width, height):
            return
        self._icon_data = Image.new('RGB', (width, height))
        self._icon_data.paste(self._icon.resize((width, height),Image.LANCZOS))
        self._icon_data.tostring = self._icon_data.tobytes

    def _assert_docked(self):
        """  
        Verifica se o ícone está ancorado à bandeja do sistema, acionando a ancoragem se necessário.  
        """  
        self._dock_window()
        assert self._systray_manager

    def _dock_window(self):
        """  
        Anexa a janela à bandeja do sistema, se um gerenciador de bandeja estiver disponível.  
        """  
        systray_manager = self._get_systray_manager()
        if not systray_manager:
            return
        self._systray_manager = systray_manager
        self._send_message(
                        self._systray_manager,
                        self._net_system_tray_opcode,
                        self._SYSTEM_TRAY_REQUEST_DOCK,
                        self._window.id
                        )
        systray_manager.change_attributes(event_mask=Xlib.X.StructureNotifyMask)
        self._display.flush()
        self._systray_manager = systray_manager

    def _undock_window(self):
        """  
        Desanexa a janela da bandeja do sistema, tratando a remoção.  
        """ 
        try:
            self._systray_manager.change_attributes(
                event_mask=Xlib.X.NoEventMask)
        except XError:
            self._log.error('Failed to stop notifications', exc_info=True)
        self._window.unmap()
        self._window.reparent(self._display.screen().root, 0, 0)
        self._systray_manager = None
        self._display.flush()

    def _get_systray_manager(self):
        """  
        Obtém o gerenciador de bandeja do sistema.  
        """ 
        self._display.grab_server()
        try:
            systray_manager = self._display.get_selection_owner(self._net_system_tray_sx)
        finally:
            self._display.ungrab_server()
        self._display.flush()
        if systray_manager != Xlib.X.NONE:
            return self._display.create_resource_object('window',systray_manager.id)

    def _send_message(self, window, client_type, l0=0, l1=0, l2=0, l3=0):
        """  
        Envia uma mensagem para a janela especificada.  
        """  
        self._display.send_event(
                            window,
                            Xlib.display.event.ClientMessage(
                                type=Xlib.X.ClientMessage,
                                client_type=client_type,
                                window=window.id,
                                data=(32,(Xlib.X.CurrentTime, l0, l1, l2, l3))
                                ),
                            event_mask=Xlib.X.NoEventMask)

    def _events(self):
        """  
        Executa um loop, gerenciando eventos da janela e do sistema.  
        """
        self._loop = True        
        while self._loop == True:
            event = self._display.next_event()
            if not event:
                break
            else:
                yield event