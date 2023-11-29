from flask import Flask, render_template, request, jsonify
import requests
from openai import OpenAI
client = OpenAI(api_key= "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")
import prompt as pr
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

# URL of your Flask server's endpoint (replace with your actual URL)
url = "http://20.163.29.17:80/predict"

# Function to fetch news articles from NewsAPI
def fetch_news_articles(topic):
    api_key = '0e2ef7c699bc4a18a5a3b58714579809'  # Replace with your actual NewsAPI key
    base_url = 'https://newsapi.org/v2/everything'
    params = {
        'q': topic,
        'apiKey': api_key,
        'language': 'en',
        'pageSize': 10,
        'sortBy': 'relevancy'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        print('Failed to fetch articles:', response.status_code)
        return []
    
# Function to scrape the content of the article
def scrape_article_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Unable to fetch the article content."
    
    soup = BeautifulSoup(response.content, 'html.parser')
    content = ' '.join([p.text for p in soup.find_all('p')])
    return content

# Route for handling the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the form submission and showing results
@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form.get('input_text')
    articles = fetch_news_articles(topic)
    return render_template('result.html', articles=articles)

# Route for handling the summary generation
@app.route('/get_summary', methods=['POST'])
def get_summary():
    data = request.json
    article_url = data['url']
    print(article_url)
    content = scrape_article_content(article_url)
    # Pass content to gpt and fetch summary
    summary = get_completion(content)
    return jsonify({'summary': summary})
# Route for handling the summary generation
# @app.route('/get_summary', methods=['POST'])
# def get_summary():
#     data = request.json
#     article_content = data['content']  # Retrieve the content from the request
#     # You can modify this part to generate the summary from the content
#     # Example: summary = generate_summary(article_content)
#     # For now, let's assume you have a function called generate_summary
#     summary = generate_summary(article_content)
#     return jsonify({'summary': summary})
def get_completion(news_content, model="gpt-3.5-turbo"):

    messages = [{"role": "system", "content": pr.sys_prompt},{"role": "user", "content": news_content}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    # print(response)
    print(response.choices[0].message.content)
    return response.choices[0].message.content


# Save response function
@app.route('/save_response', methods=['POST'])
def save_response():
    data = request.json
    article_content = data['article_content']
    article_summary = data['article_summary']
    user_response = data['user_response']
    file_path = 'responses.txt'
    
    try:
        with open(file_path, 'a') as file:
            file.write(f"Content: {article_content}\nSummary: {article_summary}\nUser Response: {user_response}\n\n")
    except IOError as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'Failed to save response'}), 500

    return jsonify({'message': 'Response saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)

