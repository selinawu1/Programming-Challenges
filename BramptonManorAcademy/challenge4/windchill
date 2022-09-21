def windchill(temp, speed):
    return 35.74 + 0.6215 * temp - 35.75 * speed ** 0.16 + 0.4275 * temp * speed ** 0.16

def temp_index(temp, speed):
    return f"Temperature of {temp} and speed of {speed} gives windchill of: {windchill(temp, speed)}"

if __name__ == "__main__":
    print(f"{temp_index(10, 15)}\n{temp_index(0, 25)}\n{temp_index(-10, 35)}")
    temperature = float(input("Temperature: "))
    speed = float(input("Speed: "))
    print(f"Windchill: {windchill(temperature, speed)}")
