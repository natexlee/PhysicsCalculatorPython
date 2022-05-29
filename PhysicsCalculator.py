
#Physics calculator by Nate Lee

from unittest import case
from xml.etree.ElementTree import tostring

#Unit values
unit = input("Please enter a unit to solve for: ").strip().lower()


# units = {"distance": int(input("Enter a distance (meters): ")), 
# "time": int(input("Enter a time (seconds): ")), 
# "velocity": int(input("Enter a velocity (m/s): "))






if (unit == "velocity"):
    # units["distance"]
    # units["time"]
    distance = int(input("Enter a distance (meters): "))
    time = int(input("Enter a time (seconds): "))
    answer = distance / time
    print("Velocity = " + str(round(answer)) + " m/s")

elif (unit == "acceleration"):
    velocity = int(input("Enter a velocity (m/s): "))
    time = int(input("Enter a time (seconds): "))
    answer = velocity / time
    print("Acceleration = " + str(round(answer)) + " m/s^2")

elif (unit == "final velocity"):
    initialVelocity = int(input("Enter an initial velocity (m/s): "))
    acceleration = int(input("Enter an acceleration (m/s^2): "))
    time = int(input("Enter an time (seconds): "))
    answer = initialVelocity + int(acceleration * time)
    print(str(round(answer)) + " m/s")



