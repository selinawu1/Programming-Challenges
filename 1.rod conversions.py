def rodConversion():
    rods = float(input("Enter number of rods:"))

    def intoMeters():
        return rods * 5.0292

    def intoMiles():
        return rods * 5.0292 / 1609.34

    def intoFeet():
        return rods * 5.0292 / 0.3048

    def intoFurlongs():
        return rods / 40

    print("You input " + str(rods) + " rods. \n\nConversions")
    print("Meters: " + str(intoMeters()))
    print("Feet: " + str(intoFeet()))
    print("Miles: " + str(intoMiles()))
    print("Furlongs: " + str(intoFurlongs()))
    print("Minutes to walk "+ str(rods) + " rods: " + str(intoMiles() * 60 / 3.1))


rodConversion()

