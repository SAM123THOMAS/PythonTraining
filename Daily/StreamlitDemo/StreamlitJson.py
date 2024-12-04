
import  requests
import streamlit as st

st.title("Weather Demo")


lat=st.text_input("Lattitude:")
long=st.text_input("Longitude:")
lat=float(lat)
long=float(long)

#12.9719
#77.5937


url ="https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":lat,
    "longitude":long,
    "current_weather":"true"
}


response=requests.get(url,params)
print(response)
st.write(response.json()['current_weather']["temperature"])