import streamlit as st
import requests

st.set_page_config(page_title="Weather App 🌦️", page_icon="🌤️", layout="centered")

st.title("🌤️ Simple Weather App (Public API)")

# User input
city = st.text_input("Enter a city name:")

if st.button("Get Weather"):
    try:
        # Step 1: Get city coordinates from Open-Meteo geocoding API
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url).json()

        if "results" not in geo_response:
            st.error("City not found. Try again.")
        else:
            lat = geo_response["results"][0]["latitude"]
            lon = geo_response["results"][0]["longitude"]
            location_name = geo_response["results"][0]["name"]

            # Step 2: Get weather data using coordinates
            weather_url = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={lat}&longitude={lon}&current_weather=true"
            )
            weather_response = requests.get(weather_url).json()
            weather = weather_response["current_weather"]

            # Step 3: Display results
            st.subheader(f"🌍 Weather in {location_name}")
            st.metric("Temperature", f"{weather['temperature']} °C")
            st.metric("Wind Speed", f"{weather['windspeed']} km/h")
            st.metric("Condition Code", weather["weathercode"])
    except Exception as e:
        st.error(f"Something went wrong: {e}")

st.markdown("---")
st.caption("Powered by [Open-Meteo API](https://open-meteo.com/)")
