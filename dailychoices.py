choice1 = input("Would you like a piece of candy? type yes to accept it or type no to kill the person xD")
if choice1 == "yes":
    print("You grabbed the candy and ate it")
    print("then he drove away and gave candy to other children")
    choice3 = input("what are you going to do? type play to play smash bros, or type draw")
    if choice3 == "play":
        print("You went back in the house and played some smash bros on the nintendo gameqube")
        print("THE END")
    elif choice3 == "draw":
        print("You went back inside and drew a manga and became famous")
        print("THE END")
    else:
        print("please type play or draw")
elif choice1 == "no":
    print("You took a shutgun and killed the person asking it")
    print("The police is after you, what would you do")
    choice2 = input("what would you do? type run to run or type fuckit")
    if choice2 == "run":
        print("You ran from the cops and tried to hide somewhere...")
        print("where would you hide?")
        choice4 = input("type home to go home or type plane to leave the country")
        if choice4 == "home":
            print("but you shrugged and didn't care that the cops came, you just went home")
            print("when you got home the police surrounded you and putted you behind bars...")
            print("THE END")
        elif choice4 == "plane":
            print("You first went home and took your belongings, you then ran towards the airport and went towards a other country")
            print("but someone took the whole plane hostage, what will you do")
            choice5 = input("type idc to actually die in a planecrash or type rescue")
            if choice5 == "idc":
                print("you shrugged it off and the plane crashes")
                print("GAME OVER")
            elif choice5 == "rescue":
                print("You killed the hostage holder and saved the day, yay :D")
                print("GAME OVER")
            else:
                print("Please type idc or rescue...")
        else:
            print("please type home or plane")
    elif choice == "fuckit":
        print("You committed suicide, there is no story anymore, see ya, sorry for the whole thing")
    else:
        print("please type run or fuckit")
else:
    print("please type yes or no")
