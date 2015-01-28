name = raw_input("Gimme a name! ==> ")
adj = raw_input("Gimme a adjective! ==> ")
noun = raw_input("Gimme a noun! ==> ")
you_shall_pass = False
while not you_shall_pass:
    you_shall_pass = True
    verb = raw_input("Gimme a verb ending in -ing! ==> ")
    if len(verb) > 2:
        for i in range(len(verb) - 3, len(verb)):
            if i == len(verb) - 3:
                if not verb[i] == 'i': you_shall_pass = False
            elif i == len(verb) - 2:
                if not verb[i] == 'n': you_shall_pass = False
            elif i == len(verb) - 1:
                if not verb[i] == 'g': you_shall_pass = False
    else:
        you_shall_pass = False
                
            
color = raw_input("Gimme a color! ==> ")
print
print name + " was " + verb + " at the " + color + " " + adj + " " + noun + "."
print
print "Now Gimme Some Money"
