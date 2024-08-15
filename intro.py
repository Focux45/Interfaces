import streamlit as st
from PIL import Image
st.title("😎 MI PRIMERA APP 😎")
st.header("Aqui subire todo el contenido")
st.write("Hola mundo")
image = Image.open("mclaren.jpg")
st.image(image,caption = "mclaren")
