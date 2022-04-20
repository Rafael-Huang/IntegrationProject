
"""
Integration project by Rafael Huang.
The project is a quiz regarding our class and general knowledge.
"""
__author__ = "Rafael Huang"
# References: Course website, W3Schools, Paulo Drefahl, Henrique Baggio

user_name = input("Please enter your name: ")
print("\nWelcome", user_name + "! This is a short quiz to test your general"
                               " knowledge about Python. Good Luck!")


def main():
    """
    This is the main function, it runs the program
    """
    play_again = True
    while play_again:
        score = 0  # defines user score
        valid_response = False
        print("\nINTEGRATION PROJECT QUIZ")
        while not valid_response:
            try:
                print("\nQuestion 1: ", sep='')  # \n will give a space between
                # the lines, making the quiz more organized and easier to see.
                print("What is the value of the following operation?" * 1)
                print("2 ** 3 + 15 / (2 * 5) = ", end='')
                # "*" means a multiplication
                # between both numbers.
                answer1 = float(input())

                if answer1 == float(2 ** 3 + 15 / (2 * 5)):
                    print("\nCorrect!")
                    score += 1
                    # if answer is correct, 1 point will be added
                    # to final score.
                else:
                    print("\nIncorrect!")
                valid_response = True
            except ValueError:
                print("invalid input, try again.")
                pass

        print("\nQuestion 2:")
        print("What is the name of the following operators in the example:")
        print("a ** b + c / d - e:")

        operator1 = input("A) **: ")
        # letter A helps indicate each question.
        if operator1.lower() == "exponent" or operator1.lower() == \
                "power":
            # two answers possible to get the correct answer.
            print("\nCorrect!")
            score += 0.25
            # if operator_1 is correct, 0.25 will be added to final score.
        else:
            print("\nIncorrect!")

        operator_2 = input("\nB) +: ")
        if operator_2.lower() == "addition" or operator_2.lower() == "add" or \
                operator_2.lower() == "plus" or operator_2.lower() == "sum":

            print("\nCorrect!")

            score += 0.25
        else:
            print("\nIncorrect!")

        operator_3 = input("\nC) /: ")
        if operator_3.lower() == "division" or operator_3.lower() == "divide":
            # lower() means that input will always be lowercase
            print("\nCorrect!")
            score += 0.25
        else:
            print("\nIncorrect!")

        operator_4 = input("\nD) -:")
        if operator_4.lower() == "subtraction" or operator_4.lower() == \
                "minus":
            print("\nCorrect!")
            score += 0.25
        else:
            print("\nIncorrect!")

        valid_response = False
        while not valid_response:
            try:
                print("\nQuestion 3: ")
                print("What is the result of the fol" + "lowing expression: ")
                result = float(input("45 % 3 - 15 // 4 = "))

                if result == float(45 % 3 - 15 // 4):
                    print("\nCorrect!")
                    score += 1
                else:
                    print("\nIncorrect!")
                valid_response = True
            except ValueError:
                print("Invalid input, try again.")

        valid_response = False
        while not valid_response:
            print("\nQuestion 4: ")
            print("What is the value of the following operation: "
                  "\n12 ** 2 - 56 * 2: ")
            print("a) 24")
            print("b) 42")
            print("c) 32")
            print("d) 30")
            answer = input("Answer: ")
            try:
                answer = int(answer)
                print("Invalid input, try again.")

            except ValueError:
                if answer == "c":
                    print("\nCorrect!")
                    score += 1
                else:
                    print("\nIncorrect!")
                valid_response = True

        valid_response = False
        while not valid_response:
            try:
                print("\nQuestion 5:")
                print("What is the correct answer of the following operation:")
                print("45 - 32/8 + 9 ** 2: ", end="")

                result = int(input())

                if result == 45 - 32 / 8 + 9 ** 2 and result != 0:
                    print("\nCorrect!")
                    score += 1
                else:
                    print("\nIncorrect!")

                valid_response = True
            except ValueError:
                print("Invalid input, try again.")

        valid_response = False
        while not valid_response:
            print("\nQuestion 6: ")
            print("[monkeys, sharks, elephants]")
            print("What animal is in index 1: ")
            animal = input("Animal: ")
            try:
                animal = int(animal)
                print("\nInvalid input, try again.")

            except ValueError:
                if animal == "sharks":
                    print("\nCorrect!")
                    score += 1
                    valid_response = True
                else:
                    print("\nIncorrect!")
                    valid_response = True

            print("\nQuestion 7: ")
            print("[blue, red, yellow, orange, green, brown, white]")
            print("what colors are in range(0, 2, 4): ")

            for x in range(0, 2, 4):
                position0 = str(input("\nEnter color in position 0: "))
                if position0 == "blue":
                    print("\nCorrect!")
                    score += 1
                else:
                    print("\nIncorrect!")
                position2 = str(input("\nEnter color in position 2: "))
                if position2 == "yellow":
                    print("\nCorrect!")
                    score += 1
                else:
                    print("\nIncorrect!")
                position4 = str(input("\nEnter color in position 4: "))
                if position4 == "green":
                    print("\nCorrect!")
                    score += 1
                else:
                    print("\nIncorrect!")
                    break

            print("\nQuestion 8: ")
            print("\nWhich type of loop would be used if i know how m`any "
                  "times the program will run? ")
            keep_running = True
            while keep_running:
                loop = str(input())
                if loop.lower() == "for loop" or loop.lower() == "for":
                    print("\nCorrect!")
                    score += 1
                if loop == "while loop" or loop == "while":
                    print("\nIncorrect!")
                keep_running = False

        # displaying player's final score
        if score > 5.5:
            print("\n"+user_name+",your final score is {} /10.0"
                                 "\nCongratulations!You passed!".format(score))
        else:
            print("\n"+user_name+", your final score is {} /10.0\nDue to your "
                                 "score,you didn't pass.Try again!"
                  .format(score))
        valid_option = True
        while valid_option:
            print("Select option: \n1) Play again \n2) Exit Game \n3) "
                  "Show Answers")
            choice = input("")
            if choice == '1':
                pass
                valid_option = False
            elif choice == '2':
                valid_option = False
                play_again = False
            elif choice == '3':
                print("\n1)9.5 \n\n2)a)exponent or power\n  b)addition, "
                      "add, plus, or sum\n  c)division or divide\n  "
                      "d)subtraction or minus  \n\n3)-3 \n\n4)C  \n\n5)122.0"
                      "\n\n6)sharks\n\n7)0 = blue \n  2 = yellow \n  4 = green"
                      "\n\n8)for loop or for")
                valid_option = False
                play_again = False
            else:
                print("invalid option")


main()
