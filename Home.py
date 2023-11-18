import streamlit as st

st.set_page_config(page_title="Introdução")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Página Principal")
