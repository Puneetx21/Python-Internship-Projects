import json
import random
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Auto-download NLTK data if missing
for resource in ['punkt', 'wordnet', 'punkt_tab']:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)
lemmatizer = WordNetLemmatizer()

def load_intents(path='intents.json'):
    with open(path, 'r') as f:
        return json.load(f)

def preprocess(text):
    """Tokenize and lemmatize input text."""
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join([lemmatizer.lemmatize(token) for token in tokens])

def build_corpus(intents_data):
    """Build pattern corpus and tag mapping."""
    corpus = []
    tags = []
    responses = {}

    for intent in intents_data['intents']:
        tag = intent['tag']
        responses[tag] = intent['responses']

        for pattern in intent['patterns']:
            corpus.append(preprocess(pattern))
            tags.append(tag)

    return corpus, tags, responses


def get_response(user_input, corpus, tags, responses, vectorizer, tfidf_matrix, threshold=0.2):
    """Match user input to an intent and return a response."""
    processed_input = preprocess(user_input)
    input_vector = vectorizer.transform([processed_input])
    similarities = cosine_similarity(input_vector, tfidf_matrix).flatten()

    best_match_idx = np.argmax(similarities)
    best_score = similarities[best_match_idx]

    if best_score < threshold:
        # Use fallback intent
        return random.choice(responses.get('fallback', ["I don't understand. Please try again."]))

    matched_tag = tags[best_match_idx]
    return random.choice(responses[matched_tag])


def build_chatbot():
    """Initialize and return all chatbot components."""
    intents_data = load_intents()
    corpus, tags, responses = build_corpus(intents_data)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    return corpus, tags, responses, vectorizer, tfidf_matrix


# ── Standalone terminal chat (test without Flask) ──
if __name__ == '__main__':
    corpus, tags, responses, vectorizer, tfidf_matrix = build_chatbot()
    print("🤖 NLP Chatbot ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye! 👋")
            break

        response = get_response(user_input, corpus, tags, responses, vectorizer, tfidf_matrix)
        print(f"Bot: {response}\n")
