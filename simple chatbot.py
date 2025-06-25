import re

print(" Chatbot: Hello! I’m your AI assistant. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if re.search(r"\b(bye|exit|quit)\b", user_input):
        print(" Chatbot: Goodbye! Have a great day!")
        break

    # Greet the user
    elif re.search(r"\b(hi|hello|hey)\b", user_input):
        print(" Chatbot: Hi there! How can I assist you?")

    # Ask about the bot
    elif re.search(r"(your name|who are you)", user_input):
        print(" Chatbot: I'm a simple rule-based chatbot built using pattern matching.")

    # Ask about AI
    elif re.search(r"\b(what is|define)\b.*\b(ai|artificial intelligence)\b", user_input):
        print(" Chatbot: AI stands for Artificial Intelligence — machines that simulate human intelligence.")

    # Ask about wellbeing
    elif re.search(r"how.*(you|doing)", user_input):
        print(" Chatbot: I'm doing well, thank you! How about you?")

    # Fallback/default
    else:
        print(" Chatbot: I'm not sure how to respond to that. Can you ask me something else?")
