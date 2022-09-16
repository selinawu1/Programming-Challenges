def calcEnergy(scale):
    return 10 ** (1.5 * scale + 4.8)

def calcTnt(energy):
    return energy / (4.184 * (10 ** 9))

def richterCalculator(scale):
    energy = calcEnergy(scale)
    tnt = calcTnt(energy)
    return f"Richter value: {scale} \nEquivalence in joules: {energy} \nEquivalence in tons of TNT: {tnt}"

def richterScale():
    table = {0: [1],
             1: [5],
             2: [9.1],
             3: [9.2],
             4: [9.5]
             }
    for x in range(len(table)):
        table[x].append(calcEnergy(table[x][0]))
        table[x].append(calcTnt(table[x][1]))

    print(f"{'Richter':<25}{'Joules':<25}{'TNT':<25}")
    for key, value in table.items():
        richter, joules, tnt = value
        print(f"{richter:<25}{joules:<25}{tnt:<25}")
  
if __name__ == "__main__":
    richterScale()
    scale = float(input("\nPlease enter a Richter scale value: "))
    print(richterCalculator(scale))
