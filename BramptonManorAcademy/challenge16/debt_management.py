
def interest(percentage, debt):
    rate = (percentage / 100)
    return rate * debt


def repayment(debt, percentage):
    rate = percentage / 100
    if rate * debt > 50:
        payment = rate * debt
    else:
        payment = 50
    return payment


if __name__ == "__main__":
    debt = 100
    amount = 0
    count = 0
    interest_percentage = int(input("Enter rate of interest: "))
    repayment_percentage = int(input("Enter rate of repayment: "))
    while debt > 0:
        debt += interest(interest_percentage, debt)
        print(amount, debt)
        amount += repayment(debt, repayment_percentage)
        debt -= repayment(debt, repayment_percentage)
        if debt < 0:
            amount += debt
        count += 1

    print(f"Total amount repaid : {round(amount, 2)}")
    print(f"Total number of repayments: {count}")
