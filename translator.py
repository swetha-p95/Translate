import streamlit as st
from googletrans import Translator

st.header("Machine  Translation Demo")
input = st.text_area("Please enter the text", value ="")
option = st.selectbox(
    'To which language do you wish to translate this text?',
    ("Malayalam","Hindi","Tamil")
    )
if st.button("Translate"):
    translator = Translator()
    translation = translator.translate(input, dest=option)
    st.write(translation.text)