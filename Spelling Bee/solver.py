import os

scriptAbsolutePath = os.path.dirname(os.path.abspath(__file__))
fileRelativePath = "../Wordlists/spelling_bee_words.txt"
usablePath = os.path.join(scriptAbsolutePath, fileRelativePath)

with open(usablePath,"r") as file:
    words=file.read().splitlines()

words.sort(key=len)
alphabet = list("abcdefghijklmnopqrstuvwxyz")
centerLetter = input("What is the main letter : ")
sideLetters = list(input("What are the 6 other letters : ").replace(" ","").lower())

for letter in sideLetters:   
    alphabet.pop(alphabet.index(letter))
alphabet.pop(alphabet.index(centerLetter))

valid_words = []
for word in words:
    if centerLetter in word:
        for letter in alphabet:
            if letter in word:
                break
        else:
            valid_words.append(word)

    
print("The words that work are :")
print(*sorted(valid_words))
print("There are",len(valid_words),"words")
print("The pangrams are :")
for word in valid_words:
    for letter in sideLetters:
        if letter not in word:
            break
    else:
        print(word)