import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import os

# URL do pin do Pinterest que você quer converter
URL = "https://br.pinterest.com/pin/419960734028592872/"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
}


def buscar_url_da_imagem(url_pinterest):
   

    response = requests.get(url_pinterest, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

   
    og_image = soup.find("meta", property="og:image")

    if og_image:
        return og_image["content"]
    else:
        raise Exception("Imagem não encontrada. Verifique se a URL é de um pin específico.")


def baixar_imagem(url_imagem):
    

    response = requests.get(url_imagem, headers=HEADERS)
    imagem = Image.open(BytesIO(response.content))
    return imagem


def converter_para_png(imagem, nome_arquivo):
    
  

    # Garante que a imagem está em RGB (necessário para salvar como PNG sem erros)
    if imagem.mode != "RGB":
        imagem = imagem.convert("RGB")

    caminho = f"pngs/{nome_arquivo}.png"  # <-- altere "pngs" para o caminho que desejar. Ex: "C:/Users/voce/Imagens"
    imagem.save(caminho, format="PNG")
    print(f"Imagem salva como: {caminho}")




url_imagem = buscar_url_da_imagem(URL)
print(f"URL da imagem encontrada: {url_imagem}")

imagem = baixar_imagem(url_imagem)
print(f"Imagem baixada: {imagem.width}x{imagem.height}px")

converter_para_png(imagem, "imagem_convertida")
