print("Welcome to my computer quiz!")

playing = input("Do you want to play(Y/N)? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("correct!")
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("correct!")
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")
if answer == "power suply":
    print("correct!")
else:
    print("Incorrect!")
    