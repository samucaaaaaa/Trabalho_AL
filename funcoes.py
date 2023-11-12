import numpy as np
from PIL import Image
import cv2
from streamlit import image


def escurecer_imagem(imagem_array, pct_escurecimento, salvar=False):

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = imagem_array[:,:,canal_cor] * ((100-pct_escurecimento)/100)

    resultado = Image.fromarray(imagem_array.astype("uint8"))

    if salvar == True:
        return resultado.save("imagem_resultado.png"), image(resultado, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(resultado, caption="Imagem Alterada", width=377)


def imagem_preto_branco(imagem_array, salvar=False):

    imagem_array = np.dot(imagem_array[..., :3], [0.3, 0.59, 0.11])
    
    resultado = Image.fromarray(imagem_array.astype("uint8"))

    if salvar == True:
        return resultado.save("imagem_resultado.png"), image(resultado, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(resultado, caption="Imagem Alterada", width=377)


def rotaciona_90(imagem_array, salvar=False):

    imagem_array = np.transpose(imagem_array, (1,0,2))
    
    resultado = Image.fromarray(imagem_array.astype("uint8"))
    
    if salvar == True:
        return resultado.save("imagem_resultado.png"), image(resultado, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(resultado, caption="Imagem Alterada", width=377)


def filtro_quente(imagem_array, salvar=False):

    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] * 1.2, 0, 255)
    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] * 0.8, 0, 255)

    resultado = Image.fromarray(imagem_array.astype("uint8"))

    if salvar == True:
        return resultado.save("imagem_resultado.png"), image(resultado, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(resultado, caption="Imagem Alterada", width=377)


def inverte_imagem(imagem_array, salvar=False):
    
    imagem_invertida_array = np.flip(imagem_array, 1)

    imagem_invertida = Image.fromarray(imagem_invertida_array.astype("uint8"))

    if salvar == True:
        return imagem_invertida.save("imagem_resultado.png"), image(imagem_invertida, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(imagem_invertida, caption="Imagem Alterada", width=377)


def filtro_blur(imagem, salvar=False):

    matriz_filtro = np.ones((3, 3), np.float32) / 9

    imagem_borrada = cv2.filter2D(imagem, -1, matriz_filtro)
    
    if salvar == True:
        return cv2.imwrite("imagem_resultado.png", imagem_borrada)
    else:
        return image(imagem_borrada, caption="Imagem Alterada", width=377)


def repete_imagem(imagem_array, num_repeticoes, salvar=False):

    imagem_array = imagem_array[:, :, :3]
    imagem_repeticoes_array = np.concatenate([imagem_array] * num_repeticoes, axis=1)
    
    imagem_repeticoes = Image.fromarray(imagem_repeticoes_array)

    if salvar == True:
        return imagem_repeticoes.save("imagem_resultado.png"), image(imagem_repeticoes, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(imagem_repeticoes, caption="Imagem Alterada", width=377)


def filtro_frio(imagem_array, salvar=False):

    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] * 1.2, 0, 255)
    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] * 0.8, 0, 255)

    imagem_filtrada = Image.fromarray(imagem_array.astype("uint8"))

    if salvar == True:
        return imagem_filtrada.save("imagem_resultado.png"), image(imagem_filtrada, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(imagem_filtrada, caption="Imagem Alterada", width=377)


def redimensionar_imagem(imagem_array, altura, largura, salvar=False):

    altura_original, largura_original = imagem_array.shape[:2]

    x_indices = (np.arange(largura) * largura_original / largura).astype(int)
    y_indices = (np.arange(altura) * altura_original / altura).astype(int)

    imagem_redimensionada_array = imagem_array[np.ix_(y_indices, x_indices)]
    
    imagem_redimensionada = Image.fromarray(imagem_redimensionada_array.astype("uint8"))

    if salvar == True:
        return imagem_redimensionada.save("imagem_resultado.png"), image(imagem_redimensionada, caption="Imagem Alterada", width=imagem_array.shape[1])
    elif salvar == False:
        return image(imagem_redimensionada, caption="Imagem Alterada", width=377)


def filtro_cor(imagem_array, cor, tipo_imagem=None, salvar=False):
    
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
    
    if tipo_imagem == "png":
        matriz_correcao = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]).reshape(4,3)
        imagem_array = np.dot(imagem_array, matriz_correcao)
    else:
        imagem_array = Image.fromarray(imagem_array)
    
    filtro = np.array(proporcoes)
    
    try:
        imagem_transformada = imagem_array * filtro
        imagem_transformada = np.clip(imagem_transformada, 0, 255)
    
    except Exception:
        print(f"A imagem passada não é do tipo {tipo_imagem}")
    else:
        resultado = Image.fromarray(imagem_transformada.astype("uint8"))

    if salvar == True:
        return resultado.save("imagem_resultado.png"), image(resultado, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(resultado, caption="Imagem Alterada", width=377)


def filtro_sepia(imagem_array, tipo_imagem=None, salvar=False):
    if tipo_imagem == "png":
        matriz_correcao = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]).reshape(4,3)
        imagem = np.dot(imagem_array, matriz_correcao)
    else:
        imagem = Image.fromarray(imagem_array)

    sepia_filter = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])
    
    try:
        imagem_transformada = np.dot(imagem,sepia_filter.T)
        imagem_transformada = np.clip(imagem_transformada,0,255)
    except Exception:
        return f"A imagem passada não é do tipo {tipo_imagem}"
    else:
        # Aumentando o amarelo para se adequar ao filtro sépia
        imagem_transformada[..., 0] *= 1.2
        imagem_transformada[..., 1] *= 1.2
        imagem_transformada = np.clip(imagem_transformada, 0, 255)
        
        resultado = Image.fromarray(imagem_transformada.astype("uint8"))

    if salvar == True:
        return resultado.save("imagem_resultado.png"), image(resultado, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(resultado, caption="Imagem Alterada", width=377)


def cor_negativa(imagem_array, salvar=False):

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = 255 - imagem_array[:,:,canal_cor]

    
    resultado = Image.fromarray(imagem_array.astype("uint8"))

    if salvar == True:
        return resultado.save("imagem_resultado.png"), image(resultado, caption="Imagem Alterada", width=377)
    elif salvar == False:
        return image(resultado, caption="Imagem Alterada", width=377)
