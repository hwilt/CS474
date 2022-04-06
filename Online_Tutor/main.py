# Online java tutor
# This is the main file for the online java tutor
# It will be used to run the online java tutor


from student import Student # import the student class
import os
import time


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input("Hi, welcome to the online java tutor.\nWhat is your name? ")    
    stu = Student(name)
    print("Hello " + stu.get_name() + "!")
    time.sleep(1)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hi")
        print("What would you like to do?")
        print("1. Check your score")
        print("2. Add a correct answer")
        print("3. Add an incorrect answer")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your score is " + str(stu.get_score()))
        elif choice == "2":
            stu.addCorrect()
        elif choice == "3":
            stu.addIncorrect()
        else:
            break

if __name__ == "__main__":
    main()