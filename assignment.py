# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = [-1] * 10
TopOfStack = -1

def IsEmpty():
    return TopOfStack == -1

def IsFull():
    return TopOfStack == 9


# Exercise 2
def Push(Item):
    global TopOfStack
    if IsFull():
        return False
    TopOfStack = TopOfStack + 1
    Stack[TopOfStack] = Item
    return True


# Exercise 3
def Pop():
    global TopOfStack
    if IsEmpty():
        return -1
    DataToReturn = Stack[TopOfStack]
    TopOfStack = TopOfStack - 1
    return DataToReturn


# Exercise 4
def Peek():
    if IsEmpty():
        return -1
    return Stack[TopOfStack]

def Size():
    return TopOfStack + 1


# Exercise 5
def ReverseWord(Word):
    global TopOfStack
    ReversedWord = ""
    TopOfStack = -1
    for Letter in Word:
        Push(Letter)
    while not IsEmpty():
        ReversedWord = ReversedWord + Pop()
    return ReversedWord

