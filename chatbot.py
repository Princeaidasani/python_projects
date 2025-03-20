def chatbot():
    print("Hello! I'm ChatBot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("ChatBot: Goodbye! Have a great day!")
            break
        
        if "hello" in user_input:
            print("ChatBot: Hello! How can I help you?")
        elif "weather" in user_input:
            print("ChatBot: I'm not a weather expert, but you can check an online weather service!")
        elif "name" in user_input:
            print("ChatBot: I'm ChatBot, your friendly assistant!")
        elif "help" in user_input:
            print("ChatBot: Sure! I can assist with basic questions. What do you need?")
        else:
            print("ChatBot: I'm sorry, I didn't understand that. Can you rephrase?")

if _name_ == "_main_":
    chatbot()