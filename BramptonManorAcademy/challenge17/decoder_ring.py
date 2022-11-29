import string


def generate_dial(dial, n):
    m = 0
    counter = 1
    new_dial = []
    for x in range(26):
        print(m, dial)
        m += n - counter
        if 0 <= m < len(dial):
            new_dial.append(dial[m])
        elif len(dial) >= n:
            m -= len(dial)
            new_dial.append(dial[m])
        else:
            m = -1 * (m - len(dial))
            new_dial.append(dial[m])
        print(m, new_dial)
        dial.remove(dial[m])
    return new_dial


def encrypt(first_dial, second_dial, plaintext):
    print(first_dial)
    new_word = ""
    for x in range(len(plaintext)):
        print()
        new_word += second_dial[first_dial.index(plaintext[x])]
    return new_word


if __name__ == "__main__":
    first_dial = list(string.ascii_uppercase)
    print(first_dial)
    n = int(input("Enter an integer between 1 and 1000000: "))
    plaintext = str(input("Enter a word: ").upper())
    second_dial = generate_dial(first_dial, n)

    encrypted_word = encrypt(first_dial, second_dial, plaintext)
    print(f"The encrypted word is {encrypted_word}.")
