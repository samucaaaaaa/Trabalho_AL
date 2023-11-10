from PIL import Image
import streamlit as st
from funcoes import *
import cv2

st.set_page_config(page_title="Trabalho de Álgebra Linear")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

with st.container():
    st.title("Trasformações Lineares com imagens")
    st.write("Aqui estão algumas transformações que podemos fazer com as imagens")
    st.write("Quer acessar o projeto pelo GitHub? [Clique aqui](https://github.com/samucaaaaaa/Trabalho_AL)")
    if st.button("Clique para ir no projeto do GitHub :)"):
        site_url = "https://github.com/samucaaaaaa/Trabalho_AL"
        st.write(f'<meta http-equiv="refresh" content="0; url={site_url}" />', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("Clique no botão para alterar a imagem!")
    st.image("imagens/yuri.png", caption="Imagem Original") 

    imagem_yuri = Image.open("imagens/yuri.png")
    imagem_yuri_array = np.array(imagem_yuri)
    # Botão escure imagem

    # Opções de transformação
    transformacao = st.selectbox("Escolha a transformação:", ["Nenhum", "Cor negativa", "Escurecer Imagem", "Filtrar cor", "Filtro blur",
                                                               "FIltro frio", "Filtro quente","FIltro sepia", "Imagem Preto e Branco",
                                                              "Inverter imagem",  "Repetir imagem", "Rotacionar 90°","Redimensionar imagem"])

    # TODO: Tentar tratar exceção nas funções que recebem tipo de imagem como parâmetro

    # Botão para aplicar a transformação selecionada
    if transformacao == "Escurecer Imagem":
        porcent_escurecimento = st.slider("Escolha a porcentagem de escurecimento:", 0, 100, 1)
        escurecer_imagem(imagem_yuri_array, porcent_escurecimento, "yes")
        st.image("imagem_resultado.png", caption="Imagem Escurecida")

    if transformacao == "Imagem Preto e Branco":
        imagem_preto_branco(imagem_yuri_array, "yes")
        st.image("imagem_resultado.png")

    if transformacao == "Rotacionar 90°":
        rotaciona_90(imagem_yuri_array, "yes")
        st.image("imagem_resultado.png") 

    if transformacao == "Filtro quente":
        filtro_quente(imagem_yuri_array)
        st.image("imagem_resultado.png")  

    if transformacao == "Inverter imagem":
        inverte_imagem(imagem_yuri_array)
        st.image("imagem_resultado.png")       

    if transformacao == "Filtro blur":
        imagem_yuri_array = cv2.imread("imagens/yuri.png")
        filtro_blur(imagem_yuri_array)
        st.image("imagem_resultado.png")    

    if transformacao == "Repetir imagem":
        n_repeticoes = st.slider("Escolha o número repetições:", 1, 10, 1)
        repete_imagem(imagem_yuri_array, n_repeticoes)
        st.image("imagem_resultado.png") 

    if transformacao == "FIltro frio":
        filtro_frio(imagem_yuri_array)
        st.image("imagem_resultado.png")  

    if transformacao == "Redimensionar imagem":
        altura = st.slider("Escolha a altura:", 100, 800, step=20)
        largura = st.slider("Escolha a largura", 100, 1000, step=20)
        redimensionar_imagem(imagem_yuri_array, altura, largura)
        st.image("imagem_resultado.png")  

    if transformacao == "Filtrar cor":
        cor = st.selectbox("Escolha a cor do filtro:", ["agua", "amarelo", "azul", "roxo", "verde", "vermelho"])
        filtro_cor(imagem_yuri_array, cor, "png")
        st.image("imagem_resultado.png")   

    if transformacao == "FIltro sepia":
        filtro_sepia(imagem_yuri_array, "png")
        st.image("imagem_resultado.png")   
                     
    if transformacao == "Cor negativa":
        cor_negativa(imagem_yuri_array)
        st.image("imagem_resultado.png") 

with st.container():
    st.write("---")
    st.write("Escolha uma imagem para fazer as transformações!")
    # Usa st.file_uploader para permitir o upload de imagens
    uploaded_file = st.file_uploader("Faça o upload de uma imagem", type=["jpg", "png", "jpeg"])
    # Verifica se um arquivo foi enviado
    if uploaded_file is not None:
        # Carrega a imagem original
        imagem_original = Image.open(uploaded_file)
        imagem_array = np.array(imagem_original)

        st.image(imagem_original, caption="Imagem Original", use_column_width=True)

        imagem_alterada = escurecer_imagem(imagem_array, 70, "no")
        imagem_alterada.save("temp_imagem_alterada.png")
        st.image(imagem_alterada, caption="Imagem Alterada", use_column_width=True)
    # TODO: Fazer um selectbox para o usuário escolher o tipo de transformação após realizar o upload da imagem    
        

        