from PIL import Image
import streamlit as st
from funcoes import *
import cv2

st.set_page_config(page_title="Trabalho de Álgebra Linear")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Trasformações Lineares com imagens")
    st.write("Aqui estão algumas transformações que podemos fazer com as imagens")
    st.write("Quer acessar o projeto pelo GitHub? [Clique aqui](https://github.com/samucaaaaaa/Trabalho_AL)")
    if st.button("Clique para ir no projeto do GitHub :)"):
        site_url = "https://github.com/samucaaaaaa/Trabalho_AL"
        st.write(f'<meta http-equiv="refresh" content="0; url={site_url}" />', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.write("Clique no botão para alterar a imagem!")
    st.image("imagens/yuri.png") 

    imagem_yuri = Image.open("imagens/yuri.png")
    imagem_yuri_array = np.array(imagem_yuri)
    # Botão escure imagem

    # Opções de transformação
    transformacao = st.selectbox("Escolha a transformação:", ["Nenhum", "Escurecer Imagem", "Imagem Preto e Branco", "Rotacionar 90°", "Filtro quente",
                                                              "Inverter imagem", "Repetir imagem", "FIltro frio", "Filtro blur", "Redimensionar imagem",
                                                              "FIltro frio", "FIltro sepia", "Cor negativa"])

    # Imagem original
    #st.image("imagens/yuri.png", caption="Imagem Original")

    # Botão para aplicar a transformação selecionada
    if transformacao == "Escurecer Imagem":
        escurecer_imagem(imagem_yuri_array, 70)
        st.image("imagem_resultado.png", caption="Imagem Escurecida")

    if transformacao == "Imagem Preto e Branco":
        imagem_preto_branco(imagem_yuri_array)
        st.image("imagem_resultado.png")

    if transformacao == "Rotacionar 90°":
        rotaciona_90(imagem_yuri_array)
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
        repete_imagem(imagem_yuri_array, 7)
        st.image("imagem_resultado.png") 

    if transformacao == "FIltro frio":
        filtro_frio(imagem_yuri_array)
        st.image("imagem_resultado.png")  

    if transformacao == "Redimensionar imagem":
        redimensionar_imagem(imagem_yuri_array, 200, 700)
        st.image("imagem_resultado.png")  

    if transformacao == "Filtrar cor":
        filtro_cor(imagem_yuri_array)
        st.image("imagem_resultado.png")   

    if transformacao == "FIltro sepia":
        filtro_sepia(imagem_yuri_array)
        st.image("imagem_resultado.png") 

    if transformacao == "Cor negativa":
        cor_negativa(imagem_yuri_array)
        st.image("imagem_resultado.png")                    

with st.container():
    # Usa st.file_uploader para permitir o upload de imagens
    uploaded_file = st.file_uploader("Faça o upload de uma imagem", type=["jpg", "png", "jpeg"])
    # Verifica se um arquivo foi enviado
    if uploaded_file is not None:
        # Carrega a imagem original
        imagem_original = Image.open(uploaded_file)
        imagem_array = np.array(imagem_original)

        st.image(imagem_original, caption="Imagem Original", use_column_width=True)

        imagem_alterada = escurecer_imagem(imagem_array, 70, "dont show")
        caminho_da_imagem_alterada = "temp_imagem_alterada.png"
        imagem_alterada.save(caminho_da_imagem_alterada, format="PNG")
        st.image(imagem_alterada, caption="Imagem Alterada", use_column_width=True)
        # TODO: Criar um botão para download, tirando o download automático

        