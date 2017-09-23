import random

print("\n\nWelcome to Chris' number guessing game\n")
print("A random number will be generated between 1 and 100\n")
print("Guess the correct number and learn a secret about me!\n")
number = random.randint(1,100)
secrets = ['I have mild hearing loss :)', 'Chris takes longer than usual in the shower', 'I get distracted very easily', "It's christmas and I'm coding a noob program", "My dreams are very weird. Very."]
while True:
    try:
        question = int(input("Guess the number!"))
    except ValueError:
        print("Put in a vaild number noob!")
        continue

    if question < number:
        print("Your number is too low! Try again!")
    elif question > number:
        print("Your number is too high! Try again!")
    else:
        print("Correct!")
        random_list = random.randint(0,len(secrets))
        print(secrets[random_list])
        break
