# Professor Hervi 
# AdamSmithcit137_listProcessing

## @adamSmith - author
## I pledge my word of honor that I have abided
## by the CSN Academic Integrity Policy while completing
## this assignment.

## @file : AdamSmithcit137_hw6 - name of file

## @1.0 The date as 2020-10--3

## @time <1 hr

## @brief - 
# orginal data a,b,c,d sotre in 2 lists:
# list1 - as entered
# list2 - in reverse

listInOrder = []
listInReverse = []

listLength = 1
while listLength > 0:
    if listLength < 0:
        print("All set, thank you.")
    else:
        listLength = int(input("how many variables?"))
        for x in range(listLength):
            print("Please enter", listLength, "more data values:")
            inputVariable = input("Please enther a value:")
            listInOrder.append(inputVariable)
            listInReverse.insert(0, inputVariable)
            listLength = listLength - 1

print(listInOrder)
print(listInReverse)
    
