from PIL import Image  

# Carrega a imagem existente (substitua pelo caminho da sua imagem)  
image_path = "imagens/icons/icone-padrao.ico"  # Substitua pelo caminho correto da sua imagem  
output_icon_path = "icone-padrao.ico"  # Nome do arquivo de saída  

# Abre a imagem  
try:  
    img = Image.open(image_path)  

    # Redimensiona a imagem para 64x64 pixels (tamanho comum para ícones)  
    img = img.resize((32, 32), Image.LANCZOS)  

    # Salva a imagem como um arquivo .ico  
    img.save(output_icon_path, format='ICO')  
    print(f"Ícone criado com sucesso: {output_icon_path}")  

except Exception as e:  
    print(f"Erro ao criar o ícone: {e}") 