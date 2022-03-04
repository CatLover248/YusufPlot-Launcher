import fun

def console():
    print("Welcome to YusufPlot-Launcher!")
    print("Commands:")
    print(" help - shows list of commands.")
    print(" run - runs YusufPlot.")
    print(" update - updates and reinstalls YusufPlot using git.")
    print(" install - installs YusufPlot.")
    print(" quit - quits YusufPlot Launcher")

    while True:
        user_input = input("YusufPlot-Launcher > ")
        if user_input.strip().lower() == "help":
            print("Commands:")
            print(" help - shows list of commands.")
            print(" run - runs YusufPlot.")
            print(" update - updates and reinstalls YusufPlot using git.")
            print(" install - installs YusufPlot.")
            print(" quit - quits YusufPlot Launcher")
        elif user_input.strip().lower() == "run":
            fun.run()
        elif user_input.strip().lower() == "update":
            fun.clone_repo("https://github.com/FatyCaty/YusufPlot")
        elif user_input.strip().lower() == "install":
            fun.clone_repo("https://github.com/FatyCaty/YusufPlot")
        elif user_input.strip().lower() == "quit":
            quit()
        else:
            print("Invalid command, do help for a list of commands.")