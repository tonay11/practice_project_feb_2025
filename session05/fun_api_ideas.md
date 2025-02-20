### **1️⃣ NASA API 🚀 (Space Data & Astronomy)**
- 📡 **What it does:** Get daily astronomy pictures, asteroid tracking, and Mars rover photos.
- 🔥 **Why it’s cool:** Space images, real-time satellite data, and the ability to track asteroids near Earth.
- 🔗 [NASA API Docs](https://api.nasa.gov/)
- **Example: Get the Astronomy Picture of the Day**
  ```python
  import requests

  API_KEY = "DEMO_KEY"
  url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
  response = requests.get(url).json()

  print("Title:", response["title"])
  print("Explanation:", response["explanation"])
  print("Image URL:", response["url"])
  ```

---

### **2️⃣ OpenAI DALL·E API 🎨 (AI-Generated Images)**
- 🎨 **What it does:** Generates images from text prompts using AI.
- 🔥 **Why it’s cool:** Students can turn **text into artwork** with AI.
- 🔗 [OpenAI API Docs](https://beta.openai.com/docs/)
- **Example: Generate an Image**
  ```python
  import openai

  openai.api_key = "your_api_key"

  response = openai.Image.create(
      prompt="A futuristic city in the clouds with neon lights",
      n=1,
      size="1024x1024"
  )

  print(response["data"][0]["url"])
  ```

---

### **3️⃣ Pokémon API 🎮 (Pokémon Data & Stats)**
- 🕹 **What it does:** Fetch Pokémon details like abilities, types, and evolutions.
- 🔥 **Why it’s cool:** Students can create a **Pokédex!**
- 🔗 [PokéAPI Docs](https://pokeapi.co/)
- **Example: Get Pokémon Data**
  ```python
  import requests

  pokemon = "pikachu"
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
  response = requests.get(url).json()

  print("Name:", response["name"])
  print("Type:", response["types"][0]["type"]["name"])
  print("Abilities:", [ability["ability"]["name"] for ability in response["abilities"]])
  ```

---

### **4️⃣ Google Maps API 🗺️ (Geolocation & Routes)**
- 🏙 **What it does:** Get locations, directions, and real-time traffic.
- 🔥 **Why it’s cool:** Can be used to **build a travel app or a city guide.**
- 🔗 [Google Maps API Docs](https://developers.google.com/maps)
- **Example: Get Geolocation Data**
  ```python
  import requests

  API_KEY = "your_google_maps_api_key"
  location = "London"
  url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}"
  response = requests.get(url).json()

  print("Formatted Address:", response["results"][0]["formatted_address"])
  print("Latitude:", response["results"][0]["geometry"]["location"]["lat"])
  print("Longitude:", response["results"][0]["geometry"]["location"]["lng"])
  ```

---

### **5️⃣ OpenWeather API ⛅ (Real-Time Weather Data)**
- 🌦 **What it does:** Get current weather, forecasts, and historical data.
- 🔥 **Why it’s cool:** Students can build a **weather app** with real-time data.
- 🔗 [OpenWeather API Docs](https://openweathermap.org/api)
- **Example: Get Current Weather**
  ```python
  import requests

  API_KEY = "your_api_key"
  city = "Tokyo"
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
  response = requests.get(url).json()

  print("City:", response["name"])
  print("Temperature:", response["main"]["temp"], "°C")
  print("Weather:", response["weather"][0]["description"])
  ```

---

### **6️⃣ Spotify API 🎵 (Music Data & Playlists)**
- 🎶 **What it does:** Get song data, create playlists, and analyze tracks.
- 🔥 **Why it’s cool:** Build a **music recommendation app** or an **AI DJ**.
- 🔗 [Spotify API Docs](https://developer.spotify.com/documentation/web-api/)
- **Example: Get Track Info**
  ```python
  import requests

  token = "your_spotify_access_token"
  track_id = "3n3Ppam7vgaVa1iaRUc9Lp"
  url = f"https://api.spotify.com/v1/tracks/{track_id}"
  headers = {"Authorization": f"Bearer {token}"}

  response = requests.get(url, headers=headers).json()

  print("Track Name:", response["name"])
  print("Artist:", response["artists"][0]["name"])
  print("Album:", response["album"]["name"])
  ```

---

### **7️⃣ Giphy API 😂 (GIF Search & Memes)**
- 📺 **What it does:** Search for trending GIFs or memes.
- 🔥 **Why it’s cool:** Students can create a **meme generator!**
- 🔗 [Giphy API Docs](https://developers.giphy.com/)
- **Example: Search for a GIF**
  ```python
  import requests

  API_KEY = "your_giphy_api_key"
  query = "funny cat"
  url = f"https://api.giphy.com/v1/gifs/search?q={query}&api_key={API_KEY}&limit=1"

  response = requests.get(url).json()

  print("GIF URL:", response["data"][0]["images"]["original"]["url"])
  ```

---

### **8️⃣ Twilio API 📞 (Send SMS & Calls)**
- 📱 **What it does:** Send SMS, make calls, and verify phone numbers.
- 🔥 **Why it’s cool:** Build an **automated messaging system**.
- 🔗 [Twilio API Docs](https://www.twilio.com/docs)
- **Example: Send an SMS**
  ```python
  from twilio.rest import Client

  account_sid = "your_account_sid"
  auth_token = "your_auth_token"
  client = Client(account_sid, auth_token)

  message = client.messages.create(
      body="Hello from Twilio!",
      from_="+1234567890",
      to="+0987654321"
  )

  print("Message sent with ID:", message.sid)
  ```

