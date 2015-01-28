# Austin Jenchi
# 01/27/2015
# Intro to Game Programming
# 8th Period
# TipCalc

while True:
    try:
        bill = input("What is the bill? ==> $")
        if bill > 0 and not type(bill) is str:
            break
    except: print "u fail"
tip = .15
print "The tip is: $%2.2f" % (bill * tip)
