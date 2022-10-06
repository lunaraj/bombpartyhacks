import pyautogui as pg
import time
import random as rand
def sortLength(words):
    wordList = []
    for i in words:
        wordList.append(i)
    wordList.sort(key=len)
    wordList.reverse()
    return wordList

def randomLetters():

    length = rand.randint(2, 3)


def main():
    words = open('words.txt', 'r')
    final = sortLength(words)

    for j in range(100):
        print(final[j])


    
if __name__ == '__main__':
    main()