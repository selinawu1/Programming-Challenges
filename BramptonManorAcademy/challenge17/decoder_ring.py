import string


def generate_dial(dial, n):
    m = 0
    new_dial = []
    for x in range(26):
        m += n - 1
        if 0 <= m < len(dial):
            new_dial.append(dial[m])
        else:
            m = m % len(dial)
            new_dial.append(dial[m])
        dial.remove(dial[m])
    return new_dial


def encrypt(first_dial, second_dial, plaintext):
    new_word = ""
    for x in range(len(plaintext)):
        new_word += second_dial[first_dial.index(plaintext[x])]
    return new_word


if __name__ == "__main__":
    first_dial = list(string.ascii_uppercase)
    n = int(input("Enter an integer between 1 and 1000000: "))
    plaintext = str(input("Enter a word: ").upper())
    second_dial = generate_dial(first_dial, n)
    
    first_dial = list(string.ascii_uppercase)
    encrypted_word = encrypt(first_dial, second_dial, plaintext)
    print(f"The encrypted word is {encrypted_word}.")
