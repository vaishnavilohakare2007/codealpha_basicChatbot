# Basic Chatbot

print("🤖 Welcome to Basic Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")
    
    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")
    
    elif user_input == "what is your name":
        print("Bot: My name is ChatBot.")
    
    elif user_input == "help":
        print("Bot: You can ask me simple questions.")
    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    
    else:
        print("Bot: Sorry, I don't understand that.")
