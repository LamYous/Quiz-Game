print("Welcome to my computer quiz!")

playing = input("Do you want to play(yes/no)? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ").lower()
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ").lower()
if answer.lower() == "power suply":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score / 4) * 100}%.")
    