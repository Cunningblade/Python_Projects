print("Quizzzzzz")
name = input("What is your Name?\n")
print("Welcome",name,"\n")
start = input("Do you want to start Playing : Press Y for 'START PLAYING' otherwise Press Anything to exit:")
if start != 'Y':
    quit()
score = 0
Question = 1
print("Your Score is 0 ")
# Games Start

#Question 1
print("Question",Question,":")
answer = input("Who is known as the Father of Geometry?\n")
Question += 1
if answer.lower() == "euclid":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

#Question 2
print("Question",Question,":")
answer = input("Which is the biggest animal on earth?\n")
Question += 1
if answer.lower() == "blue whale":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

#Question 3
print("Question",Question,":")
answer = input("How many days does a leap year have?\n")
Question += 1
if answer == "366":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

#Question 4
print("Question",Question,":")
answer = input("Who wrote the Mahabharata?\n")
Question += 1
if answer.lower() == "ved vyasa":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

#Question 5
print("Question",Question,":")
answer = input("Which is the smallest ocean?\n")
Question += 1
if answer.lower() == "arctic ocean":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

#Question 6
print("Question",Question,":")
answer = input("Which organ is responsible for the purification of blood in the human body?\n")
Question += 1
if answer.lower() == "kidney":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

#Question 7
print("Question",Question,":")
answer = input("What do you call a shape that has six sides?\n")
Question += 1
if answer.lower() == "hexagon":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

#Question 8
print("Question",Question,":")
answer = input("Which part of the human body has the smallest bone?\n")
Question += 1
if answer.lower() == "ear":
    print("Correct Answer!!\nYour Score is increased by 1\n")
    score += 1
else:
    print("OOps Wrong Answer!\n")

print("Your Gussed",score,"correctly.")
print("Your Percentage of correct answer is:",((score/8)*100),"%")


        
    


