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
# Exemplos de uso de MyPopup

# Importar arquivo que contem a class MyPopup
from BoxDialog import MyPopup  

# Função de exemplo para chamar todos os tipos de MyPopup
def chamar_popups(root):
    # Exibir uma mensagem de erro sobre WiFi ou arquivo para cada tipo.
    
    pop = MyPopup(root)  

    # Nesse primeiro exemplo será modificado o icone , a fonte , e os tamanhos de titulo e detalhes.    
    pop.show_mensagem("Você está sem internet",  
                       "Confira sua conexão, verifique se o cabo de rede está desconectado ou se existe sinal de WiFi!",  
                       icon="erro",
                       font=("impact.ttf", 20, 15)
                       )  
    
    # Nesse segundo exemplo será modificado apenas os tamanhos de titulo e detalhes. 
    resposta_cancelar = pop.ask_sim_cancelar("WiFi não conectado", "Fechar o aplicativo?",font=(40, 10))  
    if resposta_cancelar is not None:          
        if resposta_cancelar:  
            print("Usuário escolheu: Fechar o aplicativo.")            
        else:  
            print("Usuário escolheu: Não fechar o aplicativo.")

    # Nos exemplos seguintes será usado os padrões de MyPopup.
    resposta_nao = pop.ask_sim_nao("WiFi não conectado", "Deseja continuar em modo Offline?")  
    print(f"Resposta do popup 'ask_sim_nao': {resposta_nao}")   
     
    resposta_substituir = pop.ask_sim_nao_cancelar("Arquivo já existente", "Deseja substituí-lo?")      
    if resposta_substituir is not None:  
        if resposta_substituir:  
            print("Usuário escolheu: Substituir arquivo.")             
        else:  
            print("Usuário escolheu: Não substituir arquivo.")  

    resposta_repetir = pop.ask_repetir_cancelar("Arquivo não encontrado", "Repetir a busca?")  
    print(f"Resposta do popup 'ask_repetir_cancelar': {resposta_repetir}")  

    resposta_aceitar = pop.ask_aceitar_recusar("Termos de adesão", "Aceita os termos e a política da empresa?")  
    print(f"Resposta do popup 'ask_aceitar_recusar': {resposta_aceitar}")