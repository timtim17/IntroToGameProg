# Austin Jenchi
# 1/30/2015
# 8th Period
# Paycheck

print "Welcome to How to Job"
print
wage_per_hour = raw_input("How much is your hourly wage? ==> $")
if not wage_per_hour == "":
    try:
        wage_per_hour = float(wage_per_hour)
    except:
        wage_per_hour = 12.00
else:
    wage_per_hour = 12.00
print "Your pay is $%2.2f per hour." % wage_per_hour
print
print "You've worked 26 hours. (in one 24-hour day! remarkable!)"
print
total_wage = wage_per_hour * 26
print "Your Pay Before Taxes is $%2.2f" % total_wage
print
print "After taxes of 23%%, your total pay is $%2.2f." % (total_wage * .23)
print
print "After paying your union fees, you recieved a measly $%2.2f of your previous $%2.2f." % ((total_wage * .23) - 25, total_wage)
