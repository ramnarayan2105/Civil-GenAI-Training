import streamlit as st
st.title("My first streamlit app")
st.write("Hello Ramnarayan")
st.text("Lets start")

name= st.text_input("Enter name:")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

