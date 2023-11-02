import streamlit as st
from funcoes import escurecer_imagem

st.set_page_config(page_title="Trabalho de Álgebra Linear")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Trasformações Lineares com imagens")
    st.write("Aqui estão algumas transformações que podemos fazer com as imagens")
    st.write("Quer acessar o projeto pelo GitHub? [Clique aqui](https://github.com/samucaaaaaa/Trabalho_AL)")

with st.container():
    st.write("---")

if st.button("Clique para ir no projeto do GitHub :)"):
    site_url = "https://github.com/samucaaaaaa/Trabalho_AL"
    st.write(f'<meta http-equiv="refresh" content="0; url={site_url}" />', unsafe_allow_html=True)

if st.button("Alterar Imagem"):
    escurecer_imagem("yuri.png", 70)

st.image('yuri.png') 
