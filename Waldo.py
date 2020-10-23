import random

while True:
    people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye", "Dirk", "Amber"]
    random.shuffle(people)
    if people == "Waldo":
        print("We hebben waldo gevonden")
        running = False
    else:
        print(people)



