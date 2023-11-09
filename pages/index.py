from PIL import Image
import streamlit as st
from funcoes import *

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

    # Botão escure imagem
    if st.button("Escurecer Imagem"):
        escurecer_imagem("imagens/yuri.png", 70, "show")

    # Botão imagem preto e branco
    if st.button("Imagem preto e branco"):
        imagem_preto_branco("imagens/yuri.png", "show")    

with st.container():
    # Usa st.file_uploader para permitir o upload de imagens
    uploaded_file = st.file_uploader("Faça o upload de uma imagem", type=["jpg", "png", "jpeg"])
    # Verifica se um arquivo foi enviado
    if uploaded_file is not None:
        # Carrega a imagem original
        imagem_original = Image.open(uploaded_file)

        # Salva a imagem original em um arquivo temporário
        caminho_da_imagem_original = "temp_imagem_original.png"
        imagem_original.save(caminho_da_imagem_original, format="PNG")
        st.image(imagem_original, caption="Imagem Original", use_column_width=True)

        imagem_alterada = escurecer_imagem(caminho_da_imagem_original, 70, "dont show")
        caminho_da_imagem_alterada = "temp_imagem_alterada.png"
        imagem_alterada.save(caminho_da_imagem_alterada, format="PNG")
        st.image(imagem_alterada, caption="Imagem Alterada", use_column_width=True)
        # TODO: Criar um botão para download, tirando o download automático

        