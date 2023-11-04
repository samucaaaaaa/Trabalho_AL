import numpy as np
from PIL import Image
import cv2

def escurecer_imagem(caminho_imagem, pct_escurecimento):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = imagem_array[:,:,canal_cor] * ((100-pct_escurecimento)/100)

    return Image.fromarray(imagem_array)

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

    # imagem_array[:,:,0] = np.clip(imagem_array[:,:,2] * 1.2, 0, 255)
    # imagem_array[:,:,2] = np.clip(imagem_array[:,:,0] * 0.8, 0, 255)

    resultado = Image.fromarray(imagem_array)
    return resultado.save("imagem_resultado.png")

def inverte_imagem(caminho_imagem):
    
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)
    
    imagem_invertida_array = np.flip(imagem_array, 1)

    imagem_invertida = Image.fromarray(imagem_invertida_array)

    return imagem_invertida.save("imagem_resultado.png")

def filtro_blur(caminho_imagem):
    imagem = cv2.imread(caminho_imagem)
    matriz_filtro = np.ones((3, 3)) / 9

    imagem_borrada = cv2.filter2D(imagem, -1, matriz_filtro)

    return cv2.imwrite("imagem_resulatado.jpg", imagem_borrada)

def filtro_amarelo(caminho_da_imagem):
    imagem = Image.open(caminho_da_imagem)
    imagem_array = np.array(imagem)

    filtro_amarelo = np.array([1.5, 1.2, 0.8])
    imagem_transformada = imagem_array * filtro_amarelo

    imagem_transformada = np.clip(imagem_transformada, 0, 255)

    resultado = Image.fromarray(imagem_transformada.astype("uint8"))

    return resultado.save("imagem_resultado.png")

def repete_imagem(caminho_imagem, num_repeticoes):
    imagem = Image.open(caminho_imagem)
    
    imagem_array = np.array(imagem)

    imagem_array = imagem_array[:, :, :3]

    imagem_repeticoes_array = np.concatenate([imagem_array] * num_repeticoes, axis=1)
    imagem_repeticoes = Image.fromarray(imagem_repeticoes_array)

    return imagem_repeticoes.save("imagem_resultado.png")

def filtro_frio(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    imagem_array = np.array(imagem_array)

    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] * 1.2, 0, 255)
    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] * 0.8, 0, 255)

    imagem_filtrada = Image.fromarray(imagem_array)

    return imagem_filtrada.save("imagem_resultado.png")

def filtro_sepia(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    vermelho = imagem_array[:,:,0]
    verde = imagem_array[:,:,1]
    azul= imagem_array[:,:,2]
    
    sepia_vermelho= np.clip(0.393 * vermelho+ 0.769 * verde + 0.189 * azul, 0, 255)
    sepia_verde= np.clip(0.349 * vermelho+ 0.686 * verde + 0.168 * azul, 0, 255)
    sepia_azul= np.clip(0.272 * vermelho+ 0.534 * verde + 0.131 * azul, 0, 255)

    imagem_array[:,:,0] = sepia_vermelho
    imagem_array[:,:,1] = sepia_verde
    imagem_array[:,:,2] = sepia_azul
    
    imagem = Image.fromarray(imagem_array)

    return imagem.save("imagem_resultado.png")