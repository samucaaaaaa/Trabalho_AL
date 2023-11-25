import cv2
import numpy as np
from PIL import Image
import streamlit as st

def escurecer_imagem(imagem_array, pct_escurecimento, salvar=False):

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = imagem_array[:,:,canal_cor] * ((100-pct_escurecimento)/100)

    resultado = Image.fromarray(imagem_array.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)

    if salvar == True:
        resultado.save("imagem_resultado.png")


def imagem_preto_branco(imagem_array, salvar=False):

    imagem_array = np.dot(imagem_array[..., :3], [0.3, 0.59, 0.11])
    
    resultado = Image.fromarray(imagem_array.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def rotaciona_90(imagem_array, salvar=False):

    imagem_array = np.transpose(imagem_array, (1,0,2))
    
    resultado = Image.fromarray(imagem_array.astype("uint8"))
    
    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def filtro_quente(imagem_array, salvar=False):

    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] * 1.2, 0, 255)
    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] * 0.8, 0, 255)

    resultado = Image.fromarray(imagem_array.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def inverte_imagem(imagem_array, eixo, salvar=False):
    
    if eixo == "Horizontal":
        eixo = 0
    elif eixo == "Vertical":
        eixo = 1
    imagem_invertida_array = np.flip(imagem_array, eixo)

    resultado = Image.fromarray(imagem_invertida_array.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def repete_imagem(imagem_array, num_repeticoes, salvar=False):

    imagem_array = imagem_array[:, :, :3]
    imagem_repeticoes_array = np.concatenate([imagem_array] * num_repeticoes, axis=1)
    
    resultado = Image.fromarray(imagem_repeticoes_array)

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")

def filtro_frio(imagem_array, salvar=False):

    imagem_array[:,:,2] = np.clip(imagem_array[:,:,2] * 1.2, 0, 255)
    imagem_array[:,:,0] = np.clip(imagem_array[:,:,0] * 0.8, 0, 255)

    resultado = Image.fromarray(imagem_array.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def redimensionar_imagem(imagem_array, altura, largura, salvar=False, apenas_salvamento=False):

    altura_original, largura_original = imagem_array.shape[:2]

    x_indices = (np.arange(largura) * largura_original / largura).astype(int)
    y_indices = (np.arange(altura) * altura_original / altura).astype(int)

    imagem_redimensionada_array = imagem_array[np.ix_(y_indices, x_indices)]
    
    imagem_redimensionada = Image.fromarray(imagem_redimensionada_array.astype("uint8"))

    if apenas_salvamento == True:
        return imagem_redimensionada.save("imagem_resultado.png")
    elif salvar == True:
        imagem_redimensionada.save("imagem_resultado.png")
        
    centralize_widget(st.image, imagem_redimensionada, caption="Imagem Alterada", width=377)
    

def filtro_blur(imagem_array, qnt_blur, salvar=False):
    redimensionar_imagem(imagem_array, imagem_array.shape[0] / qnt_blur, imagem_array.shape[1] / qnt_blur, apenas_salvamento=True)
    
    imagem = Image.open("imagem_resultado.png")
    imagem_borrada_array = np.array(imagem)
    
    redimensionar_imagem(imagem_borrada_array, imagem_array.shape[0] * qnt_blur, imagem_array.shape[1] * qnt_blur, apenas_salvamento=True)
    
    imagem = Image.open("imagem_resultado.png")
    imagem_borrada_array = np.array(imagem)

    resultado = Image.fromarray(imagem_borrada_array.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")
    

def filtro_cor(imagem_array, cor, tipo_imagem=None, salvar=False):
    
    if cor.lower() == "vermelho":
        proporcoes = [1.5,1,1]
    elif cor.lower() == "verde":
        proporcoes = [1,1.5,1]
    elif cor.lower() == "azul":
        proporcoes = [0.5,1,2]
    elif cor.lower() == "roxo":
        proporcoes = [0.8,0.5,1.2]
    elif cor.lower() == "amarelo":
        proporcoes = [1.5, 1.2, 0.5]
    elif cor.lower() == "água":
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
        return "Erro"
    else:
        resultado = Image.fromarray(imagem_transformada.astype("uint8"))

        centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
        if salvar == True:
            resultado.save("imagem_resultado.png")


def filtro_sepia(imagem_array, tipo_imagem=None, salvar=False):
    if tipo_imagem == "png":
        matriz_correcao = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]).reshape(4,3)
        imagem = np.dot(imagem_array, matriz_correcao)
    else:
        imagem = Image.fromarray(imagem_array)

    sepia_filter = np.array([[0.393, 0.349, 0.272], [0.769, 0.686, 0.534], [0.189, 0.168, 0.131]])
    
    try:
        imagem_transformada = np.dot(imagem,sepia_filter)
        imagem_transformada = np.clip(imagem_transformada,0,255)
    except Exception:
        st.write(f"A imagem passada não é do tipo {tipo_imagem}")
    else:
        # Aumentando o amarelo para se adequar ao filtro sépia
        imagem_transformada[..., 0] *= 1.2
        imagem_transformada[..., 1] *= 1.2
        imagem_transformada = np.clip(imagem_transformada, 0, 255)
        
        resultado = Image.fromarray(imagem_transformada.astype("uint8"))

        centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
        if salvar == True:
            resultado.save("imagem_resultado.png")


def cor_negativa(imagem_array, salvar=False):

    for canal_cor in range(0,3):
        imagem_array[:,:,canal_cor] = 255 - imagem_array[:,:,canal_cor]

    
    resultado = Image.fromarray(imagem_array.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def filtro_cimento(imagem_array, shift, salvar=False):

    if shift == 0:
        return centralize_widget(st.image, imagem_array, caption="Imagem Sem Alteração", width=377)
    
    # Convertendo a imagem para escala de cinza
    imagem_cinza = imagem_array.mean(axis=2)

    # Aplicar um filtro de borda
    bordas = imagem_cinza - np.roll(imagem_cinza, shift=shift, axis=0)

    # Inverter as cores
    imagem_cimentada = 255 - bordas

    # Normalizar para o intervalo 0-255
    imagem_cimentada = (imagem_cimentada / np.max(imagem_cimentada) * 255).astype(np.uint8)

    # Ajustar o contraste da imagem

    resultado = Image.fromarray(imagem_cimentada)

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def contorno_imagem(imagem_array, salvar):
    # Recebendo os parâmetros com próprio shape, a função redimencionar_imagem apenas retorna um caminho para a imagem original
    # Isso garaante o funcionamento da função
    redimensionar_imagem(imagem_array, imagem_array.shape[0], imagem_array.shape[1], apenas_salvamento=True)

    # Convertendo a imagem sem as cores
    imagem = Image.open("imagem_resultado.png").convert("L")
    imagem = np.array(imagem)

    # Definindo o kernel do operador de Sobel
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Aplicando o operador de Sobel
    bordas_x = np.convolve(imagem.flatten(), sobel_x.flatten(), mode="same").reshape(imagem.shape)
    bordas_y = np.convolve(imagem.flatten(), sobel_y.flatten(), mode="same").reshape(imagem.shape)

    # Calculando a magnitude das bordas
    bordas = np.hypot(bordas_x, bordas_y)

    # Normalizando para o intervalo 0-255
    bordas = (bordas / np.max(bordas) * 255)
    # bordas = np.clip(bordas, 0, 255).astype(np.uint8)

    resultado = Image.fromarray(bordas.astype(np.uint8))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")
    

def transladar_imagem(imagem_array, translacao_x, translacao_y, salvar=False):
    altura, largura, _ = imagem_array.shape

    # Criando uma matriz de zeros com o mesmo formato da imagem
    imagem_transladada = np.zeros_like(imagem_array)

    # Calculando as novas coordenadas após a translação
    nova_posicao_x = np.clip(np.arange(largura) + translacao_x, 0, largura - 1)
    nova_posicao_y = np.clip(np.arange(altura) + translacao_y, 0, altura - 1)

    # Usando broadcasting para atribuir os valores da imagem original para as novas coordenadas
    imagem_transladada[nova_posicao_y[:, np.newaxis], nova_posicao_x, :] = imagem_array[:, :, :]

    resultado = Image.fromarray(imagem_transladada.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")
    

def rotaciona_imagem(imagem_array, angulo, salvar=False):
    altura, largura, _ = imagem_array.shape

    # Calculando o centro da imagem
    centro = (largura // 2, altura // 2)

    # criando a matriz de rotação afim
    matriz_rotacao = cv2.getRotationMatrix2D(centro, angulo, 1.0)

    # Aplicando a rotação afim na imagem
    imagem_rotacionada = cv2.warpAffine(imagem_array, matriz_rotacao, (largura, altura), flags=cv2.INTER_LINEAR)

    resultado = Image.fromarray(imagem_rotacionada.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        resultado.save("imagem_resultado.png")


def compressão_imagem_svd(imagem_array, prop_k, tipo_imagem="jpg", salvar=False):
    
    k = imagem_array.shape[1] // prop_k
        
    if tipo_imagem == "png":
        matriz_correcao = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]).reshape(4,3)
        imagem = np.dot(imagem_array, matriz_correcao)
    
    else:
        imagem = imagem_array
    
    # Normalizando os dados da imagem usando Min-Max
    imagem = (imagem - np.min(imagem)) / (np.max(imagem) - np.min(imagem))

    # Realizando a decomposição SVD para cada entrada de cor e reconstruindo a imagem usando apenas os k maiores valores singulares 
    array_r = imagem[:,:, 0]
    U, Σ, V_T = np.linalg.svd(array_r)
  
    array_r_filtrado =  U[:, :k] @ np.diag(Σ[:k]) @ V_T[:k, :]
    
    array_g = imagem[:,:, 1]
    U, Σ, V_T = np.linalg.svd(array_g)
      
    array_g_filtrado =  U[:, :k] @ np.diag(Σ[:k]) @ V_T[:k, :]
    
    array_b = imagem[:,:, 2]
    U, Σ, V_T = np.linalg.svd(array_b)
 
    array_b_filtrado =  U[:, :k] @ np.diag(Σ[:k]) @ V_T[:k, :]

    imagem[:,:, 0] = array_r_filtrado
    imagem[:,:, 1] = array_g_filtrado
    imagem[:,:, 2] = array_b_filtrado
    # Alterando o intervalo para 0 a 1
    imagem_array_filtrado = np.clip(imagem, 0, 1)

    # Convertendo de volta para o intervalo de 0 a 255
    imagem_array_filtrado = imagem_array_filtrado * 255
    
    resultado = Image.fromarray(imagem_array_filtrado.astype("uint8"))

    centralize_widget(st.image, resultado, caption="Imagem Alterada", width=377)
    
    if salvar == True:
        try:
            resultado.save("imagem_resultado.jpg")
            with open("imagem_resultado.jpg", "rb") as imagem_resultado:
                imagem_bytes = imagem_resultado.read()

            st.download_button("Confirmar o Download da nova imagem", imagem_bytes, "imagem_resultado.jpg", "image/jpg")

        except OSError:
            resultado.save("imagem_resultado.png") 
            
            with open("imagem_resultado.png", "rb") as imagem_resultado:
                imagem_bytes = imagem_resultado.read()

            st.download_button("Confirmar o Download da nova imagem", imagem_bytes, "imagem_resultado.png", "image/png") 


def transformacao(transformacao, imagem_array, tipo_imagem="jpg", salvar=False, key_widgets="teste"):
    if transformacao == "Escurecer Imagem":
        porcent_escurecimento = st.slider("Escolha a porcentagem de escurecimento:", 0, 100, 1, key=f"slider {key_widgets} esc")
        escurecer_imagem(imagem_array, porcent_escurecimento, salvar)

    if transformacao == "Imagem Preto e Branco":
        imagem_preto_branco(imagem_array, salvar)

    if transformacao == "Rotacionar 90°":
        rotaciona_90(imagem_array, salvar)

    if transformacao == "Filtro Quente":
        filtro_quente(imagem_array, salvar)  

    if transformacao == "Inverter Imagem":
        eixo = st.selectbox("Escolha como inverter a imagem:", ["Horizontal", "Vertical"], key=f"selectbox {key_widgets} inverção")
        inverte_imagem(imagem_array, eixo, salvar)       

    if transformacao == "Filtro Blur":
        intensidade = st.slider("Escolha a intensidade do blur:", 1, 10, 1, key=f"slider {key_widgets} blur")
        filtro_blur(imagem_array, intensidade, salvar)    

    if transformacao == "Repetir Imagem":
        n_repeticoes = st.slider("Escolha o número repetições:", 1, 10, 1, key=f"slider {key_widgets} repetições")
        repete_imagem(imagem_array, n_repeticoes, salvar)
        
    if transformacao == "Filtro Frio":
        filtro_frio(imagem_array, salvar)  

    if transformacao == "Redimensionar Imagem":
        altura = st.slider("Escolha a altura:", 100, 800,imagem_array.shape[0], step=20, key=f"slider {key_widgets} altura")
        largura = st.slider("Escolha a largura", 100, 1000, imagem_array.shape[1], step=20, key=f"slider {key_widgets} largura")
        redimensionar_imagem(imagem_array, altura, largura, salvar)

    if transformacao == "Filtrar Cor":
        cor = st.selectbox("Escolha a cor do filtro:", ["Água", "Amarelo", "Azul", "Roxo", "Verde", "Vermelho"], key=f"selectbox {key_widgets} filtra cor")
        filtro_cor(imagem_array, cor, tipo_imagem, salvar)   

    if transformacao == "Filtro Sépia":
        filtro_sepia(imagem_array, tipo_imagem, salvar)
                        
    if transformacao == "Cor Negativa":
        cor_negativa(imagem_array, salvar)
    
    if transformacao == "Filtro Cimento":
        shift = st.slider("Escolha o nível de relevo:", -5, 5, 0, key=f"slider {key_widgets} cimento")
        filtro_cimento(imagem_array, shift, salvar)
    
    if transformacao == "Contorno Imagem":
        contorno_imagem(imagem_array, salvar)
    
    if transformacao == "Comprimir Imagem":
        proporcao_k = st.slider("Escolha o nível de compressão:", 2, 20, 2, key=f"slider {key_widgets} compressão")
        compressão_imagem_svd(imagem_array, proporcao_k, tipo_imagem, salvar)

    if transformacao == "Transladar Imagem":
        translacao_x = st.slider(f"Escolha o X:", -900, 900, 0, key=f"translacao_x{key_widgets}")
        translacao_y = st.slider(f"Escolha o Y:", -900, 900, 0, key=f"translacao_y{key_widgets}")
        transladar_imagem(imagem_array, translacao_x, translacao_y, salvar)  

    if transformacao == "Rotacionar Imagem":
        angulo_rotacao = st.slider("Ângulo de Rotação", -180, 180, 0, key=f"angulo_rotacao{key_widgets}")    
        rotaciona_imagem(imagem_array, angulo_rotacao, salvar)  


def centralize_widget(widget, *args, **kwargs):
    col2 = st.columns([2,5,2])[1]
    with col2:
        widget(*args, **kwargs)
