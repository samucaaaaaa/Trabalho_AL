import numpy as np
from PIL import Image
import streamlit as st
from funcoes import transformacao, centralize_widget

st.set_page_config(page_title="Trabalho de Álgebra Linear")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.container():
    st.title("Trasformações Lineares com imagens")
    st.write("Aqui estão algumas transformações que podemos fazer com as imagens")

with st.container():
    st.write("---")
    st.write("Selecione o filtro para alterar a imagem!")
    centralize_widget(st.image, "imagens/paisagem.jpg", caption="Imagem Original", width=377)

    imagem_teste = Image.open("imagens/paisagem.jpg")
    imagem_teste_array = np.array(imagem_teste)
    
    # Opções de transformação
    transformacao_teste = st.selectbox("Escolha a transformação para o teste:", ["Nenhum", "Teste", "Contorno imagem", "Cor negativa", "Escurecer Imagem", "Filtrar cor", "Filtro blur",
                                                               "Filtro cimento", "Filtro frio", "Filtro quente","Filtro sepia", "Imagem Preto e Branco",
                                                              "Inverter imagem",  "Repetir imagem", "Rotacionar 90°","Redimensionar imagem"])

    # Botão para aplicar a transformação selecionada
    transformacao(transformacao_teste, imagem_teste_array, "jpg")

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

        centralize_widget(st.image, imagem_original, caption="Imagem Original", width=377)

        escolha_transformacao = st.selectbox("Escolha a transformação:", ["Nenhum", "Teste", "Contorno imagem", "Cor negativa", "Escurecer Imagem", 
                                                                "Filtrar cor", "Filtro blur", "Filtro cimento", "Filtro frio", "Filtro quente",
                                                                "Filtro sepia", "Imagem Preto e Branco","Inverter imagem",  "Repetir imagem",
                                                                "Rotacionar 90°","Redimensionar imagem"])
        
        salvamento = st.checkbox("Salvar", value=False)
        
        transformacao(escolha_transformacao, imagem_array, salvar=salvamento, key_widgets="alter")
        
        if salvamento == True and escolha_transformacao == "Nenhum":
            st.write("A nova imagem será salva como 'imagem_resultado.png'")
        elif salvamento == True and escolha_transformacao != "Nenhum": 
            with open("imagem_resultado.png", "rb") as imagem_resultado:
                imagem_bytes = imagem_resultado.read()

            # Criando um botão de download para a imagem
            st.download_button("Confirmar o Download da nova imagem", imagem_bytes, "imagem_resultado.png", "image/png")

        