import random
import operator
from time import *


def product_set_func(initial, end):
    global first_number
    first_number = random.randint(initial, end)
    global second_number
    second_number = random.randint(initial, end)

    return first_number, second_number


def division_set_func(initial, end):
    global first_number
    first_number = random.randint(initial, end)
    global second_number
    second_number = random.randint(initial, end)

    if first_number / second_number == first_number // second_number:
        return first_number, second_number
    else:
        while first_number / second_number != first_number // second_number:
            first_number = random.randint(initial, end)
            second_number = random.randint(initial, end)
        return first_number, second_number


leaderboards = {}
correct = []
incorrect = []
correct_answer_list = {}
user_difficulty_list = ["easy", "medium", "hard"]
try_again = ["play", "quit"]
op_mappings = {"+": operator.add,
               "-": operator.sub,
               "*": operator.mul,
               "/": operator.truediv}

op = ["+", "-", "*", "/"]
# Introduction
user_name = input("Please enter your name: ")

while True:
    print("----------WELCOME {} TO THE MATH QUIZ GAME----------".format(user_name.upper()))
    user_difficulty = input("Which type of difficulty do you want to play with : Easy, Medium, Hard   -->")
    user_difficulty = user_difficulty.lower()

    while user_difficulty not in user_difficulty_list:
        user_difficulty = input("Which type of difficulty do you want to play with : Easy, Medium, Hard   -->")

    # It starts counting the time elapsed for completing the quiz.
    start = time()
    counter = 0
    while counter != 10:

        if user_difficulty == "easy":
            first_number = random.randint(5, 20)
            second_number = random.randint(5, 20)
            random_operator = random.choice(op)
            # This code changes the problem values to easy ones
            if random_operator == "*":
                first_number, second_number = product_set_func(1, 10)
            if random_operator == "/":
                first_number, second_number = division_set_func(1, 10)

            answer = op_mappings[random_operator](first_number, second_number)

            # This code checks whether a problem is repeated or not, if repeated then it creates another problem.
            if "{} {} {} :".format(first_number, random_operator, second_number) in correct_answer_list.keys():
                while "{} {} {} :".format(first_number, random_operator, second_number) in correct_answer_list.keys():
                    first_number = random.randint(5, 20)
                    second_number = random.randint(5, 20)
                    random_operator = random.choice(op)
            else:
                pass

        if user_difficulty == "medium":
            first_number = random.randint(30, 80)
            second_number = random.randint(30, 80)
            random_operator = random.choice(op)
            # This code changes the problem values to easy ones
            if random_operator == "*":
                first_number, second_number = product_set_func(10, 30)
            if random_operator == "/":
                first_number, second_number = division_set_func(10, 100)

            answer = op_mappings[random_operator](first_number, second_number)

            # This code checks whether a problem is repeated or not, if repeated then it creates another problem.
            if "{} {} {} :".format(first_number, random_operator, second_number) in correct_answer_list.keys():
                while "{} {} {} :".format(first_number, random_operator, second_number) in correct_answer_list.keys():
                    first_number = random.randint(5, 40)
                    second_number = random.randint(5, 40)
                    random_operator = random.choice(op)
            else:
                pass

        if user_difficulty == "hard":
            first_number = random.randint(90, 200)
            second_number = random.randint(50, 200)
            random_operator = random.choice(op)
            # This code changes the problem values to easy ones
            if random_operator == "*":
                first_number, second_number = product_set_func(10, 40)
            if random_operator == "/":
                first_number, second_number = division_set_func(13, 200)

            answer = op_mappings[random_operator](first_number, second_number)

            # This code checks whether a problem is repeated or not, if repeated then it creates another problem.
            if "{} {} {} :".format(first_number, random_operator, second_number) in correct_answer_list.keys():
                while "{} {} {} :".format(first_number, random_operator, second_number) in correct_answer_list.keys():
                    first_number = random.randint(5, 200)
                    second_number = random.randint(5, 200)
                    random_operator = random.choice(op)
            else:
                pass

        # Sets the answer to the correct_answer_list dictionary.
        correct_answer_list["{} {} {} :".format(first_number, random_operator, second_number)] = answer

        # Manipulates over user input.
        try:
            user_inpt = float(input("{} {} {} = ".format(first_number, random_operator, second_number)))
        except ValueError:
            print("\nThis is the last chance to enter your answer in numbers")
            try:
                user_inpt = float(input("{} {} {} = ".format(first_number, random_operator, second_number)))
            except ValueError:
                print("The Game has been ended")
                break

        if user_inpt == answer:
            correct.append(user_inpt)
        else:
            incorrect.append(user_inpt)
        # Increases the counter value by 1.
        counter += 1

    # It calculates the time taken to complete the quiz.
    end_timer = time()
    difference = end_timer - start

    # This code appends the users completion data to a leaderboard.txt file.
    file = open("leaderboards.txt", "a")
    file.seek(2)
    file.write("{} -- Difficulty: {}, Time: {}, Result: {}%\n".format(user_name.capitalize(), user_difficulty,
                                                                     str(difference), str(len(correct)*10)))
    file.close()

    # Prints out the summery of the game.
    print("\nYou have completed the quiz in ", str(difference), " Seconds")
    print("\nYour result is :" + str(len(correct)*10) + "%")
    print("\n---- Here are the correct answers of the problems ----\n")
    for keys, values in correct_answer_list.items():
        print(keys, values)

    try_again_input = input("\nTo play again please enter play or quit to exit the game.")
    while try_again_input.lower() not in try_again:
        try_again_input = input("\nTo play again please enter play or quit to exit the game.")
    if try_again_input.lower() == "quit":
        print("\nTHANK YOU FOR PLAYING THE MATH QUIZ.")
        break
    if try_again_input.lower() == "play":
        # Redeclaring correct and incorrect lists as empty for correct evaluation of results when same user plays game again.
        correct = []
        incorrect = []
        continue


# This code shows the leaderboards of the quiz in all the difficulty levels.
leader_input_show = input("\nDo you want to see the leaderboards answer in yes or no.")
if leader_input_show.lower() == "yes":
    print("\nThe leaderboards are :")
    file = open("leaderboards.txt", "r")
    leader = file.readline().strip()
    while leader:
        print(leader)
        leader = file.readline().strip()
    file.close()
else:
    pass
