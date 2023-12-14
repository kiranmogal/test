# import random

# # Function to greet the user
# def greet():
#     responses = ["Hello!", "Hi there!", "Greetings!", "Nice to meet you!"]
#     return random.choice(responses)

# # Function to handle user's input
# def handle_input(user_input):
#     user_input = user_input.lower()
    
#     if user_input.startswith("hi") or user_input.startswith("hello"):
#         return greet() 
#     elif "how are you" in user_input:
#         return "I'm good, thank you! How about you?"
#     elif "your name" in user_input:
#         return "I'm a chatbot. You can call me ChatBot!"
#     elif "bye" in user_input:
#         return "Goodbye! Have a great day!"
#     else:
#         return "I'm sorry, I didn't understand. Could you please rephrase?"

# # Main function for the chatbot interaction
# def chat():
#     print("ChatBot: " + greet())
    
#     while True:
#         user_input = input("User: ")
#         response = handle_input(user_input)
#         print("ChatBot: " + response)
        
#         if "bye" in user_input:
#             break

# # Run the chatbot
# chat()

import random
def greet():
    responses = ["hi", "hello", "hey there"]
    return random.choice(responses)

def handle_input(user_input) :
    user_input = user_input.lower()
    if user_input.startswith("hi") :
        return greet()
    elif "how r u" in user_input :
        return "im gud , how r u?"
    elif "whatday is today?" in user_input:
        return "its saturday"
    else :
        return "i did not understand that. can you please re-enter?"
    

def chat() :
    print("Chatbot : " + greet())

    while True :
        user_input = input("User :")
        response = handle_input(user_input)
        print("chatbot :" + response())
        
        if "bye" or "stop" in user_input :
            break

chat()

