

def generateShifterArray(x=2):
    shifterTarget=[]
    shifterCounter=[]
    startBits=[]
    for i in range(0,x):
        shifterTarget.append(2**i)
        shifterCounter.append(0)
        startBits.append("0")
    return shifterTarget,shifterCounter,startBits

def flipBitAtIndex(bitSequence,i):
    if bitSequence[i]=="0":
        bitSequence[i]="1"
    else:
        bitSequence[i]="0"
    return bitSequence


def generateVectorSpace(x=2):
    space=[]
    size=2**x
    wordSize=x
    shifterTarget,shifterCounter,startBits=generateShifterArray(x)
    for i in range(0,size):
        word=""
        for j in range(0,wordSize):
            if(shifterCounter[j]<shifterTarget[j]):
                shifterCounter[j]=shifterCounter[j]+1
            else:
                startBits = flipBitAtIndex(startBits, j)
                shifterCounter[j]=0
                shifterCounter[j]=shifterCounter[j]+1

            word=startBits[j]+word

        space.append(word)
    return space


def checkSpecificStringOnCondition(indexArray,string):
    counter=0
    for i in indexArray:
        if string[i-1]=="1":
            counter=counter+1
    if (counter%2==0):
        return True
    else:
        return False

def checkAllStringConditions(conditionsIndexArrays,string):
    valid = True
    for conditionArray in conditionsIndexArrays:
        if (not checkSpecificStringOnCondition(conditionArray,string)):
            valid = False

    return valid

def getAllValidCodes(codeSet,conditionsIndexArrays):
    validCodes=[]
    for code in codeSet:
        if checkAllStringConditions(conditionsIndexArrays, code):
            validCodes.append(code)
    return validCodes



def checkDistance(code1, code2):
    maxIndex=len(code1)
    i=0
    distance=0
    while(i<maxIndex):
        if (code1[i]==code2[i]):
            pass
        else:
            distance=distance+1
        i=i+1
    return distance

def checkMinDistnaceOfSet(codeSet):
    i=0
    minDistance=10000000000
    while(i<len(codeSet)):
        j=i+1
        while(j<len(codeSet)):
            dist=checkDistance(codeSet[i],codeSet[j])
            if (dist<minDistance):
                minDistance=dist
            j=j+1
        i=i+1
    return minDistance

def correctError(errorCode,validCodes):
    i=0
    nearestCode=None
    minDistance=1000000
    while i<len(validCodes):
        distance=checkDistance(errorCode,validCodes[i])
        if (distance<minDistance):
            nearestCode=validCodes[i]
            minDistance=distance
            # print(nearestCode,distance)
        i=i+1
    return nearestCode,minDistance


codeSet=generateVectorSpace(7)
print(codeSet)
validCodes=getAllValidCodes(codeSet,[[1,3,5,7],[2,3,6,7],[4,5,6,7]])
print(validCodes)
minDistance=checkMinDistnaceOfSet(validCodes)
print("minimum distance is: ",minDistance)
print("errors that can be detected are: ",(minDistance-1))
print("errors that can be correted are: ",(minDistance-1)//2)

codeOkToCheck='0001101'
correctedCode, correctedCodeDistance=correctError(codeOkToCheck,validCodes)
print("we check the correction of "+codeOkToCheck+" its result is "+correctedCode+" with distance of "+str(correctedCodeDistance))
