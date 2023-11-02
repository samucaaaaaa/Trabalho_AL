import numpy as np
from PIL import Image

def escurecer_imagem(caminho_imagem, pct_escurecimento):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = imagem_array[:,:,canal_cor] * ((100-pct_escurecimento)/100)

    resultado = Image.fromarray(imagem_array)
    return resultado.save("imagem_resultado.png")

def imagem_preto_branco(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)
    
    imagem_array = np.dot(imagem_array[..., :3], [0.3, 0.59, 0.11])

    resultado = Image.fromarray(imagem_array)
    return resultado.save("imagem_resultado.png")

def rotacior_90(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    imagem_array = np.transpose(imagem_array, (1,0,2))
    resultado = Image.fromarray(imagem_array)
    return resultado.save("teste_img.png")
