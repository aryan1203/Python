def Ayodhya():
    direction = ["left","right","forward","backward"]
    print("Ayodhya is the birthplace of Lord Ram, who is an important deity in the Hindu pantheon.")
    print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = input("Option (left/ right/ forword/ backward) :")
    while userInput in direction:
        if userInput == "left":
            riverSarayu()
        elif userInput == "right":
            ramMandir()
        elif userInput == "forward":
            hanumanGarhi()
        elif userInput == "backward":
            print("No return way for here .")
        else: 
            print("Please enter a valid option.")

def riverSarayu():
    direction = ["right","forward"]
    print("The Sarayu originates from Lake Mansarovar in the Himalayas and is also known as the Ghaghra and the Manas Nandini.")
    print("From here we have only two choice. Choice One.\n")
    userInput = input("Option (right/ forword) :")
    while userInput in direction:
        if userInput == "right":
            Ayodhya()
        elif userInput == "forward":
            Market()
        else: 
            print("Please enter a valid option.")

def hanumanGarhi():
    direction = ["left","right","backward", "forward"]
    print("Hanuman Garhi is a 10th-century temple of Lord Hanuman.")
    print("Lord Hanuman is himself a devotee of Lord Rama, and so it fits that Hanuman holds a place of importance at Ayodhya, the birthplace of Lord Rama")
    print("From here we have all direction to choice. Choice One.\n")
    userInput = input("Option (left/ right/ backward/ forward) :")
    while userInput in direction:
        if userInput == "left":
            Market()
        elif userInput == "right":
            ramMandir()
        elif userInput == "backward":
            Ayodhya()
        elif userInput == "forward":
            exit()
        else: 
            print("Please enter a valid option.")

def ramMandir():
    direction = ["left","forward"]
    print("Ram Mandir is a Hindu temple that is being built in Ayodhya, Uttar Pradesh, India, at the site of Ram Janmabhoomi, according to the Ramayana the birthplace of Rama, a principal deity of Hinduism.")
    print("From here we have only two choice. Choice One.\n")
    userInput = input("Option (left/ forword) :")
    while userInput in direction:
        if userInput == "left":
            Ayodhya()
        elif userInput == "forward":
            hanumanGarhi()
        else: 
            print("Please enter a valid option.")

def Market():
    direction = ["right","backward"]
    print("The famous market of Ayodhya.")
    print("From here we have only two choice. Choice One.\n")
    userInput = input("Option (right/ backward) :")
    while userInput in direction:
        if userInput == "right":
            hanumanGarhi()
        elif userInput == "backward":
            riverSarayu()
        else: 
            print("Please enter a valid option.")

while True:
    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to visit the Ayodhya.")
    print("However, during your exploration, you find yourself lost in beauty of this place.")
    print("You can choose to walk in multiple directions to find a way out.")
    name = input("Let's start with your name: ")
    print("Good luck, " +name+ ".")
    Ayodhya()