# Autor:

Rafael A. Nunes (rafa.nunes2018@hotmail.com) 2024

# Aviso Importante:

O uso deste código deve ser realizado com cautela.
Qualquer defeito ou erro resultante da execução deste código não será de responsabilidade do autor, mas sim de quem o executar.
Certifique-se de entender completamente o que o código faz antes de utilizá-lo.

O código realiza o backup do executável do Python e utiliza o Resource Hacker para remover a pasta de ícones de um arquivo executável,
criando uma cópia no mesmo diretório do executável com um sufixo "2" no nome (Python2).

Para utilizar este código, é necessário ter o Windows, Python e o Visual Studio Code (VSCode) instalados em seu computador.
Certifique-se de que ambas as ferramentas estão instaladas corretamente.

Download do Python:
Você pode baixar a versão mais recente do Python através do site oficial: python.org/downloads

Download do Visual Studio Code:
O Visual Studio Code pode ser baixado no site oficial: code.visualstudio.com/Download


# Primeiro:
Criar ou Localizar o Atalho do VSCode:
Se você não tiver um atalho, crie um clicando com o botão direito no executável do VSCode e selecionando "Criar atalho".

# Segundo:
Modificar as Propriedades do Atalho:
Clique com o botão direito no atalho do VSCode e selecione "Propriedades".
Vá para a aba "Compatibilidade". Marque a opção "Executar este programa como administrador".
Clique em "OK" para confirmar.

## OBS:
Com essa configuração, toda vez que você iniciar o VSCode através desse atalho ou seu executável,
ele será executado com privilégios de administrador.

# Terceiro:
Abrir a pasta com os arquivos:
Se ainda não estiver aberto, inicie o Visual Studio Code.
No canto superior esquerdo, clique em Arquivo (ou File).
Selecione a opção "Abrir Pasta..." (ou "Open Folder...").
Navegue até a pasta que contenha os arquivos do código.
Selecione-a e clique no botão "Selecionar Pasta" (ou "Select Folder").

# Quarto:
Executar o código:
Abra o arquivo "remover_icon_do_python.py".
Clique no ícone de reprodução (play) no canto superior direito. ou:
Clique com o botão direito e selecione "Executar Python".
Clique em "Executar o arquivo do Python no Terminal".

# Quinto:
Selecionar o novo interpretador:
Abra o seu próprio arquivo Python (por exemplo um código tkinter). 
No canto inferior esquerdo da janela do VSCode, você verá a versão do Python atualmente em uso,
geralmente exibida como uma etiqueta (por exemplo, "Python 3.x.x").
Clique nessa etiqueta.
Isso abrirá uma lista de interpretadores disponíveis. Você verá opções de interpretadores detectados pelo VSCode.
Selecione o novo interpretador clicando em "Inserir caminho do interpretador" (ou "Enter interpreter path...").
Navegue até o novo interpretador Python2 e o escolha.

Agora o ícone do Python na barra de tarefas não terá um ícone padrão, podendo ser personalizado (por exemplo: iconbitmap ).

## OBS2:
Não é possível criar um ambiente virtual a partir do novo interpretador Python2.