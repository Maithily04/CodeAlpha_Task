def chatbot_response(user_input):
    user_input = user_input.lower()  # Handle case-insensitive input
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."

# Main loop to keep the chatbot running
def run_chatbot():
    print("Chatbot: Hello! Type something...")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
            break

# Run the chatbot
run_chatbot()
