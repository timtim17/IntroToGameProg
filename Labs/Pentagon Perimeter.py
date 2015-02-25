# Austin Jenchi
# 2/23/2015
# 8th Period
# Pentagon Perimeter

lengths = []

for i in range(1, 6):
    try:
        lengths.append(input("What is the length of side #%d? => " % i))
    except NameError: pass

perimeter = 0
for length in lengths:
    perimeter += length

print "\nYour pentagon's perimeter is " + str(perimeter) + "."