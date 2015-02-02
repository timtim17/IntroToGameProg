# Austin Jenchi
# 01/26/2015
# Intro to Game Programming
# 8th Period
# Week 1

print "********** Exercise 1.2 **********"
print
print "   |   |   "
print "-----------"
print "   |   |   "
print "-----------"
print "   |   |   "
print

print "********** Exercise 1.4 Part II **********"
print
import math
solution1 = (3 * 5)/(2+3)
print str(solution1)
print
solution2 = math.sqrt(7 + 9) * 2
print str(solution2)
print
solution3 = math.pow(4 - 7, 3)
print str(solution3)
print
solution4 = (-19 + 100) ** (1/4)
print str(solution4)
print
solution5 = 6 % 4
print str(solution5)
print

print "********** Exercise 1.4 Part III **********"
problemA = (5 + 2)/3
problemB = 5 + 2/3

print "Problem A: ((5 + 2)/3) Solution: " + str(problemA)
print "Problem B: (5 + 2/3) Solution: " + str(problemB)
print

print "********** Exercise 1.5 **********"
print
while True:
    firstName = raw_input("What is your first name? ==> ")
    if not firstName == "": break
while True:
    lastName = raw_input("What is your last name? ==> ")
    if not lastName == "": break
print
print "Enter your date of birth:"
while True:
    try:
        birthMonth = int(raw_input("    Month? ==> "))
        if 0 < birthMonth < 13:
            break
    except ValueError: print "Nope, it has to be a number between 1 and 12."
while True:
    try:
        birthDay = int(raw_input("    Day? ==> "))
        if 0 < birthDay < 32:
            break
    except ValueError: print "Nope, it has to be a number between 1 and 31."
while True:
    try:
        birthYear = raw_input("    Year? ==> ")
        int(birthYear)  # Test to see if it actually is a number, not just four random things
        if len(birthYear) == 4:
            break
    except ValueError: print "Nope, it has to be a year (that's 4 numbers)."

print firstName + " " + lastName + " was born on " + str(birthMonth) + "/" + str(birthDay) + "/" + str(birthYear)
print

# Homework Assignment: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/assignments/MIT6_189IAP11_hw1.pdf
