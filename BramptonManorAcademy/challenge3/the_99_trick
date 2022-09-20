def your_part(answer):
    return 99 - answer

def friends_part(factor):
    num1 = int(input("*Player* Pick any number between 50-99: "))
    num2 = str(num1 + factor + 1)
    return num1 - int(num2[1:])

def the99trick(fin, ans):
    return f"I said the answer was {fin} and the calculation result is {ans}"

if __name__ == "__main__":
    print("We are going to play a game.")
    answer = int(input("*You* This will be the answer. Select a number between 10-49: "))
    factor = your_part(answer)
    final = friends_part(factor)
    print(the99trick(final, answer))
