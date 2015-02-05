# Austin Jenchi
# 2/3/2015
# 8th Period
# GPA

from time import sleep

while True:
    try:
        gpa = round(float(raw_input("What was your GPA ==> ")), 1)
        if 0.0 <= gpa <= 4.0:
            break
        else:
            print "That isn't a GPA. Take School 101, and you'll learn that a GPA is between 0.0 and 4.0!"
            print
            print "You can find it in the course catalog: http://www.lwsd.org/school/EHS/Pages/Course-Catalog.aspx"
            print
    except ValueError:
        print "That ain't no GPA!"
        print
        print "Do you know what a number is? Did you take basic math?"
        print

print

print str(gpa) + ", hmm..."

sleep(5)

print

if gpa < 2.0:
    print "Oh Dear. You're going to have to do an hour of chores."
    print "..."
    sleep(5)
    print "FOREVER!!!"
elif gpa > 3.6:
    print "CONGRAAAAAAAAAAAAAAAAATULATIONSSSSSSSSSSSS!"
    print
    print "You get to have Fridays off!!!!!!!!!!!"
else:
    print "Good Job!"
    print "/me gives pat on back"
    print "You get to leave school at 2:00 AM everyday!"
