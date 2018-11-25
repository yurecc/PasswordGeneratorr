import random as r
alphabet = []
symbols = ('=', '+', '_', '-', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', ',', '.', '<', '>', '?')
dictionary = ['a', 'b', 'c', 'd']

def geniratepasswd(n, alphabet):
    for i in range(0, n):
        passletter = r.choice(alphabet)
        print(passletter, end = '')
    print()    

def letterindictionary():
    if alphabet[i] = dictionary[i][0]:
        print(dictionary[i], end = " ")
        print()

question = (">How strong your password should be? ")
for letter in range(97,123):
    alphabet.append(chr(letter))
    alphabet.append(r.randint(1, 10))
    alphabet.append(chr(letter).upper())
    alphabet.append(r.choice(symbols))

print(question)
n = int(input(">Enter password length: "))
while True:
    if n < 16:
        answer = input(">Password is too short, continue?(y or n): ")
        if answer == 'y':
            n = int(input(">Enter password length: "))
            geniratepasswd(n, alphabet)
            break
        elif answer == 'n':
            geniratepasswd(n, alphabet)
            break
    elif n > 16:
        geniratepasswd(n, alphabet)
        break


