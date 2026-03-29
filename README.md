# pinterest-to-png
Script Python para baixar imagens do Pinterest e converter de JPEG para PNG - desenvolvido por ter problemas na instalação de imagens

# Pinterest JPEG → PNG Converter

Converte imagens do Pinterest de JPEG para PNG a partir de uma URL de pin.

## Instalação

pip install requests Pillow beautifulsoup4

## Como usar

1. Abra o arquivo pinterest_to_png.py
2. Troque o valor da variável URL pela URL do seu pin:

URL = "https://www.pinterest.com/pin/123456789/"

3. Execute:

python3 pinterest_to_png.py

## Saída

A imagem convertida é salva automaticamente na pasta pngs/, que é criada caso não exista.

Para mudar o destino, edite essa linha no código:

caminho = f"pngs/{nome_arquivo}.png"  # altere "pngs" para o caminho desejado

Exemplos:
- Windows: "C:/Users/voce/Imagens"
- Mac/Linux: "/home/voce/Documentos/pngs"

## Como funciona

1. buscar_url_da_imagem() — Acessa o pin e extrai a URL da imagem via meta tag og:image
2. baixar_imagem() — Baixa a imagem usando requests
3. converter_para_png() — Converte e salva como PNG usando Pillow

 ## Dependências

- requests — para fazer requisições HTTP
- Pillow — para abrir e converter imagens
- beautifulsoup4 — para extrair dados do HTML da página


## aviso
- toda vez que o usuario colocar outra url de uma nova imagem, a pasta onde a imagem interior, sera trocada e terá apenas aquela imagem na pasta. Isso foi feito intencionalmente para que não acumule imagens inuteís.
