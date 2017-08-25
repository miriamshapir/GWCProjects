####### BINARY SEARCH #######

# Prompt user to enter a city - Pay attention the the lower/higher case letters
searchKey = input("What city are you looking for?: ")

# Initialize variables
foundCity = ""
found = False
firstPoint = 0
lastPoint = len(citiesList)-1

# Loop thru the citiesList by updating the midPoint
while (): # ADD YOUR CODE HERE

    midPoint = int((firstPoint + lastPoint) / 2)

    # If the city found
    if ():  # ADD YOUR CODE HERE



    # Else if the city is less than the citiesList midPoint in an alphabetic order
    elif ():  # ADD YOUR CODE HERE



    # Else if the city is greater than the citiesList midPoint in an alphabetic order
    elif ():  # ADD YOUR CODE HERE



# If the city is found, then print the city name. Else, print an error message!
if (found == True):
    print("Your city is in the city list. It is %s." % foundCity)
else:
    print("Your city is not in the city list!")
