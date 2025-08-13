def gamingbot():
    print("👋Welcome to the gaming bot!")
    print("Ask me about, consoles, games, tips, or gaming news.")
    print("Type exit anytime to quit\n")
    while True:
        userinput = input("Enter an option: ").lower()
        if userinput == "exit":
            print("Exiting.......")
            break
        elif any(word in userinput for word in["hello", "hi", "good morning"]):
            print("Hey gamer, ready to get started?")
        elif "console" in userinput or "best console" in userinput:
            print("Xbox Series, either one is good. Nintendo Switch or Switch 2. Playstation 4 and 5 are good too. You can also make your own PC and customize it to your needs.")
        elif "games" in userinput:
            print("Some of the most popular games include GTA 5, Minecraft, Call of Duty, Fortnite, and Roblox.")
        elif "tips" in userinput or "tip" in userinput:
            print("Some tips for games is make sure you actually enjoy the game, otherwise there is no reason to be playing it. Practice will make you better at it, dont give up, and be persistent.")
        elif "gaming news" in userinput:
            print("My Nintendo News Rumour: Mario fan thinks they have discovered the 40th anniversary account")
            print("Unreal Engine 5.6.1 Hotfix Released")
            print("Fae Farm Will Lose Online Support On Steam Next Month")
        else:
            print(f"{userinput} is not an option, please either restart the chatbot to type a valid response.")
gamingbot()   