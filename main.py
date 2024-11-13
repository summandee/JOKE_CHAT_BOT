import random

# List of jokes
jokes = [
    "Why couldn't the bicycle find its way home? It lost its bearings!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!"
]

def tell_joke():
    return random.choice(jokes)

# Main chat loop
while True:
    user_input = input("You: ").lower()
    
    if user_input == "tell me a joke":
        print("Joke Bot: " + tell_joke())
    elif user_input == "exit":
        print("Joke Bot: Goodbye! Have a great day!")
        break
    else:
        print("Joke Bot: I can tell you a joke if you ask me to! Type 'tell me a joke' or 'exit' to quit.")
