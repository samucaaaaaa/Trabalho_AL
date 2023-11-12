from PIL import Image
import streamlit as st
from funcoes import *
import cv2

def transformacao(transformacao, imagem_array, tipo_imagem="jpg", salvar=False):
    if transformacao == "Escurecer Imagem":
        porcent_escurecimento = st.slider("Escolha a porcentagem de escurecimento:", 0, 100, 1)
        escurecer_imagem(imagem_array, porcent_escurecimento, salvar)

    if transformacao == "Imagem Preto e Branco":
        imagem_preto_branco(imagem_array, salvar)

    if transformacao == "Rotacionar 90°":
        rotaciona_90(imagem_array, salvar)

    if transformacao == "Filtro quente":
        filtro_quente(imagem_array, salvar)  

    if transformacao == "Inverter imagem":
        inverte_imagem(imagem_array, salvar)       

    if transformacao == "Filtro blur":
        imagem_array = cv2.imread("imagens/yuri.png")
        filtro_blur(imagem_array, salvar)    

    if transformacao == "Repetir imagem":
        n_repeticoes = st.slider("Escolha o número repetições:", 1, 10, 1)
        repete_imagem(imagem_array, n_repeticoes, salvar)
        
    if transformacao == "FIltro frio":
        filtro_frio(imagem_array, salvar)  

    if transformacao == "Redimensionar imagem":
        altura = st.slider("Escolha a altura:", 100, 800,imagem_array.shape[0], step=20)
        largura = st.slider("Escolha a largura", 100, 1000, imagem_array.shape[1], step=20)
        redimensionar_imagem(imagem_array, altura, largura, salvar)

    if transformacao == "Filtrar cor":
        cor = st.selectbox("Escolha a cor do filtro:", ["agua", "amarelo", "azul", "roxo", "verde", "vermelho"])
        filtro_cor(imagem_array, cor, tipo_imagem, salvar)   

    if transformacao == "FIltro sepia":
        filtro_sepia(imagem_array, tipo_imagem, salvar)
                        
    if transformacao == "Cor negativa":
        cor_negativa(imagem_array, salvar)

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
    st.write("Selecione o filtro para alterar a imagem!")
    st.image("imagens/yuri.png", caption="Imagem Original") 

    imagem_yuri = Image.open("imagens/yuri.png")
    imagem_yuri_array = np.array(imagem_yuri)
    
    # Opções de transformação
    transformacao_teste = st.selectbox("Escolha a transformação para o teste:", ["Nenhum", "Cor negativa", "Escurecer Imagem", "Filtrar cor", "Filtro blur",
                                                               "FIltro frio", "Filtro quente","FIltro sepia", "Imagem Preto e Branco",
                                                              "Inverter imagem",  "Repetir imagem", "Rotacionar 90°","Redimensionar imagem"])

    # Botão para aplicar a transformação selecionada
    transformacao(transformacao_teste, imagem_yuri_array, "png")

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

        st.image(imagem_original, caption="Imagem Original", width=377)

        escolha_transformacao = st.selectbox("Escolha a transformação:", ["Nenhum", "Cor negativa", "Escurecer Imagem", "Filtrar cor", "Filtro blur",
                                                               "FIltro frio", "Filtro quente","FIltro sepia", "Imagem Preto e Branco",
                                                              "Inverter imagem",  "Repetir imagem", "Rotacionar 90°","Redimensionar imagem"])
        
        salvamento = st.checkbox("Salvar", value=False)
        
        transformacao(escolha_transformacao, imagem_array)#, salvar=salvamento)
        
        if salvamento == True and escolha_transformacao == "Nenhum":
            st.write("A nova imagem será salva como 'imagem_resultado.png'")
        elif salvamento == True and escolha_transformacao != "Nenhum": 
            with open("imagem_resultado.png", "rb") as imagem_resultado:
                imagem_bytes = imagem_resultado.read()

            # Criando um botão de download para a imagem
            st.download_button("Confirmar o Download da nova imagem", imagem_bytes, "imagem_resultado.png", "image/png")

        