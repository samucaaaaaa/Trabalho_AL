import numpy as np
from PIL import Image
import cv2

def escurecer_imagem(imagem_array, pct_escurecimento, escolhe_salvar):

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = imagem_array[:,:,canal_cor] * ((100-pct_escurecimento)/100)

    resultado = Image.fromarray(imagem_array.astype("uint8"))

    if escolhe_salvar == "yes":
        return resultado.save("imagem_resultado.png")
    elif escolhe_salvar == "no":
        return resultado

def imagem_preto_branco(imagem_array, escolhe_salvar):

    imagem_array = np.dot(imagem_array[..., :3], [0.3, 0.59, 0.11])
    
    resultado = Image.fromarray(imagem_array.astype("uint8"))

    if escolhe_salvar == "yes":
        return resultado.save("imagem_resultado.png")
    elif escolhe_salvar == "no":
        return resultado

def rotaciona_90(imagem_array, escolhe_salvar):

    imagem_array = np.transpose(imagem_array, (1,0,2))
    
    resultado = Image.fromarray(imagem_array.astype("uint8"))
    
    if escolhe_salvar == "yes":
        return resultado.save("imagem_resultado.png")
    elif escolhe_salvar == "no":
        return resultado

def filtro_quente(imagem_array):

    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] * 1.2, 0, 255)
    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] * 0.8, 0, 255)

    resultado = Image.fromarray(imagem_array.astype("uint8"))
    return resultado.save("imagem_resultado.png")

def inverte_imagem(imagem_array):
    
    imagem_invertida_array = np.flip(imagem_array, 1)

    imagem_invertida = Image.fromarray(imagem_invertida_array.astype("uint8"))
    return imagem_invertida.save("imagem_resultado.png")

def filtro_blur(imagem):

    matriz_filtro = np.ones((3, 3), np.float32) / 9

    imagem_borrada = cv2.filter2D(imagem, -1, matriz_filtro)

    return cv2.imwrite("imagem_resultado.png", imagem_borrada)

def repete_imagem(imagem_array, num_repeticoes):

    imagem_array = imagem_array[:, :, :3]
    imagem_repeticoes_array = np.concatenate([imagem_array] * num_repeticoes, axis=1)
    
    imagem_repeticoes = Image.fromarray(imagem_repeticoes_array)
    return imagem_repeticoes.save("imagem_resultado.png")

def filtro_frio(imagem_array):

    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] * 1.2, 0, 255)
    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] * 0.8, 0, 255)

    imagem_filtrada = Image.fromarray(imagem_array.astype("uint8"))
    return imagem_filtrada.save("imagem_resultado.png")

def redimensionar_imagem(imagem_array, altura, largura):

    altura_original, largura_original = imagem_array.shape[:2]

    x_indices = (np.arange(largura) * largura_original / largura).astype(int)
    y_indices = (np.arange(altura) * altura_original / altura).astype(int)

    imagem_redimensionada_array = imagem_array[np.ix_(y_indices, x_indices)]
    
    imagem_redimensionada = Image.fromarray(imagem_redimensionada_array.astype("uint8"))
    return imagem_redimensionada.save("imagem_resultado.png")

def filtro_cor(imagem_array, cor):
    
    if cor.lower() == "vermelho":
        proporcoes = [1.5,1,1]
    elif cor.lower() == "verde":
        proporcoes = [1,1.5,1]
    elif cor.lower() == "azul":
        proporcoes = [1,1,1.5]
    elif cor.lower() == "roxo":
        proporcoes = [1.5,1,1.5]
    elif cor.lower() == "amarelo":
        proporcoes = [1.5, 1.2, 0.8]
    elif cor.lower() == "agua":
        proporcoes = [1,1.5,1.5]

    filtro = np.array(proporcoes)
    
    imagem_transformada = imagem_array * filtro
    imagem_transformada = np.clip(imagem_transformada, 0, 255)

    resultado = Image.fromarray(imagem_transformada.astype("uint8"))
    return resultado.save("imagem_resultado.png")

def filtro_sepia(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_array = np.array(imagem)

    sepia_filter = np.array([[.393, .769, .189],
                            [.349, .686, .168],
                            [.272, .534, .131]])

    imagem = Image.fromarray(imagem_array)

    imagem_transformada = np.dot(imagem,sepia_filter.T)
    imagem_transformada = np.clip(imagem_transformada,0,255)

    # Aumentando o amarelo para se adequar ao filtro sépia
    imagem_transformada[..., 0] *= 1.2
    imagem_transformada[..., 1] *= 1.2
    imagem_transformada = np.clip(imagem_transformada, 0, 255)
    
    resultado = Image.fromarray(imagem_transformada.astype("uint8"))
    return resultado.save("imagem_resultado.png")

def cor_negativa(imagem_array):

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = 255 - imagem_array[:,:,canal_cor]

    
    resultado = Image.fromarray(imagem_array.astype("uint8"))
    return resultado.save("imagem_resultado.png")
