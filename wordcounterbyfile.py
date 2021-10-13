def takefile():
    filename = input("Enter a file: ")
    numberwords = 0
    file = open(filename, "r")
    for line in file:
        words = line.split()
        numberwords = numberwords + len(words)
    print("Number of words are: ")
    print(numberwords)

takefile()
    