# To fetching data from api
import requests

# To store data fetched from api
import pandas as pd

# To visualize the stored data
import matplotlib.pyplot as plt



# The base url of openweathermap website is
# http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}

# Registered then Taken from website
api_key = '8caf306f108285c65fab6c702965decd'

# Function to fetch data from website using api
def fetch_weather_data(city,api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(url)
    
    # if the request succeed
    if response.status_code == 200:
        # Take response from the api and store it in json format
        data  =  response.json()

        # Processing - extracting the required information from the api
        return {
            'City' : data['name'],
            "Temperature (°C)": round(data['main']['temp'] - 273.15, 2),
            "Humidity (%)": data['main']['humidity'],
            "Wind Speed (m/s)": data['wind']['speed'],
            "Condition": data['weather'][0]['description']
        }
        
    # if any error occurs in response   
    else:
        print("Error in fetching data")   
        return None


    
# List of cities
cities = ['Bhubaneswar', 'Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore']



# Fetch weather data for all cities


weather_data = []

for city in cities:
    city_weather = fetch_weather_data(city, api_key)
    if city_weather is not None:  # Only add if data is valid
        weather_data.append(city_weather)
        
# Here weather_data will contain a list of dictionaries



df = pd.DataFrame(weather_data)

print(df)
    
# Collected data from different cities now we have to visualize it

# ===== Visualization ====
'''
As we want to show compare each cities with thier weather info, we would with each factor like temperature , humidity and wind speed one by one, and because we are comparing 2 values everytime we would use the bar plot of matplotlib for visualizing the information fetched from api.
'''

# Selecting colors for different cities for better view
colors = ['red', 'blue', 'green', 'orange', 'yellow']

# Temperature

plt.bar(df['City'], df['Temperature (°C)'], color=colors)
plt.title("City-wise Temperature Comparison (°C)")
plt.xlabel('Cities')
plt.ylabel('Temperature')
plt.show()

# Humidity

plt.bar(df['City'], df['Humidity (%)'], color=colors)
plt.title("City-wise Humidity Comparison (%) ")
plt.xlabel('Cities')
plt.ylabel('Humidity')
plt.show()

# Wind Speed (m/s)

plt.bar(df['City'], df['Wind Speed (m/s)'], color=colors)
plt.title("City-wise Wind Speed Comparison (m/s)")
plt.xlabel('Cities')
plt.ylabel('Wind Speed (m/s)')
plt.show()