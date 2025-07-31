from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    [
        r"welcome to house price predictor(.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you?", "Hi there!", "Hey!"]
    ],
    [
        r"what's your name\??",
        ["I am your web chatbot assistant!"]
    ],
    [
        r"how are you\??",
        ["I'm a program, but thanks for asking!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ]
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form["msg"]
    response = chatbot.respond(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
