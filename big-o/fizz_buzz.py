"""
Write a function, fizz_buzz, that takes in a number n as an argument. The function should return a list containing numbers from 1 to n, replacing certain numbers according to the following rules:

if the number is divisible by 3, make the element "fizz"
if the number is divisible by 5, make the element "buzz"
if the number is divisible by 3 and 5, make the element "fizzbuzz"

Example #1:
fizz_buzz(11) # -> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11]

Example #2:
fizz_buzz(2) # -> [1,2]

"""

def fizz_buzz(n: int):
    results = []
    for i in range(1, n+1):
        if(i % 3 == 0 and i % 5 == 0):
            results.append("fizzbuzz")
        elif(i % 3 == 0):
            results.append("fizz")
        elif(i % 5 == 0):
            results.append("buzz")
        else:
            results.append(i)


    return results

print(fizz_buzz(11))
print(fizz_buzz(2))

"""
Analysis:
Time complexity: O(n)
Space complexity: O(n)

Lessons learnt:
1. if you want to check if a number is devisible by multiple numbers, for example x, y You have 2 options:
    a) if number % x == 0 and number % y == 0
    b) if number % LCM(x, y) == 0. LCM - Least Common Multiple
"""