# is_on = True
# game_state = "continue" if is_on else "don't continue"
# print(game_state)


# import random
# num = random.randint(0, 11)
# guess_number = int(input('Enter an integer: >>> '))
# result = 'number has been guessed correctly' if guess_number == num else 'number was incorrect'
# print(result)





def welcome():
    user = input("Enter name: >>> ")
    return f"hello, {user}." if user == "Rob" else f"you are not the main user."

print(welcome())
