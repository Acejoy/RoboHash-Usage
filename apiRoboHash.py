import requests
import random
import string

WEBSITE = 'https://robohash.org/'

def getWord():
    length = random.randint(1,20)
    word = ''.join(random.choices(string.ascii_letters +string.digits, k=length))
    return word


def runQuery(num):
    
    for i in range(num):
        receivedWord = getWord()
        print(f'The word is:{receivedWord}')        
        k = requests.get(WEBSITE+receivedWord)

        with open('./pics/'+receivedWord+'.png', 'wb') as f:    
            imgcontent = k.content
            f.write(imgcontent)


if __name__ == "__main__":
    freqQueries = int(input('How many images you want?'))
    runQuery(freqQueries)
