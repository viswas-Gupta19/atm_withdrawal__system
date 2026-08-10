# Python ATM Withdrawal System

PIN = input("Enter your PIN: ")

if PIN == "1234":
    balance = int(input("Enter your balance: "))
    withdrawal_amount = int(input("Enter your withdrawal amount: "))

    if balance >= withdrawal_amount:
        print("Transaction successful")
        print("Remaining balance:", balance - withdrawal_amount)
    else:
        print("Insufficient balance")
else:
    print("Invalid PIN")
