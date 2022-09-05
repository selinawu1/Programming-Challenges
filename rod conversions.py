def rodConversion():
    rods = float(input("Enter number of rods:"))
    meters = 5.0292
    miles = rods * meters / 1609.34
    print("You input " + str(rods) + " rods. \n\nConversions")
    print("Meters: " + str(rods * meters))
    print("Feet: " + str(rods * meters / 0.3048))
    print("Miles: " + str(miles))
    print("Furlongs: " + str(rods / 40))
    print("Minutes to walk "+ str(rods) + " rods: " + str(miles * 60 / 3.1))

rodConversion()
