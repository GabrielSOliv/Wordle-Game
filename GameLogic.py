import random

def SelectWord(language: str) -> str:
    with open('words/' + language + '.txt', 'r') as file:
        words = file.readlines()
    selected_line = words[random.randint(0, len(words) - 1)].strip().split()

    word = selected_line[random.randint(0, len(selected_line) - 1)]

    return word
   
def wordVerification (guessWord: str, rightWord: str):
    guessWord = str.lower(guessWord)
    if guessWord == rightWord:
        return list(0,1,2,3,4)
    
    remainingLetters = list(rightWord)
    rightLetters = []
    wrongPlaceLetter = []
    wrongLetter = []
    
    for i in range(len(guessWord)):
        if guessWord[i] == rightWord[i]:
            rightLetters.append(i)
            remainingLetters[i] = '-'
        
    for i in range(len(guessWord)):
        if guessWord[i] != rightWord[i]:
            if guessWord[i] in remainingLetters:
                wrongPlaceLetter.append(i)
                
                for j in range(len(remainingLetters)):
                    if guessWord[i] == remainingLetters[j]:
                        remainingLetters[j] = '-'
                        break    
            else:
                wrongLetter.append(i)
                
    return rightLetters, wrongPlaceLetter, wrongLetter


def wordExist(guessWord: str, language: str) -> bool:
    guessWord = guessWord.lower()
    
    with open('words/' + language + '.txt', 'r') as file:
        words = [line.strip().lower() for line in file]

    return guessWord in words