import numpy as np
from PIL import Image
import cv2

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
    return resultado.save("imagem_resultado.png")

def filtro_quente(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] + 30, 0, 255).astype(np.uint8)
    imagem_array[:,:,1] = np.clip(imagem_array[:,:,1] + -10, 0, 255).astype(np.uint8)
    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] + -10, 0, 255).astype(np.uint8)

    resultado = Image.fromarray(imagem_array)
    return resultado.save("imagem_resultado.png")

def inverte_imagem(caminho_imagem):
    
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    matriz_transf = np.array([[-1, 0, imagem_array.shape[1]], [0, 1, 0], [0, 0, 1]])

    imagem_invertida_array = np.matmul(matriz_transf, imagem_array)

    imagem_invertida = Image.fromarray(imagem_invertida_array)

    return imagem_invertida.save("imagem_resultado.png")

def filtro_blur(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    matriz_filtro = np.ones((3, 3), np.float32) / 9

    imagem_borrada = cv2.filter2D(imagem, -1, matriz_filtro)

    return cv2.imwrite("imagem_resulatado.jpg", imagem_borrada)
