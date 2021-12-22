import random
chance = 10
number_of_chance = 0
computer_point = 0
your_point = 0

char = ["snake", "water", "gun"]

print("welcome to ''snake, water, gun'' game\n"

      "  Gun kills snake,\n  Snake drinks water,\n"

      "  Gun drowse in water.")

while True:

    reply = random.choice(char)

    inp = input("choose your character: Snake / Water / Gun \n")

    print(reply)

    if inp == reply:

        print("Tye , both point 0")

    elif inp == "snake" and reply == "gun":

        computer_point = computer_point+1

        print(f"your point is {your_point} and computer"

              f" point is {computer_point}")

    elif inp == "snake" and reply == "water":

        your_point = your_point+1

        print(f"your point is {your_point} and computer"

              f" point is {computer_point}")

    elif inp == "water" and reply == "gun":

        your_point = your_point+1

        print(f"your point is {your_point} and "

              f"computer point is {computer_point}")

    elif inp == "water" and reply == "snake":

        computer_point = computer_point+1

        print(f"your point is {your_point} and computer"

              f" point is {computer_point}")

    elif inp == "gun" and reply == "snake":

        your_point = your_point+1

        print(f"your point is {your_point} and "

              f"computer point is {computer_point}")

    elif inp == "gun" and reply == "water":

        computer_point = computer_point+1

        print(f"your point is {your_point} and "

              f"computer point is {computer_point}")

    number_of_chance = number_of_chance+1

    print(f"{chance-number_of_chance} chance is left"

          f" out of {chance} chance")

    if chance-number_of_chance < 1:

        number_of_chance = number_of_chance + 1

        print("\ngame over")

        break

print(f"your point is {your_point} and "

      f"computer point is {computer_point}")

if computer_point > your_point:

    print("\ncomputer wins")

elif your_point > computer_point:

    print("\nyou win")

else:

    print("Tye")
