import requests, os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
ai_api_key = os.getenv("GROQAI_API_KEY")

client = Groq(api_key=ai_api_key)

# Fetch news from api
def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    # print(data)
    return data.get("articles", [])

# convert news description into humor
def funny_news(description):
    if description is None:
            description = "Description is None"
    prompt = f"Convert news into funny and add emojis:{description}"
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content


articles = fetch_news()
for article in articles:
    title = article.get("title", "No title")
    description = article.get("description")
    humorous = funny_news(description)
    # print(title,description)

    print(f"Title: {title}")
    print(f"Original_description: {description}")
    print(f"Humorous_description: {humorous}")
