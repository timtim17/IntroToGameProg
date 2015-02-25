# Austin Jenchi
# 2/24/2015
# 8th Period
# Shopping Cart

total_cost = 0
for i in range(1, 6):
    while True:
        try:
            cost = input("What is the price of item #%d? => " % i)
            if cost > 0:
                total_cost += cost
                break
        except NameError: pass

print "The total cost of your cart is $%2.2f." % total_cost
print
print "However, since you're buying online, your cost is $%2.2f with shipping." % (total_cost + 20)