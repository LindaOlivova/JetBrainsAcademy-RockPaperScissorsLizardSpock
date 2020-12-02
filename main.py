import random

def load_rating():
    rating = open("rating.txt", "r")
    rating_lines = rating.readlines()
    rating_dictionary = {}

    for line in rating_lines:
        name, score = line.split(" ")
        rating_dictionary[name] = int(score)

    rating.close()
    return rating_dictionary

def score(name, result, rating_dictionary):
    if user_name not in rating_dictionary:
        rating_dictionary[name] = 0

    if result == 1:
        rating_dictionary[name] += 50

    if result == 2:
        rating_dictionary[name] += 100



def check_result(user_choice, computer, computer_options):
    choice_user, choice_computer = user_choice, computer

    nr_defeating_options = int((len(computer_options) - 1) / 2)
    defeating_options = []
    index = 0
    words_counting = 0
    run = True

    while run:
        for word in computer_options:
            if word == choice_user:
                words_counting += 1
                continue

            if words_counting >= 1 and words_counting <= nr_defeating_options:
                defeating_options.append(word)
                words_counting += 1
            if words_counting == nr_defeating_options + 1:
                run = False
                break

            if index == (len(computer_options)-1):
                index = 0
            index += 1


    #
    # for word in computer_options:
    #     if word == choice_user:
    #         index += 1
    #         continue
    #     if index >= 1 and index <= nr_defeating_options:
    #         defeating_options.append(word)
    #         index += 1



    if choice_user == choice_computer:
        return 1
    if choice_computer not in defeating_options:
        return 2
    return 3

def parse_computer_options(chosen_options):
    if chosen_options == "":
        return ["rock","paper","scissors"]

    return chosen_options.split(",")

def parse_user_options(options_list):
    user_list = options_list.copy()
    user_list.append("!rating")
    user_list.append("!exit")

    return user_list


user_name = input("Enter your name:")
print("Hello, " + user_name)
chosen_options = input()
print("Okay, let's start")
data = load_rating()


computer_options = parse_computer_options(chosen_options)
user_options = parse_user_options(computer_options)

while True:
    user_choice = input()
    computer = random.choice(computer_options)

    if user_choice not in user_options:
        print("Invalid input")
        continue

    if user_choice == "!rating":
        print("Your rating: {}".format(data[user_name]))
        continue

    elif user_choice == "!exit":
        print("Bye!")
        break

    else:
        result = check_result(user_choice, computer, computer_options)
        if result == 1:
            print("There is a draw ({})".format(computer))
        if result == 2:
            print("Well done. The computer {} and failed".format(computer))
        if result == 3:
            print("Sorry, but the computer chose {}".format(computer))

        score(user_name, result, data)
