import streamlit as st

st.title("User Input Demo")
#st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.text("Enter the username")
username=st.text_input("Username")
st.write("Input username is ",username)
password=st.text_input("Password")
st.write("Input Password is ",password)

