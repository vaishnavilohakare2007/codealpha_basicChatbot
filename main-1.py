from flask import Flask, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"
    elif "how are you" in message:
        return "I'm doing well, thank you!"
    elif "name" in message:
        return "I'm a simple Python chatbot."
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user_message = data["message"]
    bot_reply = chatbot_response(user_message)

    return jsonify({
        "message": user_message,
        "reply": bot_reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)