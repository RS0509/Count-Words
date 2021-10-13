sentence=input("Enter a sentence:")
charactercount=0
wordcount=1
for i in sentence:
    charactercount=charactercount+1
    if(i== ' '):
        wordcount=wordcount+1
print("number of words:")
print(wordcount)
print("number of characters:")
print(charactercount)
