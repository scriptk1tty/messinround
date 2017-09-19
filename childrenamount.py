import random
print("Hello dearie!")

response = input()

childrenAmount = random.randint(1, 20)

found = False

while not found:
    print ("Can you guess how many children I have?")
    guess = int(input())
    if int(guess) == childrenAmount:
        found = True
        print("That's right! Can you believe it?")
    if guess > childrenAmount:
        print("Do I look like I've had that many children?!")
    if guess < childrenAmount:
        print("No, I've had a couple more than that.")


