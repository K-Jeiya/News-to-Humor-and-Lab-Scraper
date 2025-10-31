from flask import Flask, jsonify, request
import requests, os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()
app = Flask(__name__)

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

@app.route('/humor-news')
def humor_news():
    params = request.args.to_dict()

    articles = fetch_news()

    humorous_articles = []
    for article in articles:
        humorous_articles.append({
            "title": article.get("title", "No title"),
            "original_description": article.get("description"),
            "humorous_description": funny_news(article.get("description"))
        })
    
    #save the data to a json file
    with open('news.json', 'w', encoding="utf_8") as f:
        json.dump(humorous_articles, f, ensure_ascii=False, indent=4)
    

    return jsonify({
        "status": "success",
        "data": humorous_articles
    })
 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
