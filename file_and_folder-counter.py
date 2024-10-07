import os
hdr = "Welcome to the file-counter!"
middle = hdr.center(130)
print(middle)
print()
while True:
    for list in["(1) Count files and folders in a given path","\033[33m(2) Social Media/Contact\033[0m","\033[31m(3) End the program\033[0m"]:
        print(list)

    chc1 = int(input("Please type your choice (1,2 or 3): "))
    if chc1 == 1:
        counter1 = 0
        counter2 = 0
        pth = input("Please enter the path of the folder")
        print()
        for pathhh in os.listdir(pth):                      #Lists every file and folder-name in the given directory from "pth"
            if os.path.isfile(os.path.join(pth, pathhh)):   #Checks if the current checked file is really a file and combines the inputted directory, as well as the currently checked file
                counter1 += 1
            elif os.path.isdir(os.path.join(pth)):
                counter2 += 1
        print(f"Number of \033[31mfiles\033[0m: {counter1}")
        print(f"Number of \033[31mfolders\033[0m: {counter2}")
        print()
    elif chc1 == 2:
        print()
        for list in[
            "\033[36mDiscord\033[0m: TimespyPShell",
            "\033[33mInstagram\033[0m: faxi.ffoo",
            "LinkedIn\033[0m: boyeinschaf",
            "\033[32mGithub\033[0m: Colleblock83"
        ]:
            print(list)
            print()
    elif chc1 == 3:
        exit()
    else:
        input("Sorry I didn't understand your input.")









