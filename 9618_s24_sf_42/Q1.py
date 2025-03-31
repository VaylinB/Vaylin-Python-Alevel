WordArray = []
NumAns = -1
def ReadWords(filename):
    global NumAns,WordArray
    try:
        global NumAns
        file = open(filename,'r')
        NumAns = -1
        for line in file:
            WordArray.append(line.strip())
            NumAns += 1
        file.close()
        print(WordArray)
        Play()
    except FileNotFoundError:
        print("File is not found")

    


def Play():
    global WordArray,NumAns
    print("Main word:",WordArray[0])
    print("Number of Answers",NumAns)
    Input = ""
    Correct = 0


    Input = input("Enter word:")
    while Input != "no":
        CorrectAns = False
        for i in range(1,len(WordArray)):
            if WordArray[i] == Input:
                CorrectAns = True
                WordArray[i]=""
                break
        if CorrectAns == True:
            Correct +=1
            print("Correct!")
        else:
            print("Wrong!")
        Input = input("Enter word:")
    print("Percentage of answers found:", (Correct/NumAns)*100,"%")
    Notfound= ""
    for i in range(len(WordArray)):
        if WordArray[i] != "":
            Notfound = Notfound+","+str(WordArray[i])
    print("Answers not found:", Notfound)

Ask = input("What level?:")
Ask = Ask.capitalize()+".txt"

ReadWords("9618_s24_sf_42/"+Ask)
   
            
            

