#quiz game
#Create a quiz game where users answer questions:
#Store questions and answers.
#Keep score.
#Provide feedback on correct and incorrect answers.

#welcome -> question -> good/bad = score -> end bye

quiz = {"How many legs have a spider?": "8",
        "What color is an elephant?": "grey",
        "Who is bigger: alligator or crocodile?": "crocodile"
        }

print("Hi! This is Animal Quiz.\nLet's get started!\n")

score = 0

for key, value in quiz.items():
    print(key)
    answer = str(input("Answer: ").strip().lower())
    if answer == value:
        print("Great!")
        score += 1
    else:
        print("Wrong! Try next time")
    print(f"Your score: {score}")

print("That's it. I hope you had fun!")
