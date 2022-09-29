time = int(input("Enter the current hour: "))

if time < 6:
    greeting = "Good night"
elif time < 13:
    greeting = "Good morning"
elif time < 17:
    greeting = "Good day"
elif time < 24:
    greeting = "Good evening"

print("{}!".format(greeting))