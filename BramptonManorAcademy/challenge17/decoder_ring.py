import string


def generate_dial(dial, n):
    new_dial = []
    new_dial.append(dial[n - 1])
    for _ in range(24):
        print(n, new_dial)
        n += n
        if 0 <= n < 26:
            new_dial.append(dial[n - 1])
        else:
            n -= 26
            new_dial.append(dial[n-1])
    return new_dial


def encrypt(first_dial, second_dial, word):
    new_word = ""
    for x in range(len(word) - 1):
        new_word += second_dial[first_dial.index(word[x])]
    return new_word


if __name__ == "__main__":
    first_dial = list(string.ascii_uppercase)
    print(first_dial)
    n = int(input("Enter an integer between 1 and 1000000: "))
    word = input("Enter a word: ").upper
    second_dial = generate_dial(first_dial, n)

    encrypted_word = encrypt(first_dial, second_dial, word)
    print(f"The encrypted word is {encrypted_word}.")
