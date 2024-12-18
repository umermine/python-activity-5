#Selecting a Vehical
print("Choose a vehical")
print("1. Bike")
print("2. Car")
var_vehical = input("number 1 or 2 ")
if var_vehical == 1:
    print("Which Bike would you like to choose")
    print("1.Bicycle")
    print("2.Motorbike")
    var_bike = input("number 1 or number 2 ")
    if var_bike == 1:
        print("You have selected a Bicycle")
    else:
        print("You have selected a Motorbike")
else:
    print("Which car would you like to choose")
    print("1.Ferrari Laferrari")
    print("2.Bugatti Chiron")
    var_car = input("number 1 or 2 ")
    if var_car == 1:
        print("You have selected a Farrari Laferrari")
    else:
        print("You have selected a Bugatti Chiron")
