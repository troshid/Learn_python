import random

responses = {
    'hello': ['Hi there!', 'Hello!', 'Hey!'],
    'how are you': ['I am doing well, thank you!', 'Fantastic! How about you?', 'I am great, thanks for asking!'],
    'bye': ['Goodbye!', 'See you later!', 'Take care!']
}

def chatbot_response(message):
    for key in responses:
        if key in message.lower():
            return random.choice(responses[key])
    return "I'm sorry, I don't understand that."

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")
