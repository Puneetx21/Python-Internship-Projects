from flask import Flask, render_template, request, jsonify
from chatbot import build_chatbot, get_response

app = Flask(__name__)

# Build chatbot once when server starts
corpus, tags, responses, vectorizer, tfidf_matrix = build_chatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    if not user_message:
        return jsonify({'response': 'Please type something!'})
    bot_response = get_response(
        user_message, corpus, tags, responses, vectorizer, tfidf_matrix
    )
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
