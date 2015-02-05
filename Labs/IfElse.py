# Austin Jenchi
# 1/30/2015
# 8th Period
# IfElse

try:
    temp = int(raw_input("What is the temperature tomorrow? ==> "))
    if temp > 40:
        print "Nope, staying inside and coding."
    else:
        print "Yes! Perfect temperature to stay inside!"

    print

    gpa = float(raw_input("What is your GPA? ==> "))
    if gpa >= 3.6:
        print "Yep, you're in NHS (whatever that means :P)!"
    else:
        print "Nope."

    print

    print "Welcome to the Super Bowl!"
    print
    sea_points = int(raw_input("What will the Seahawks score be? ==> "))
    pat_points = int(raw_input("What will the Patriots score be? ==> "))
    if sea_points > pat_points:
        print "The Seahawks win!"
    elif pat_points > sea_points:
        print "The Patriots win!"
    elif sea_points == pat_points:
        print "It's a tie!"
    else:
        assert UserWarning, "You Broke the Program!!!"

    print

    hours_of_sleep = int(raw_input("How many hours of sleep did you get? ==> "))

    if hours_of_sleep >= 8:
        print "You got a good sleep!"
    else:
        print "You should get better sleep."
except:
    assert UserWarning, "u dun goofed"