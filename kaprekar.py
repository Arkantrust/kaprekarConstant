# For any 4-digit number with at least 2 different digits. If arranged in descending and ascending order and substracted, eventually we will get Kaprekar's constant = 6174.

def convertNumberToList(numberString: str) -> list[int]:
    '''Converts a number in string format to an int list in the form of [x, x, x, x]
    numberString: A string with an int value e.g. '1234'
    Returns an int list of length 4 with each position as a digit of the given number e.g. [1, 2, 3, 4]
    '''
    sequence = [0, 1, 2, 3]  # List to separate the number digits

    # i is the index for both sequence and num, stores every digit in sequence list
    for i in range(4):
        sequence[i] = int(numberString[i])
    return sequence

def hasDifferentDigits(numberString: str) -> bool:
    '''This function checks that the number entered has at least 2 different digits, as in xxyy.
    numberString: A string with the value of an int e.g. 1234.
    Returns True or False depending on weather or not the number has different digits.
    '''
    itDoes = True
    for digit in range(4):
        currentDigit = numberString[digit]
        nextDigit = numberString[digit+1]
        if currentDigit != 3 and currentDigit != nextDigit:
            itDoes = True
        elif numberString[digit] == numberString[digit+1]:
            continue
        else:
            itDoes = False
    return itDoes

def organizeNumbers(digits: list[int], order: str) -> list[int]:
    ''' This function organizes the digits of the given number in ascending or descending order.
    digits: The list with the digits.
    order: The desired order for the digits, 'asc' for ascending 'desc' for descending.
    Returns the list of digits organised.
    '''
    if order == 'desc':
        return digits.sort(reverse=True)
    elif order == 'asc':
        return digits.sort()

def SubstractOrganizedNumbers(minuendList: list[int], subtrahendList: list[int]) -> int:
    ''' This function receives two lists with numbers digits in the form of [x,x,x,x],
    casts them as ints and then substracts the smmall number(subtrahend) from the big number(minuend) and returns the result.
    minuendList: The list with the digits in descending order.
    subtrahendList: The list with the digits in ascending order.
    Returns the result of the substraction of both numbers.
    '''
    minuend = ''
    subtrahend = ''
    for i in range(4):
        minuend = minuend+str(minuendList[i])
        subtrahend = subtrahend+str(subtrahendList[i])
    minuend = int(minuend)
    subtrahend = int(subtrahend)
    result = minuend - subtrahend
    return result

def performIteration(number: str) -> int:
    ''' This function performs all the necessary steps to make a 4 digit number with at least 2 different digits into Kaprekar's constant.
    '''
    digitsList = convertNumberToList(number)
    descendingList = digitsList.sort(reverse=True)
    ascendingList = digitsList.sort()
    result = SubstractOrganizedNumbers(descendingList, ascendingList)
    return result

number = performIteration('1234')
process = 1

constant = 6174

while number != constant:
    number = performIteration(str(number))
    process += 1


# --------------------------------------------------------------------------------
'''listaPrueba = convertNumberToList('1234')

tempList = tuple(listaPrueba)

descendiente = organizeNumbers(listaPrueba, 'descending')

listaPrueba = list(tempList)
ascendiente = organizeNumbers(listaPrueba, 'ascending')

numberList = ['1234', '1212', '1122', '1221', '1112', '1222', '1111']

while True:
    # number = input('4-digit number: ')

    for i in numberList:
        print(performIteration(i))
        if len(i) != 4:
            print('\nThe number given must contain exactly 4 digits\n')
            continue
    # if not differentDigits(number):
    #     print('\nThe number must contain at least 2 different digits')
    #     continue
    break '''
#---------------------------------------------------------------------------------

print(f"The number {number} reaches Krapekar's constant after {process} iterations")


