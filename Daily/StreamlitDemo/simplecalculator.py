import streamlit as st

st.title("Calculator Demo")
numa=0
numb=0
option = st.selectbox(
    "Select ur numerical operation?",
    ("Add", "Subtract", "Multiply","Divide"),
)

st.write("You selected:", option)




numa=st.text_input("Number A")
st.write("First Number ",numa)
numb=st.text_input("Number B")
st.write("Second Number ",numb)



if(option=="Add"):
    result=int(numa)+int(numb)
    st.text(result)

if(option=="Subtract"):
    result=int(numa)-int(numb)
    st.text(result)

if(option=="Multiply"):
    result=int(numa)*int(numb)
    st.text(result)

if(option=="Divide"):
    result=int(numa)/int(numb)
    st.text(result)

