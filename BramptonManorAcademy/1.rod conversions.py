def rodsIntoMeters(rods):
    return rods * 5.0292

def rodsIntoMiles(rods):
    return rods * 5.0292 / 1609.34

def rodsIntoFeet(rods):
    return rods * 5.0292 / 0.3048

def rodsIntoFurlongs(rods):
    return rods / 40

def rodsIntoMinutes(rods):
    return rodsIntoMiles(rods) * 60 / 3.1

def rodConversion():
    rods = float(input("Enter number of rods:"))

    print(f"You input {rods} rods. \n\nConversions")
    print(f"Meters: {rodsIntoMeters(rods)}")
    print(f"Feet: {rodsIntoFeet(rods)}")
    print(f"Miles: {rodsIntoMiles(rods)}")
    print(f"Furlongs: {rodsIntoFurlongs(rods)}")
    print(f"Minutes to walk {rods} rods: {rodsIntoMinutes(rods)}")

if __name__ == "__main__":
    rodConversion()
