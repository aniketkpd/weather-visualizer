import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Weather Dashboard", layout="centered")

# App title
st.title("🌤️ Weather Data Visualization App")
st.markdown("This app fetches real-time weather data for selected cities using the OpenWeatherMap API and visualizes it.")

# Your API key
api_key = '8caf306f108285c65fab6c702965decd'

# Function to fetch data
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'City': data['name'],
            "Temperature (°C)": round(data['main']['temp'] - 273.15, 2),
            "Humidity (%)": data['main']['humidity'],
            "Wind Speed (m/s)": data['wind']['speed'],
            "Condition": data['weather'][0]['description'].capitalize()
        }
    else:
        return None

# City selection
default_cities = ['Bhubaneswar', 'Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore']
cities = st.multiselect("Select Cities", options=default_cities, default=default_cities)

# Fetch and process weather data
weather_data = []
for city in cities:
    data = fetch_weather_data(city, api_key)
    if data:
        weather_data.append(data)

# Convert to DataFrame
if weather_data:
    df = pd.DataFrame(weather_data)
    st.subheader("📋 Weather Data Table")
    st.dataframe(df, use_container_width=True)

    # Visualizations
    st.subheader("📊 Weather Visualizations")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌡️ Temperature (°C)")
        st.bar_chart(df.set_index('City')["Temperature (°C)"])
    with col2:
        st.markdown("### 💧 Humidity (%)")
        st.bar_chart(df.set_index('City')["Humidity (%)"])

    st.markdown("### 🌬️ Wind Speed (m/s)")
    st.bar_chart(df.set_index('City')["Wind Speed (m/s)"])

    st.markdown("### 🌈 Weather Conditions")
    st.table(df[['City', 'Condition']])
else:
    st.warning("No data available. Please check your API key or city names.")

