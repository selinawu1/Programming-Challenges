def richterScale():
    table = {1: [1],
             2: [5],
             3: [9.1],
             4: [9.2],
             5: [9.5]
             }
    for x in range(len(table)):
        table[x + 1].append(pow(10, (1.5 * float(table[x + 1][0]) + 4.8)))
        table[x + 1].append(float(table[x + 1][1]) / (4.18 * pow(10, 9)))

    print("{:<25} {:<25} {:<25}".format("Richter", "Joules", "TNT"))
    for key, value in table.items():
        richter, joules, tnt = value
        print("{:<25} {:<25} {:<25}".format(richter, joules, tnt))

def richterCalculator():
    scale = float(input("\nPlease enter a Richter scale value: "))
    energy = 10 ** (1.5 * scale + 4.8)
    tnt = energy / (4.18 * 10 ** 9)
    return "Richter value: " + str(scale) + "\nEquivalence in joules: " + str(
        energy) + "\nEquivalence in tons of TNT: " + str(tnt)

if __name__ == "__main__":
    richterScale()
    print(richterCalculator())
