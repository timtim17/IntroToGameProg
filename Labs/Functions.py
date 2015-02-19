# Austin Jenchi
# 2/17/2015
# 8th Period
# Functions

def this_is_a_function(i_am_a_parameter):
    print i_am_a_parameter
    i_am_a_returning_value = True
    return i_am_a_returning_value

print this_is_a_function(5)
print this_is_a_function("Python")
print this_is_a_function(False)

def the_point_of_no_return():
    print str(5 + 5)

print the_point_of_no_return()

def switchingClass():
    print "Picking up bag, walking, done!"

switchingClass()

def chorus():
    print "I am a dwarf and I'm diging a hole.\nDiggy diggy hole, diggy diggy hole!"

chorus()

def switching_class_v2(className):
    print "I am now going to %s!" % className

switching_class_v2("Algebra II")
switching_class_v2("Intro to Game Programming")

def newLine():
    print

print "Odd classes on Tuesday and Thursday."
newLine()
print "Even classes on Wednesday and Friday."

def sillyAgeJoke():
    while True:
        try:
            age = input("How old are you? => ")
            if type(age) is int: break
        except: pass

    if 14 <= age <= 19:
        print "What is 13 + 49 + 84 + 155 + 97? A headache!"
    else:
        print "Huh?"

sillyAgeJoke()

def threeLines():
    newLine()
    newLine()
    newLine()

from time import sleep
print "How do you fix a broken tuba?"
sleep(5)
threeLines()
print "With a tuba glue! Ha!"

def printTwice(word):
    print word, " ", word

printTwice("woof")
printTwice(5)
from math import pi
printTwice(pi)
printTwice("meow" * 4)

def printTimes(word, times):
    from time import sleep
    for i in range(0, times):
        print word
        sleep(1)

printTimes("meow", 9999)