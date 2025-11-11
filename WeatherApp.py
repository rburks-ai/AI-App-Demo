import streamlit as st
import requests

st.title("Weather App 🌤️")

city = st.text_input("Enter a city name:")
if st.button("Get Weather"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.write(f"**Temperature:** {data['main']['temp']} °C")
        st.write(f"**Weather:** {data['weather'][0]['description'].title()}")
    else:
        st.error("City not found or API error.")
