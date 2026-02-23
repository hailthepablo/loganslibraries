class Fraction:
    def __init__(self,numerator,denominator,sign=1):
        self.numerator = numerator
        self.denominator = denominator
        self.sign = sign
        self.update()

    def update(self):
        for i in range(len(self.numerator)):
            for j in range(len(self.denominator)):
                if self.numerator[i] == self.denominator[j]:
                    self.numerator[i] = "remove"
                    self.denominator[j] = "remove"
                    break
        newNumerator = []
        for i in self.numerator:
            if not (i == "remove" or i == 1):
                newNumerator += [i]
        newDenominator = []
        for i in self.denominator:
            if not (i == "remove" or i == 1):
                newDenominator += [i]
        if 0 in newNumerator:
            newDenominator = [1]
        self.numerator = newNumerator
        self.denominator = newDenominator

    def getInts(self):
        intNumerator = 1
        for i in self.numerator:
            intNumerator *= i
        intDenominator = 1
        for i in self.denominator:
            intDenominator *= i
        return [intNumerator,intDenominator]

    def __str__(self):
        if self.sign == -1:
            signString = "-"
        else:
            signString = ""
        if self.getInts()[1] == 1:
            return signString + str(self.getInts()[0])
        return signString + str(self.getInts()[0]) + "/" + str(self.getInts()[1])
    
    def __mul__(self,other):
        product = Fraction(self.numerator+other.numerator,self.denominator+other.denominator)
        return product
    
    def __add__(self,other):
        return Fraction(factor(self.getInts()[0]*other.getInts()[1]+self.getInts()[1]*other.getInts()[0]),factor(self.getInts()[1]*other.getInts()[1]))
    
    def __sub__(self,other):
        return Fraction(factor(self.getInts()[0]*other.getInts()[1]-self.getInts()[1]*other.getInts()[0]),factor(self.getInts()[1]*other.getInts()[1]))

def factor(number):
    if number < 0:
        sign = -1
    elif number > 0:
        sign = 1
    else:
        return [0]
    currentNum = number*sign
    factorList = []
    while currentNum != 1:
        for i in [j for j in range(number*sign+1)][2:]:
            if currentNum % i == 0:
                factorList += [i]
                currentNum = currentNum//i
                break
    if sign == -1:
        return [-1] + factorList
    return factorList

def frac(string):
    sign = 1
    newString = ""
    for i in string:
        if i == "-":
            sign *= -1
        else:
            newString += i
    newString = newString.split("/")
    if len(newString) == 1:
        newString += [1]
    return Fraction(factor(sign*int(newString[0])),factor(int(newString[1])))