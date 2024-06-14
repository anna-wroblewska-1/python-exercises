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
q1 = list(quiz.keys())[0]
q2 = list(quiz.keys())[1]
q3 = list(quiz.keys())[2]

print("Hi! This is Animal Quiz.\nLet's get started!\n")

score = 0

print(q1)
answer = str(input("Answer: "))
if answer in list(quiz.values())[0]:
    print("Great!")
    score += 1
    print(f"Your score: {score}")
else:
    print("Wrong! Try next time")
    print(f"Your score: {score}")

print(q2)
answer = str(input("Answer: ").lower())
if answer in list(quiz.values())[1]:
    print("Great!")
    score += 1
    print(f"Your score: {score}")
else:
    print("Wrong! Try next time")
    print(f"Your score: {score}")

print(q3)
answer = str(input("Answer: ").lower())
if answer in list(quiz.values())[2]:
    print("Great!")
    score += 1
    print(f"Your score: {score}")
else:
    print("Wrong! Try next time")
    print(f"Your score: {score}")

print("That's it. I hope you had fun!")