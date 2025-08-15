from colorama import init, Fore, Style
def gamingbot():
    print("👋Welcome to the gaming bot!")
    while True:
        print("Ask me about, consoles, games, tips, gaming news, the current latest version of a specific video game, or the most anticipated game of last year.")
        print("Type exit anytime to quit\n")
        userinput = input("Enter an option: ").lower()
        if userinput == "exit":
            print(Fore.GREEN+"Exiting......."+Style.RESET_ALL)
            break
        #NLP could be used in any of these elif statements that check which part of the gaming AI is being asked for
        elif any(word in userinput for word in["hello", "hi", "good morning"]):
            print("Hey gamer, ready to get started?")
        #NLP could be used in this one    
        elif any(word in userinput for word in["most popular console", "best console", "console"]):
            print("Xbox Series, either one is good. Nintendo Switch or Switch 2. Playstation 4 and 5 are good too. You can also make your own PC and customize it to your needs.")
        #NLP could also be used in this one    
        elif any(word in userinput for word in["popular video games", "video games", "games"]):
            print("Some of the most popular games include GTA 5, Minecraft, Call of Duty, Fortnite, and Roblox.")
        #NLP could also be used in this one  
        elif any(word in userinput for word in["tricks", "tips", "tip"]):
            print("Some tips for games is make sure you actually enjoy the game, otherwise there is no reason to be playing it. Practice will make you better at it, dont give up, and be persistent.")
            extra = input("Do you want tips for specific games? ").lower()
            if extra == "yes":
                print("You can get tips from these games:\n1.Minecraft\n2.Fortnite\n3.Call Of Duty\n4.GTA 5\n5.Roblox")
                choice = input()
                if choice == "1":
                    print(Fore.CYAN+"Step 1: Mark Your Spawn Point. \nStep 2: Locate Trees. \nStep 3: Punch Those Trees! \nStep 4: Start Your House. \nStep 5: Build a Crafting Table. \nStep 6: Make a Pickaxe. \nStep 7: Mine Some Stone. \nStep 8: Make a Furnace."+Style.RESET_ALL)
                elif choice == "2":
                    print(Fore.CYAN+"Avoid unnecessary fights and let other players eliminate each other. \nUse the Environment: Utilize natural cover and builds to your advantage. \nPay attention to the shrinking play area and plan your final moves carefully."+Style.RESET_ALL)
                elif choice == "3":
                    print(Fore.CYAN+"In order to get more consistent and better at the game, practice the skills to get them memorized."+Style.RESET_ALL)
                elif choice == "4":
                    print(Fore.CYAN+"Level your shooting, driving and flying skills to max as soon as you can. Do the whole tutorial, don't skip out of it, and then play various contact jobs for a while before tackling heists. "+Style.RESET_ALL)
                elif choice == "5":
                    print(Fore.CYAN+"In Roblox, there are so many different games you can try out, all you need is to have fun!"+Style.RESET_ALL)
            elif extra == "no":
                continue
            else:
                print(f"{extra} is not a valid option. Please choose tips again and type yes or no.")
        #NLP could also be used in this one  
        elif any(word in userinput for word in["video game news", "news", "gaming news"]):
            print(Fore.RED+"My Nintendo News Rumour: Mario fan thinks they have discovered the 40th anniversary account")
            print("Unreal Engine 5.6.1 Hotfix Released")
            print("Fae Farm Will Lose Online Support On Steam Next Month"+Style.RESET_ALL)
        #NLP could also be used in this one  
        elif any(word in userinput for word in["anticipated", "year", "game of year", "most"]):
             print("The most anticipated game of 2024 was Final Fantasy 7 Rebirth.")
        #NLP could also be used in this one  
        elif any(word in userinput for word in["current latest version", "latest version", "updates"]):
            print("You can get the current latest version from these games from these games:\n1.Minecraft\n2.Fortnite\n3.Call Of Duty\n4.GTA 5\n5.Roblox")
            versionwant = input()
            if choice == "1":
                    print("The current latest version of Minecraft is 1.21.100 for Bedrock Edition and 1.21.8 for Java Edition.")
            elif versionwant == "2":
                    print("The latest version of Fortnite is Chapter 6 Season 4: Shock 'N Awesome, which corresponds to update 37.00.")
            elif versionwant == "3":
                    print("The most recent Call of Duty title is Call of Duty: Black Ops 6, released in October 2024.")
            elif versionwant == "4":
                    print("The current version of Grand Theft Auto 5 (GTA 5) is 1.71.")
            elif versionwant == "5":
                    print("The latest version of Roblox is 2.685.797.")
        else:
            print(f"{userinput} is not an option, please either restart the chatbot to type a valid response.")
gamingbot()   