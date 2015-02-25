# Austin Jenchi
# 2/23/2015
# 8th Period
# Counting Chars

# Setup Char Tracking Array

alpha = []

for i in range(27):
    if i == 0:
        alpha.append({'char': 32, 'count': 0})
    else:
        alpha.append({'char': i + 96, 'count': 0})
       
# var to track unknown chars 
unknown_chars = 0

my_str = raw_input("Please type a string. => ").lower()

for i in my_str:
    matched = False
    for j in alpha:
        if j['char'] == ord(i):
            j['count'] += 1
            matched = True
            break
    if not matched:
        unknown_chars += 1

for i in alpha:
    if not i['count'] == 0:
        if alpha.index(i) == 0:
            print "Spaces: %d" % i['count']
        else:
            print "%s: %d" % (chr(i['char']), i['count'])

if not unknown_chars == 0:
    print "Unknown Chars: %d" % unknown_chars