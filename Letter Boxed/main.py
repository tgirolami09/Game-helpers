class colors():
    GREEN = "\x1b[32m"
    RED = "\x1b[31m"
    RESET = "\x1b[39m"

color = colors()

currentWords = []
result = []
def recur(remaining:int,currentlyUsedLetters:set[str],wordListByLetter:dict[str, list],lastLetter:str):
    """
    Recursively checks word combinations
    """
    global result,currentWords
    if remaining==0:
        if len(currentlyUsedLetters)==12:
            result.append(currentWords.copy())
        return None
    
    if len(currentlyUsedLetters)==12:
        return None
    
    for word in wordListByLetter[lastLetter]:
        currentWords.append(word)
        recur(remaining-1,currentlyUsedLetters.union(set(word)),wordListByLetter,word[-1])
        currentWords.pop()

def nWordSolution(amoutOfWords:int,wordList:list,wordListByLetter:dict[str, list]):
    """
    Returns a list of solutions with exactly amoutOfWords words in the solution
    """
    global result
    result.clear()
    if amoutOfWords<=0:
        return result
    
    if amoutOfWords>=4:
        return result
    
    for word in wordList:
        currentWords.append(word)
        recur(amoutOfWords-1,set(word),wordListByLetter,word[-1])
        currentWords.pop()

    return result

with open("./letter_boxed_words.txt","r") as file:
    words=file.read().splitlines()

alphabet = set("abcdefghijklmnopqrstuvwxyz")
attached_sides:list[str] = []
sides = {}

for loop in range(4):
    i = input("Give me the 3 letters of a side : ").strip()
    alphabet-=set(i)
    attached_sides+=list(i)
    for char in i:
        sides[char]=set(i)-set(char)
    
alphabet = sorted(list(alphabet))
valid_words = []
valid_words_by_first_letter = {letter:[] for letter in attached_sides}

for word in words:
    if set(word)-set(attached_sides):
        pass
    else:
        for index,char in enumerate(word[:-1]):
            if word[index+1] in sides[char]:
                break
        else:
            valid_words.append(word)
            valid_words_by_first_letter[word[0]].append(word)

for nbWords in range(2,4):
    solutions = nWordSolution(nbWords,valid_words,valid_words_by_first_letter)
    if len(solutions)!=0:
        print(f"Here are some solutions with {nbWords} words:")
        for solution in solutions:
            print(*solution,sep=color.GREEN+" and "+color.RESET)
        break

    else:
        print(f"Did not find any solutions with {nbWords} words")

user_input = ""
while user_input!="#stop":
    user_input=input("Give me a word if its unvalid ot write '#stop' to stop : ").strip()
    if user_input=="#stop":
        break

    elif valid_words.count(user_input)!=0:
        valid_words.remove(user_input)
        valid_words_by_first_letter[user_input[0]].remove(user_input)
        print(f"Removed the word '{user_input}' on this execution, it has not been removed from the word list")

    else:
        print(f"The word '{user_input}' is not in my current list")

    for nbWords in range(2,4):
        solutions = nWordSolution(nbWords,valid_words,valid_words_by_first_letter)
        if len(solutions)!=0:
            print(f"Here are some solutions with {nbWords} words:")
            for solution in solutions:
                print(*solution,sep=color.GREEN+" and "+color.RESET)
            break

        else:
            print(f"Did not find any solutions with {nbWords} words")