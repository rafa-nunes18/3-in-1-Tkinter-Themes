"""
Autor:

Rafael A. Nunes (rafa.nunes2018@hotmail.com) 2024 

Aviso Importante:

O uso deste código deve ser realizado com cautela.
Qualquer defeito ou erro resultante da execução deste código não será de responsabilidade do autor, mas sim de quem o executar.
Certifique-se de entender completamente o que o código faz antes de utilizá-lo, leia "Instruções de uso.md" para mais informações.

Direitos e Condições:

Para que o código funcione corretamente, é necessário utilizar o programa Resource Hacker através de um comando do subprocess
(verifique as permissões do usuário).

Resource Hacker™
Um compilador e descompilador de recursos freeware para aplicativos do Windows®
Versão: 5.2.7
Última atualização: 19 de novembro de 2023
Copyright: © 1999-2023 Angus Johnson
E-mail: awj1958@gmail.com

Este software é essencial para a execução das funções que envolvem a modificação do executável.
É necessário ter o Windows, Python e o Visual Studio Code (VSCode) instalados em seu computador.
A ausência ou a versão inadequada das ferramentas pode resultar em falhas na operação do código.

Diretórios:

O arquivo de instruções "Instruções de uso.md" está localizado na pasta "\programa_auxiliar".
O programa Resource Hacker está localizado na pasta "\programa_auxiliar\remover_ico_de_exe".
O interpretador Python será encontrado com o comando sys.executable, que retorna o caminho do interpretador atual.
O novo interpretador Python2 estará no mesmo diretório do Python.

Testado com:

Windows 11 PRO , versão 23H2
Visual Studio Code , versão 1.93.1
Python , versão 3.12.6
Resource Hacker 5.2.7
"""

# Importações
import subprocess  
import os  
import shutil  
import sys  

def criar_backup():  
    # Obtém o caminho do executável Python  
    caminho_python = sys.executable  
   
    # Define o caminho do backup  
    caminho_backup = caminho_python + '.backup'  
    
    # Verifica se o backup nao existe então cria o backup  
    if not os.path.exists(caminho_backup):        
        shutil.copy(caminho_python, caminho_backup)  
        print(f"Backup criado em: {caminho_backup}")
    else:        
        print("O backup já existe.")      

def remove_icon_folder(resource_hacker_path, exe_path):  
    # Verifica se o caminho do Resource Hacker é válido  
    if not os.path.isfile(resource_hacker_path):  
        print(f"Erro: O caminho do Resource Hacker não é válido: {resource_hacker_path}")  
        return  

    # Verifica se o caminho do executável é válido  
    if not os.path.isfile(exe_path):  
        print(f"Erro: O caminho do executável não é válido: {exe_path}")  
        return   

    # O caminho de saída será uma copia do executável acrescentado 2 no final do nome 
    output_path =  os.path.splitext(exe_path)[0] + '2.exe' 

    # Exclui a a copia do executável caso ela exista 
    if os.path.isfile(output_path):  
        try:  
            os.remove(output_path)  # Remove o arquivo existente  
            print(f"O arquivo existente {output_path} foi deletado.")  
        except Exception as e:  
            print(f"Ocorreu um erro ao tentar deletar o arquivo {output_path}: {e}")
            return
        
    # Criando backup do python.exe  
    criar_backup() 

    # Comando do Resource Hacker para remover a pasta de ícones  
    command = f'"{resource_hacker_path}" -open "{exe_path}" -action delete -mask ICONGROUP,1,1033 -save "{output_path}"'  
    
    # Debug: Imprime o comando que será executado  
    print("Comando a ser executado:", command)  

    # Chama o Resource Hacker  
    try:  
        subprocess.run(command, shell=True, check=True)  
    except Exception as e:  
        print(f"Ocorreu um erro em executar o comando: {e}")   


# Caminho do Resource Hacker e do executável do Python  
caminho = os.getcwd() 
resource_hacker_path = os.path.join(caminho, "programa_auxiliar", "remover_ico_de_exe", "ResourceHacker.exe")  
exe_path = sys.executable   

# Executa a função para remover a pasta de ícones do executável  
remove_icon_folder(resource_hacker_path, exe_path)

