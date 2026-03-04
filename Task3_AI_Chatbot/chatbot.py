import nltk
import random
import string

# Download required NLTK data (first time only)
nltk.download('punkt')

from nltk.tokenize import word_tokenize

# Simple predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a chatbot, but I'm doing great!", "I'm fine! How about you?"],
    "what is your name": ["I am CodTech ChatBot.", "You can call me NLP Bot."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"]
}

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def get_response(user_input):
    user_input = preprocess(user_input)

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "Sorry, I don't understand that yet."

print("ChatBot is running! (type 'bye' to exit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    response = get_response(user_input)
    print("Bot:", response)