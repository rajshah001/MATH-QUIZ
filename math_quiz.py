import random
import operator


# It is a function which is used for redeclaring the values of initial and end for product
def product_set_func(initial, end):
    global first_number
    first_number = random.randint(initial, end)
    global second_number
    second_number = random.randint(initial, end)

    return first_number, second_number


# It is a function which is used for redeclaring the values of initial and end for division 
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


counter = 0
correct = []
incorrect = []
correct_answer_list = {}
user_difficulty_list = ["easy", "medium", "hard"]

op_mappings = {"+": operator.add,
               "-": operator.sub,
               "*": operator.mul,
               "/": operator.truediv}

op = ["+", "-", "*", "/"]

# Introduction
print("----------WELCOME TO THE MATH QUIZ GAME----------")
user_difficulty = input("Which type of difficulty do you want to play with : Easy, Medium, Hard   -->")
user_difficulty.lower()

while user_difficulty not in user_difficulty_list:
    user_difficulty = input("Which type of difficulty do you want to play with : Easy, Medium, Hard   -->")

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
    user_inpt = int(input("{} {} {} = ".format(first_number, random_operator, second_number)))
    if user_inpt == answer:
        correct.append(user_inpt)
    else:
        incorrect.append(user_inpt)
    # Increases the counter value by 1.
    counter += 1

# Prints out the summery of the game.
print("\nYour result is :" + str(len(correct)*10) + "%")
print("\n---- Here are the correct answers of the problems ----\n")
for keys, values in correct_answer_list.items():
    print(keys, values)
