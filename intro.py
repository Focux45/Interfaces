import streamlit as st
from PIL import Image
st.title("😎 MI PRIMERA APP 😎")
st.header("Aqui subire todo el contenido")
st.write("Hola mundo")
image = Image.open("mclaren.jpg")
st.image(image,caption = "mclaren")
texto = st.text_input('escribe algo',"Tienes 20 años y no has conseguido un carro deportivo, pues que lastima yo tampoco")
st.write("El texto escrito es", texto)
