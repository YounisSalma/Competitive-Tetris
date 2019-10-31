import time
print("\n BUBBLE SORT: ")

#lst = []
#lstn = int(input("\n How many numbers are being entered: "))
#for i in range (0, lstn):
#    print ("\n Enter next number:")
#    elements = int(input(" "))
#    lst.append(elements)
#lstrange = (lstn-1)

pass_ = 0

lst = []

data = open(data.txt, 'r')
for line in data.readlines():
    row.append([line])
    for i in line.split(","):
        row[-1].append(i)

def bubbleSort(myList):
    global pass_
    for i in range (0, lstrange):
        for j in range (0, lstrange - i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
                print (lst)
                time.sleep(0.1)
                pass_ = pass_ + 1
    return myList

print("\n Final List:\n",bubbleSort(lst))
print("\n Amount of passes:",pass_)
