# Austin Jenchi
# 02/10/2015
# 8th Period
# Save Data

from datetime import datetime as date
from time import sleep

filename = date.now().strftime('%m%d%Y-%H%M%S') + ".json"

file = open(filename, "w")

data = raw_input("Please enter some data:\n")

file.write(data)

sleep(1)

file = open(filename)

file.read()