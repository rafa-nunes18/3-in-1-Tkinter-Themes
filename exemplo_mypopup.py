# Documentação do MyPopup  

# Introdução  

# A classe `MyPopup` é uma ferramenta para exibir diálogos interativos no aplicativo.
# Ela permite a exibição de mensagens, bem como a solicitação de respostas do usuário, como confirmações e cancelamentos.  

# Exemplo de Uso  

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