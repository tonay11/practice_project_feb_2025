# 🚀 Fun API Labs: Learn APIs Like a Pro!

## **Lab 1: Fetching and Visualizing Weather Data 🌦️**

### **🎯 Objective:**
- Retrieve live weather data using the **OpenWeather API**.
- Process and clean JSON responses.
- Store data in a **pandas DataFrame**.
- Export results as a **CSV file**.
- Plot the temperature trends using **matplotlib**.

---

## **📝 Step 1: Sign Up for OpenWeather API**
1. Go to [OpenWeather](https://home.openweathermap.org/users/sign_up) and **sign up**.
2. Navigate to **API Keys** in your dashboard.
3. Copy your **API Key** (you’ll need this later).

🔎 _Hint: Keep your API key secret! Never share it in public repositories._

---

## **🔧 Step 2: Install Required Libraries**

Before diving in, let's make sure we have the necessary tools installed:
```python
!pip install requests pandas matplotlib
```

Then, import them:
```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
```

---

## **🌍 Step 3: Make Your First API Request**
Time to fetch some weather data! Here’s how:
```python
API_KEY = "your_openweather_api_key"
CITY_NAME = "Tokyo"

# Construct request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"

# Make API request
response = requests.get(url)
data = response.json()

# Print the response
print(data)
```

### **🧐 What Just Happened?**
- We used the `requests` library to **fetch weather data** for a city.
- The response is in **JSON format**.
- If your response contains `{ 'cod': 401 }`, check if your API key is correct!

---

## **🎯 Step 4: Extract Useful Information**
Weather data is cool, but let’s **make it readable**:
```python
if "main" in data:
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    
    print(f"City: {city}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWeather: {weather}")
else:
    print("Error fetching weather data.")
```

---

## **📊 Step 5: Store Data in a DataFrame**
Let’s create a **structured table** of weather data:
```python
data_dict = {
    "City": [city],
    "Temperature (°C)": [temp],
    "Humidity (%)": [humidity],
    "Weather Description": [weather]
}

weather_df = pd.DataFrame(data_dict)
print(weather_df)
```

---

## **📂 Step 6: Export Data to CSV**
Want to save your data for future analysis? Easy!
```python
weather_df.to_csv("weather_data.csv", index=False)
print("Data saved to weather_data.csv")
```

---

## **📈 Step 7: Visualizing Weather Trends**
Graphs make everything cooler! Let’s plot temperatures:
```python
plt.figure(figsize=(6,4))
plt.bar(weather_df["City"], weather_df["Temperature (°C)"], color='skyblue')
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperature")
plt.show()
```

👀 **What You Just Did:**
- Created a **bar chart** showing the temperature in a city.

---

## **🎯 Challenge: Compare Multiple Cities**
Let’s take it a step further by comparing weather in multiple cities:
```python
cities = ["London", "New York", "Paris", "Tokyo", "Sydney"]
weather_data = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if "main" in data:
        weather_data.append({
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather Description": data["weather"][0]["description"]
        })

# Convert to DataFrame
multi_city_df = pd.DataFrame(weather_data)
print(multi_city_df)
```

📊 **BONUS:** Plot all cities on a graph!
```python
plt.figure(figsize=(8,5))
plt.bar(multi_city_df["City"], multi_city_df["Temperature (°C)"], color='coral')
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Weather Comparison Across Cities")
plt.show()
```

---

## **🎉 Extra Challenges**
- 🌎 **Enhance the script**: Allow the user to **input** cities.
- 📌 **Handle API errors** (e.g., invalid city name).
- 🚀 **Use Matplotlib to plot humidity vs. temperature**.
- 🔥 **Build a simple weather chatbot** using this data!

🚀 **Congrats! You’ve just mastered API requests!** 🎉

