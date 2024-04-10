import random
def greet():
    responses = ["Hello🌟", "Hello there", "Namaste😊", "Greeting", "Hola", "Hey!", "Hey there! Welcome to the conversation!",
                 "Hello! Nice to meet you🌟. How can I assist you today?", "Greetings! How may I be of service to you?",
                 "Hi🌞! I'm here and ready to help. What can I do for you?", "Hey! Ready to chat? I'm all ears!",
                 "Hello, friend! What's on your mind?", "Good day❤️! How can I make your day better?",
                 "Hi there! I hope you're having a great day. How can I assist you?", "Hello! I'm here to assist you with anything you need.",
                 "Hey! Glad you're here. Let's get started, shall we?", "Greetings! I'm at your service😊. How can I assist you today?",
                 "Hello, dear❤️! What brings you here today?", "Hi! I'm here to chat and help you out. What's on your mind?",
                 "Hey there! Ready to dive into our conversation😊?", "Hello! Let's make today productive together. What do you say?",
                 "Hi! How's your day going? Let's chat!", "Greetings, traveler! Welcome to our little corner of the digital world.",
                 "Hello! It's great to see you. How can I assist you today?", "Hey! I'm here and ready to assist. What can I do for you?",
                 "Hi there! Let's embark on this conversation journey together, shall we?"]
    return random.choice(responses)

def love_responses():
    responses = ["I'm sorry, but I'm just a chatbot🤖. I don't experience emotions like love or affection.",
                 "I appreciate the sentiment, but I'm a chatbot🤖 programmed to assist with tasks, not to feel emotions like love.",
                 "I'm flattered❤️, but as a chatbot, I don't have the capability to feel love or affection.",
                 "I'm here to help with any questions or tasks you have, but I'm not capable of feeling love or affection like a human does."]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye! It was a pleasure chatting with you.", "Farewell! Until we chat again, take care!",
                 "Bye for now! Wishing you a wonderful day ahead.", "Take care! Don't hesitate to return if you need assistance.",
                 "Goodbye! May your day be filled with joy and success.", "Adios! Remember, I'm just a message away if you need me.",
                 "So long! It was great helping you out. Have a fantastic day!", "See you later! Feel free to come back anytime.",
                 "Bye-bye! Stay safe and be well.", "Au revoir! Until next time, take care of yourself.",
                 "Catch you later! Remember, I'm here whenever you need assistance."]
    return random.choice(responses)

def chatbot_response(input):
    if input.lower() in ["hello", "hi", "namaste", "hola", "hey", "salawalekum", "adab"]:
        return greet()
    elif any(word in input.lower() for word in ["help", "search", "tell me about", "show me", "calculate", "translate", "remind me to"]):
        return random.choice(["Sure thing, I've got it covered.", "No worries, I'll take care of it.", "Okay, just sit back and relax.",
                              "Leave it to me, I'm here to assist you.", "Understood, I'll handle that for you.", "Don't worry, I've got your back.",
                              "Consider it done!", "Relax, I'm on the case.", "Got it, I'll get right on it.", "You can count on me to help you out.",
                              "Absolutely, I'm here to help.", "No problem, I'll sort it out for you.", "Alright, let's tackle this together.",
                              "Gotcha, I'll take the lead on this one.", "I understand, leave it to me to find a solution.", "Consider it done, I'm at your service.",
                              "Sure thing, I'll get right on it.", "Okay, I'll handle it with care.", "Roger that, I'll handle the task.",
                              "Absolutely, you can rely on me for assistance."])
    elif any(word in input.lower() for word in ["bye", "goodbye", "see you later", "catch you later", "thanks, bye", "thank you, goodbye", "take care, bye", "have a great day, goodbye"]):
        return farewell() + "\nIf you want to end the conversation, type 'exit'."
    
    elif any(word in input.lower() for word in ["love you", "marry me", "I love you", "I'm in love with you", "I have feelings for you"]):
        return love_responses()
    else:
        return random.choice(["I apologize, but I'm only trained with limited data at the moment. My team is still working on improving my capabilities. Please bear with us.",
                              "Sorry about that. My training data is limited, and my team is still working on enhancing my abilities. Thank you for your patience.",
                              "I'm sorry, but my training data is limited, and my development team is continually working to improve my skills. Your patience is appreciated.",
                              "Apologies, my training data is somewhat limited at the moment. My team is hard at work expanding my knowledge. Thank you for your understanding.",
                              "I regret to inform you that I'm only trained with a limited dataset for now. Rest assured, my team is diligently working on enhancing my capabilities. Thank you for your patience.",
                              "Sorry for any inconvenience. My training data is currently limited, but my team is working hard to improve my abilities. Thank you for your understanding and patience.",
                              "I apologize for any inconvenience caused. At the moment, my training data is limited, but my development team is actively working to enhance my capabilities. Your patience is greatly appreciated."])

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print(farewell())
        break
    else:
        print("Riya: ", chatbot_response(user_input))
