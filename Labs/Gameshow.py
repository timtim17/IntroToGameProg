# Austin Jenchi
# 2/2/2015
# 8th Period
# Gameshow

print "WELCOME TO The Generic Gameshow!"
print

while True:
    try:
        number = int(raw_input("Enter a number between 1 and 20: "))
        if 1 <= number <= 20:
            break
        else:
            print str(number) + " is not between 1 and 20! Do you know how to count?"
            print
    except ValueError:
        print "That ain't no number!"
        print

print

if number <= 7:
    print "CONGRAAAAAAAAAAAAAAAAAAAAATULATIONS!!! You win a goat!"
else:
    print "I'm sorry, you only won a Mini Cooper."