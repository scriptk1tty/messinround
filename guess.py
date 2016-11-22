import random
print("Hello, what is your favorite number?")
number= input()

print("Your favorite number is " + number +".")

minNumber = 1
maxNumber = 100
faveNumber = random.randint(1, 10000)

print("That's awesome! My favorite number is " + str(faveNumber) + ".")

message = "Now you need to guess the magic number. It is between {0} and {1}."
print(message.format(minNumber, maxNumber))

magicNumber = random.randint(minNumber, maxNumber)

found = False

while not found:
    print("Guess what it is?")
    guess = input()
    if guess == str(magicNumber):
        found = True
        print("You got it!")
    if guess < str(magicNumber):
        print("Too low.")
    if guess > str(magicNumber):
        print("Too high.")
