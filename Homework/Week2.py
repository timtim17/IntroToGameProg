# Austin Jenchi
# 2/4/2015
# 8th Period
# Week 2

print "********** Exercise 2.4 **********"
print
# CONFIGURATION BLOCK
#
# This is the area where you can actually change the things that this program says.
# Use it if you want something other than Rocks, Papers, and Scissors
#
# ID 0 (default rock) always beats ID 2 (scissors) which always beats ID 1 (paper),
# which always beats ID 0 (rock).
#
#
weapons = ["rock", "paper", "scissors"]
error_weapons = ["rock(s)", "paper(s)", "scissors"]
#
#
# EXAMPLE CUSTOM CONFIGURATION
#
# weapons = ["soda", "pizza", "knife"]
# error_weapons = ["soda(s)", "pizza(s)", "knife(s)"]
#
# OUTPUT:
#
# Welcome to RPS Online (The Ultimate MMO RPS FPS!)!
#
# Player 1. What does thy wield? ==> rock
# Sorry, we don't have rocks in stock.
#
# We only have soda(s), pizza(s), and knife(s) in stock.
#
# Player 1. What does thy wield? ==> soda
#
# Player 2. What does thy wield? ==> knife
#
# PLAYER ONE wins, and shall pass to play another game.
#
#
# CLASSIC CONFIGURATION
#
# weapons = ["rock", "paper", "scissors"]
# error_weapons = ["rock(s)", "paper(s)", "scissors"]
#
# END OF CONFIGURATION BLOCK

print "Welcome to RPS Online (The Ultimate MMO RPS FPS!)!"

# Player One Weapon Selection
while True:
    print
    p1choice = raw_input("Player 1. What does thy wield? ==> ").lower()
    if p1choice == weapons[0]:
        p1choice = 0
        break
    elif p1choice == weapons[1]:
        p1choice = 1
        break
    elif p1choice == weapons[2]:
        p1choice = 2
        break
    else:
        print "Sorry, we don't have " + p1choice + "s in stock."
        print
        print "We only have " + error_weapons[0] + ", " + error_weapons[1] + ", and " + error_weapons[2] + " in stock."

# Player Two Weapon Selection
while True:
    print
    p2choice = raw_input("Player 2. What does thy wield? ==> ").lower()
    if p2choice == weapons[0]:
        p2choice = 0
        break
    elif p2choice == weapons[1]:
        p2choice = 1
        break
    elif p2choice == weapons[2]:
        p2choice = 2
        break
    else:
        print "Sorry, we don't have " + p2choice + "s in stock."
        print
        print "We only have " + error_weapons[0] + ", " + error_weapons[1] + ", and " + error_weapons[2] + " in stock."

print

if p1choice == 0:
    if p2choice == 0:
        print "None shall win, so none shall pass.\nThis duel shall be forever be known as a TIE."
    elif p2choice == 1:
        print "PLAYER TWO wins, and shall pass to play another game."
    elif p2choice == 2:
        print "PLAYER ONE wins, and shall pass to play another game."
elif p1choice == 1:
    if p2choice == 0:
        print "PLAYER ONE wins, and shall pass to play another game."
    elif p2choice == 1:
        print "None shall win, so none shall pass.\nThis duel shall be forever be known as a TIE."
    elif p2choice == 2:
        print "PLAYER TWO wins, and shall pass to play another game."
elif p1choice == 2:
    if p2choice == 0:
        print "PLAYER TWO wins, and shall pass to play another game."
    elif p2choice == 1:
        print "PLAYER ONE wins, and shall pass to play another game."
    elif p2choice == 2:
        print "None shall win, so none shall pass.\nThis duel shall be forever be known as a TIE."
print

# Homework Assignment: <N/A>