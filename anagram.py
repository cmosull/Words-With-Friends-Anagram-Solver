
def CheckDict(anagram):

    lines = open('enable1.txt','r').read().split('\n')

    anagramlength = len(anagram)
    good_words = list()

    for line in lines:
        wordcheck = 0
        lengthline = len(line)
        if (lengthline < anagramlength):
            checklength = lengthline
        elif (lengthline > anagramlength):
            continue
        else:
            checklength = anagramlength

        lettercounter = 0
        temp_anagram = anagram
        
        for lineletter in range(checklength):
            temp_lettercounter = lettercounter
            for anagramletter in temp_anagram:
                if (line[lineletter] == anagramletter):
                    temp_anagram = temp_anagram.replace(line[lineletter], "", 1)
                    lettercounter += 1
                    break

            if (temp_lettercounter == lettercounter):
                wordcheck = 1  

        if (wordcheck == 0):
            good_words.append(line)

    return good_words

def SortAnagrams(words):
    words.sort()
    words.sort(key= lambda s: len(s))
    return words