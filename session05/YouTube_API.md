# 🎥 Fun API Labs: Exploring YouTube Data with YouTube API 🎬

## **Lab 3: Analyzing YouTube Videos & Comments**

### **🎯 Objective:**
- Connect to the **YouTube Data API v3**.
- Fetch data on **popular videos and their comments**.
- Analyze trends in **video popularity and engagement**.
- Perform **sentiment analysis** on YouTube comments.

---

## **📝 Step 1: Set Up Your YouTube API Credentials**
1. **Sign up** at [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **YouTube Data API v3**.
3. Create **API credentials** under **APIs & Services**.
4. Copy your **API Key**.

🔎 _Hint: Never share your API keys in public repositories!_

---

## **🔧 Step 2: Install Required Libraries**

Before diving in, install the necessary tools:
```python
!pip install google-api-python-client pandas matplotlib textblob
```

Then, import them:
```python
from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
```

---

## **🎬 Step 3: Authenticate and Connect to YouTube API**
```python
YOUTUBE_API_KEY = "your_youtube_api_key"

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
```

✅ **What This Does:**
- Connects to YouTube API using your API key.
- Enables API requests to fetch video and comment data.

---

## **📺 Step 4: Fetch Top Trending Videos**

Let’s retrieve trending videos from **YouTube’s Trending Feed**:
```python
request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode="US",
    maxResults=10
)
response = request.execute()
```

✅ **What This Does:**
- Fetches **top trending videos** in the U.S.
- Retrieves video **title, view count, likes, and comment count**.

---

## **📊 Step 5: Store Data in a DataFrame**

Now, let’s organize the data into a structured **pandas DataFrame**:
```python
video_data = []

for item in response["items"]:
    video_data.append({
        "Title": item["snippet"]["title"],
        "Views": int(item["statistics"]["viewCount"]),
        "Likes": int(item["statistics"].get("likeCount", 0)),
        "Comments": int(item["statistics"].get("commentCount", 0))
    })

video_df = pd.DataFrame(video_data)
video_df.head()
```

✅ **What This Does:**
- Extracts **video title, views, likes, and comments**.
- Stores the data in a clean **DataFrame**.

---

## **📈 Step 6: Visualizing Video Popularity**

Let’s compare **views vs. likes**:
```python
plt.figure(figsize=(10,5))
plt.bar(video_df["Title"], video_df["Likes"], color='blue')
plt.xlabel("Video Title")
plt.ylabel("Likes")
plt.title("Likes on Trending Videos")
plt.xticks(rotation=45, ha='right')
plt.show()
```

👀 **What You Just Did:**
- Created a **bar chart** showing the **likes** on trending videos.

---

## **💬 Step 7: Fetching Video Comments**

Now, let’s extract **comments** from the most popular video:
```python
video_id = response["items"][0]["id"]  # Get first video's ID

comment_request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=20
)
comment_response = comment_request.execute()
```

✅ **What This Does:**
- Fetches **20 comments** from the top video.

---

## **🧐 Step 8: Performing Sentiment Analysis on Comments**

We can analyze the **tone of YouTube comments**:
```python
comments = []
sentiments = []

for item in comment_response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    sentiment = TextBlob(comment).sentiment.polarity  # Analyzes sentiment
    comments.append(comment)
    sentiments.append(sentiment)

comment_df = pd.DataFrame({"Comment": comments, "Sentiment": sentiments})
comment_df.head()
```

✅ **What This Does:**
- Uses `TextBlob` to analyze **positive vs. negative comments**.

---

## **🎭 Step 9: Visualizing Sentiment Analysis**

Let’s plot a **histogram of sentiment scores**:
```python
plt.hist(comment_df["Sentiment"], bins=20, color='green', alpha=0.7)
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.title("YouTube Comment Sentiment Analysis")
plt.show()
```

👀 **What You Just Did:**
- Created a **histogram** showing the distribution of comment sentiment.

---

## **🎯 Challenge: Explore More YouTube Data!**
🚀 Try these extra challenges:
- Find out **which category of videos gets the most views**.
- Compare **comments vs. likes**.
- Find **the most commonly used words in YouTube comments**.
- Build a **dashboard** displaying real-time YouTube stats!

🎉 **Congrats! You’ve just explored YouTube’s trending videos and comments!** 🎬🔥

