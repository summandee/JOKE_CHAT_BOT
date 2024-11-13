PROMPT :str = "what do you want?"
JOKE :str = "What is the most popular fish in the ocean? The starfish."
def joke_bot():
    user_input = input(PROMPT)
    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print("sorry, i tell only joke")
joke_bot()
