import numpy as np
from PIL import Image

def escurecer_imagem(caminho_imagem, pct_escurecimento):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    for canal in range(0,3):
        imagem_array[:,:,canal] = imagem_array[:,:,canal] * (100-pct_escurecimento)/100

    resultado = Image.fromarray(imagem_array)
    return resultado.save("imagem_resultado.png")
