from math import sqrt

number = int(raw_input("Enter the number you wish to check if it's prime: "));
print ""

def isPrime (number):
    ''' Check if a number is Prime. Takes int and returns bool.'''
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        boundary = int(round(sqrt(number)))

        for i in range(2, boundary):
            if number % 1 == 0:
                return False;

        return True;

if isPrime(number) == True:
    print "%s is a prima number." % number
else:
    print "%s is not a prime number." % number