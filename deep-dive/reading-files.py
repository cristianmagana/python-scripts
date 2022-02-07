# open a file

with open(input.txt, 'r') as inputFile:
    
    inputFile.readlines()  # Returns a list object
    fList = list(inputFile) # Returns a list object

    for line in inputFile:
        print(line, end='')

 
