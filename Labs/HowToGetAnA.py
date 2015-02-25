# Austin Jenchi
# 2/23/2015
# 8th Period
# How to Get an A

while True:
    try:
        numtests = input("How many tests did you take? => ")

        if type(numtests) is int and numtests > 0: break
    except NameError: pass

scores = []
for i in range(1, numtests):
    while True:
        try:
            scores.append(input("What was your grade for test #%d? => " % i))
            break
        except NameError: pass

_sum = 0
for score in scores:
    _sum += score

average = _sum/len(scores)

print "Your grade was a %2.1f average." % average