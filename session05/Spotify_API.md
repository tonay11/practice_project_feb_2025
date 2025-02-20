# 🎵 Fun API Labs: Exploring Spotify Data with Spotipy 🎧

## **Lab 2: Analyzing Music Trends with Spotipy**

### **🎯 Objective:**
- Connect to the **Spotify API** using Spotipy.
- Fetch data on **popular songs and artists**.
- Load and analyze **music data** using `pandas`.
- Visualize trends in **song popularity** using `matplotlib`.

---

## **📝 Step 1: Set Up Your Spotify API Credentials**
1. **Sign up** at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create a new app.
2. Copy your **Client ID** and **Client Secret**.
3. Add a **Redirect URI** (e.g., `http://localhost:9090`) in your Spotify app settings.

🔎 _Hint: Never share your API keys in public repositories!_

---

## **🔧 Step 2: Install Spotipy**

Before we begin, ensure you have `spotipy` installed:
```python
!pip install spotipy pandas matplotlib
```

Then, import the necessary libraries:
```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
```

---

## **🎼 Step 3: Authenticate and Connect to Spotify API**
```python
SPOTIPY_CLIENT_ID = "your_spotify_client_id"
SPOTIPY_CLIENT_SECRET = "your_spotify_client_secret"

# Set up authentication
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                      client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
```

✅ **What This Does:**
- Logs into Spotify’s API using your credentials.
- Enables API requests to fetch song data.

---

## **🎤 Step 4: Fetch Top 1000 Songs from 2023**

Let’s pull data on **popular songs** from the year 2023:
```python
artist_name = []
track_name = []
popularity = []
track_id = []
images = []

for i in range(0, 1000, 50):
    track_results = sp.search(q='year:2023', type='track', limit=50, offset=i)
    for t in track_results['tracks']['items']:
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        images.append(t['album']['images'][0]['url'])
```

✅ **What This Does:**
- Loops through **1000 songs from 2023**.
- Stores key details like **artist name, song title, popularity, and album image**.

---

## **📊 Step 5: Load Data into a DataFrame**

Now, let’s organize our data into a structured **pandas DataFrame**:
```python
track_dataframe = pd.DataFrame({
    'Artist': artist_name,
    'Track': track_name,
    'Track ID': track_id,
    'Popularity': popularity,
    'Image URL': images
})

# Sort by popularity (descending)
df_sorted = track_dataframe.sort_values(by='Popularity', ascending=False).reset_index(drop=True)

# Display the first 10 most popular tracks
df_sorted.head(10)
```

✅ **What This Does:**
- Converts raw data into a structured table.
- Sorts **tracks by popularity**.

---

## **🎵 Step 6: Who Were the Most Successful Artists in 2023?**

Which artists dominated the charts with multiple hits? Let’s find out!
```python
artist_counts = track_dataframe['Artist'].value_counts()
most_successful_artists = artist_counts.head(10)

# Plot the results
plt.figure(figsize=(12,6))
plt.bar(most_successful_artists.index, most_successful_artists.values, color='purple')
plt.xlabel("Artist")
plt.ylabel("Number of Songs in Top 1000")
plt.title("Top Artists with Most Songs in Spotify's 2023 Top 1000")
plt.xticks(rotation=45)
plt.show()
```

👀 **What You Just Did:**
- Counted the **number of hit songs per artist**.
- Created a **bar chart** to visualize the top 10 most successful artists.

---

## **🎚️ Step 7: Analyzing the Most Popular Song’s Features**

Spotify provides **detailed audio features** for every song. Let’s analyze the **most popular song of 2023**:
```python
most_popular_track = df_sorted.iloc[0]
most_popular_track_id = most_popular_track['Track ID']

# Get audio features
track_audio_features = sp.audio_features(most_popular_track_id)[0]

# Print key details
print(f"Danceability: {track_audio_features['danceability']}")
print(f"Energy: {track_audio_features['energy']}")
print(f"Speechiness: {track_audio_features['speechiness']}")
print(f"Valence (Mood): {track_audio_features['valence']}")
```

✅ **What This Does:**
- Retrieves **danceability, energy, and mood** data.
- Shows how Spotify analyzes songs **beyond popularity**.

---

## **🎧 Step 8: Visualizing Danceability vs. Popularity**

Let’s compare **song danceability vs. popularity**:
```python
plt.figure(figsize=(8,5))
plt.scatter(track_dataframe['Popularity'], track_dataframe['Track'].map(lambda x: sp.audio_features(sp.search(q=x, type='track')['tracks']['items'][0]['id'])[0]['danceability']), c='blue', alpha=0.5)
plt.xlabel("Popularity")
plt.ylabel("Danceability")
plt.title("Danceability vs. Popularity of Spotify Songs (2023)")
plt.show()
```

👀 **What You Just Did:**
- Created a **scatter plot** comparing danceability and popularity.
- Found out if **popular songs are also highly danceable**.

---

## **🎯 Challenge: Explore More Spotify Data!**
🚀 Try these extra challenges:
- Find the **happiest** or **most energetic** song from 2023.
- Compare **tempo vs. popularity**.
- Analyze the **most successful music genres** using `sp.recommendation_genre_seeds()`.
- Build a **playlist generator** based on user mood! 🎶

🎉 **Congrats! You’ve just analyzed music trends using the Spotify API!** 🎧🔥

