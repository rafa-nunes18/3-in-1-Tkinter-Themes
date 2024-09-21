from PIL import Image  

def redimensionar_e_salvar_imagem_ico(caminho_png, caminho_saida):  
    try:  
        # Abre a imagem ICO  
        imagem = Image.open(caminho_png)  
        
        # Redimensiona a imagem para 32x32 pixels  
        imagem_redimensionada = imagem.resize((64, 64), Image.LANCZOS)  
        
        # Salva a imagem redimensionada como CUR  
        imagem_redimensionada.save(caminho_saida, format='png')  
        print("Imagem redimensionada e salva como png com sucesso!")  

    except Exception as e:  
        print(f"Ocorreu um erro: {e}")  

# Chama a função  
redimensionar_e_salvar_imagem_ico(r"imagens/cursores/cursor-cry-x.png", r"imagens\icons\icone-padrao-64x64.png")