def layers(number):
    num = str(number)
    S, L, A, Y, E, R = num[0], num[1], num[2], num[3], num[4], num[5]
    return int(L + A + Y + E + R + S)


def slayer(number):
    if number * 3 == int(layers(number)):
        return True
    else:
        return False


if __name__ == "__main__":
    print("Guess a 6 digit number SLAYER so that the following equation is true, "
          "where each letter sands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS")
    guess = int(input("Enter your guess for SLAYER: "))
    if slayer(guess):
        print(f"Your guess is correct: SLAYER + SLAYER + SLAYER = {guess * 3}"
              f"\nLAYERS = {guess * 3}")
    else:
        print(f"Your guess is incorrect: SLAYER + SLAYER + SLAYER = {guess * 3}"
              f"\nLAYERS = {layers(guess)}")
    print("Thanks for playing.")
    
