def commaSlice(stringInput, commaIndex):
    commaCount = 0
    sliceStart = 0
    sliceEnd = len(stringInput)
    for count, char in enumerate(stringInput, start = 0):
        if char == ',':
            commaCount += 1
        if commaCount == commaIndex and sliceStart == 0:    
            sliceStart = count + 1
        if commaCount == commaIndex + 1 and sliceEnd == len(stringInput):
            sliceEnd = count 
    return stringInput[sliceStart:sliceEnd]

print(commaSlice("abc,123,4de5", 1)) #output should be 123
print(commaSlice("woijngfoiashdfa", 3)) #output should be woijngfoiashdfa
print(commaSlice(",,,woijngfoiashdfa", 3)) #output should be woijngfoiashdfa
print(commaSlice("woijngf,,oias,hdf,a", 3)) #output should be hdf