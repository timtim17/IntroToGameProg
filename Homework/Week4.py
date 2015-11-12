# Austin Jenchi
# 2/17/2015
# 8th Period
# Week 4

def zeller(month, day, year, returnHumanReadable):
    """
    Function that takes a birthday and uses Zeller's Algorithm to the day of the week of that day.

    Arguments:
        month (int) => month of date (1 (January) to 12 (December))
        day (int) => day of the month
        year (int) => year in form XXXX
        returnHumanReadable (bool) => return a human readable string or an int (0 - 7 = Sunday - Saturday)

    Returns:
        Either a human readable str ("Monday") or an int (1) depending on returnHumanReadable
    """

    # Input validation
    if not 1 <= month <= 12:
        print "ERROR: INVALID MONTH (Must be an int between 1 and 12)"
        return None
    elif not 1 <= day <= 31:
        print "ERROR: INVALID DAY (Must be an int between 1 and 31)"
        return None
    elif not len(str(year)) == 4 and type(year) is not int:
        print "ERROR: INVALID YEAR (Must be a int with a length of 4)"
        return None
    elif type(returnHumanReadable) is not bool:
        print "ERROR: INVALID PARAMETER FOR returnHumanReadable (Must be a bool)"
        return None

    # Now that the input is valid, lets format it
    if month <= 2:
        year -= 1
        month += 10
    else:
        month -= 2

    # Convert year to a string in order to slice out the first and second halves, then convert back to int
    year = str(year)
    century = int(year[:2])
    year = int(year[2:])

    # And now the main formula (Add 1 to make 1 = Sunday and 7 = Saturday)
    formula = ((((13 * month - 1)/5) + (year/4) + (century/4) + day + year - 2 * century) % 7) + 1

    # If the caller requested a human readable string, convert the number into a string.
    # Otherwise, just return the number.
    if returnHumanReadable:
        if formula == 1:
            return "Sunday"
        elif formula == 2:
            return "Monday"
        elif formula == 3:
            return "Tuesday"
        elif formula == 4:
            return "Wednesday"
        elif formula == 5:
            return "Thursday"
        elif formula == 6:
            return "Friday"
        elif formula == 7:
            return "Saturday"
        else:
            return None
    else:
        return formula


print "********** Zeller's Algorithm **********"
print

# The base code is from Week1.py Exercise 1.5, with a few modifications

# Ask for first name. Must not be empty string
while True:
    firstName = raw_input("What is your first name? ==> ")
    if not firstName == "": break

# Ask for last name. Must not be empty string
while True:
    lastName = raw_input("What is your last name? ==> ")
    if not lastName == "": break

print
print "Please enter a random date:"

# Ask for month between 1 and 12
while True:
    try:
        birthMonth = int(raw_input("    Month? ==> "))
        if 1 <= birthMonth <= 12:
            break
    except ValueError: print "Nope, it has to be a number between 1 and 12."

# Ask for day between 1 and 31
while True:
    try:
        birthDay = int(raw_input("    Day? ==> "))
        if 1 <= birthDay <= 31:
            break
    except ValueError: print "Nope, it has to be a number between 1 and 31."

# Ask for year with a length of 4
while True:
    try:
        # Keep year as a string to get length, then convert to int once length checked
        birthYear = raw_input("    Year? ==> ")
        if len(birthYear) == 4:
            birthYear = int(birthYear)
            break
    except ValueError: print "Nope, it has to be a year (that's 4 numbers)."

print
print "Your name is %s %s.\n\nThe day you chose was %02d/%02d/%04d.\nThe day of the week was %s." % (firstName, lastName, birthMonth, birthDay, birthYear, zeller(birthMonth, birthDay, birthYear, True))
print

# Homework Assignment: https://github.com/timtim17/IntroToGameProg/raw/master/Homework/Homework%204.docx
