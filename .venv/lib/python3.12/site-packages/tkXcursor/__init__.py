 
# -*- coding: utf-8 -*-  

# tkXcursor - Extensão para gerenciamento de cursores RGBA/animados   
# para widgets Tkinter sob X.org  

# Copyright (c) 2009 por Igor E. Novikov 
# 
# Versão 2.0.0 - 2024 Editado por Rafael A. Nunes  
#  
# Esta biblioteca é um software livre; você pode redistribuí-lo e/ou  
# modificá-lo sob os termos da GNU Library General Public  
# License, conforme publicado pela Free Software Foundation; seja  
# a versão 2 da Licença, ou (a seu critério) qualquer versão posterior.  
#  
# Esta biblioteca é distribuída na esperança de que seja útil,  
# mas SEM NENHUMA GARANTIA; sem mesmo a garantia implícita de  
# COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO. Veja a GNU  
# Library General Public License para mais detalhes.  
#  
# Você deve ter recebido uma cópia da GNU Library General Public  
# License junto com esta biblioteca; se não, escreva para a Free Software  
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  EUA

import os  
from . import _tkXcursor as tx  # Importa o módulo C  

class tkXcursorError(Exception):  
    """Exceção personalizada para erros do tkXcursor."""  
    pass  

def x_xcursor_supported(widget):  
    """  
    Verifica se o sistema suporta cursores ARGB/animados.  

    RETURN VALUE  
    A função retorna True/False dependendo do suporte do sistema para cursores ARGB/animados.  
    """  
    return tx.IsSupportedARGB(widget._w, widget.tk.interpaddr())  # Corrigido para IsSupportedARGB  

def x_load_cursor(widget, filename):  
    """  
    Carrega um Xcursor RGBA/animado personalizado a partir de um arquivo de recurso.  

    INPUT VALUES  
    widget - qualquer widget ou toplevel instanciado  
    filename - caminho absoluto ou relativo para o arquivo de recurso Xcursor  

    RETURN VALUE  
    A função retorna um valor inteiro que corresponde ao XID do cursor no lado do X11.  
    """  
    if not os.path.isfile(filename):  
        raise tkXcursorError('Arquivo de recurso Xcursor está faltando: ' + filename)  
    return tx.FilenameLoadCursor(widget._w, widget.tk.interpaddr(), filename)  # Corrigido para FilenameLoadCursor  

def x_set_cursor(widget, cursor_id):  
    """  
    Define um Xcursor RGBA/animado personalizado para o widget fornecido.  

    INPUT VALUES  
    widget - widget alvo  
    cursor_id - valor inteiro que corresponde ao XID do cursor no lado do X11  
    """  
    tx.SetCursor(widget._w, widget.tk.interpaddr(), cursor_id)  # Corrigido para SetCursor
