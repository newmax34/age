driving = input("have you driven a car before?")
if driving != "Yes" and driving != "No":
    print("You should only answer 'Yes' or 'No'")
    raise SystemExit
    
age = int(input("what is your age?"))
if driving == "Yes":
    if age >= 18:
        print ("You passed the test.")
    else: 
        print("That's odd...how come you've driven car before?")
elif driving == "No":
    if age >= 18:
        print ("You should go get a driver's license.")
    else: 
        print ("Good. When you are 18, you can go get a driver's license.")

    