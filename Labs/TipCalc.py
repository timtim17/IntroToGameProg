while True:
    while True:
        try:
            bill = eval(raw_input("What is the bill? ==> $"))
            if bill > 0 and not type(bill) is str:
                break
        except: print "u fail"
    tip = .15
    print "The tip is: $%2.2f" % (bill * tip)
