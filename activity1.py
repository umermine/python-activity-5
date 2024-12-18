#Adding variables
medical_cause = input("Did you have a Medical cause Y or N ")
#Writing code
if medical_cause == 'y' or medical_cause == 'Y':
    print("You are allowed")
else:
#Adding more variables
    atten = int(input("Enter your attendence "))
#Writing code
    if atten >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")