# Online java tutor
# This is the main file for the online java tutor
# It will be used to run the online java tutor


from student import Student # import the student class
import os
import time

def java_classes():
    os.system('cls' if os.name == 'nt' else 'clear')
    message = """Welcome to the Java Classes Tutorial.\nAny file that ends in .java will be a class.\nThere are three types of classes in Java; Public, Abstract, and Private"""
    print(message)
    input("Press enter to continue...")

def java_methods():
    os.system('cls' if os.name == 'nt' else 'clear')
    message = """Welcome to the Java Methods Tutorial.\nA method is a function that is defined in a class\nA method can have many variables and methods\nA method can be pulbic or private\nA method can be static or not\nA method can be abstract or not"""
    print(message)
    input("Press enter to continue...")
    

def java_objects():
    os.system('cls' if os.name == 'nt' else 'clear')
    message = """Welcome to the Java Objects Tutorial.\nAn object is a instance of a class\nAn object is made with a constructor and a destructor\nAn object can have many variables and methods\nAn object can be created with the new keyword"""
    print(message)
    input("Press enter to continue...")
    

def java_variables():
    os.system('cls' if os.name == 'nt' else 'clear')
    message = """Welcome to the Java Variables Tutorial.\nThere are 5 main variable types; String, Boolean, int, float, and char.\nBut there are so many more. You can delcare a variable without assinging it a value but you can get an error if you don't\nA String will hold words and text\nA int will hold whole numbers\nA char will hold one letter characters\nA boolean will hold either true or false\nA float will hold any number"""
    print(message)
    input("Press enter to continue...")

def quiz(stud):
    questions = {
        1: "What is the ending of a Java file?\n1. java\n2. py\n3. cc\n4. txt",
        2: "What are the types of Java classes?\n1. Abstract\n2. Public\n3. Abstract, Public and Private\n4. None of the Above",
        3: "How many variable types are there?\n1. Three\n2. Five\n3. Six\n4. Twenty",
        4: "What can a boolean variable hold?\n1. Whole numbers\n2. True/False\n3. Words/Text\n4. All of the Above",
        5: "What is an object?\n1. A Variable\n2. A class that holds Variables and Methods\n3. A Constructor\n4. A destructor",
        6: "How do you create an Object?\n1. Importing the class\n2. Same as a variable\n3. Object obj = Object()\n4. With the new keyword",
        7: "Can a method be private?\n1. True\n2. False\n",
        8: "Where are methods located?\n1. Objects\n2. Classes\n3. Both Classes and Objects\n4. None of the Above",
    }
    answers = {
        1: "1",
        2: "3",
        3: "2",
        4: "2",
        5: "2",
        6: "4",
        7: "1",
        8: "3"
    }
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Java quiz!\nYou will be asked 8 questions.\nYou will just need to type the number of the answer.")
    #time.sleep(1.5)
    for i in range(1, 9):
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Question " + str(i) + ":\n" + questions[i])
        ans = input("Answer: ")
        if ans == answers[i]:
            print("Correct!")
            stud.addCorrect()
        else:
            print("Incorrect!")
            stud.addIncorrect()
        
        
    print("You got", stud.get_score() * 100, "% correct!")
    stud.reset_num_correct()
    stud.reset_num_incorrect()
    user = input("Press enter to continue.")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input("Hi, welcome to the online java tutor.\nWhat is your name? ")    
    stu = Student(name)
    print("Hello " + stu.get_name() + "!")
    time.sleep(1)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("What would you like to do?")
        print("1. Learn about Java")
        print("2. Take a quiz")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("What do you want to learn about?")
            print("1. Classes")
            print("2. Methods")
            print("3. Variables")
            print("4. Objects")
            print("5. Back")
            choice = input("Enter your choice: ")
            if choice == "1":
                java_classes()
            elif choice == "2":
                java_methods()
            elif choice == "3":
                java_variables()
            elif choice == "4":
                java_objects()
            else:
                time.sleep(1)
        elif choice == "2":
            quiz(stu)
        else:
            break

    print("Thank you for using the Online Java Tutor!")

if __name__ == "__main__":
    main()