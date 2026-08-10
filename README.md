# atm_withdrawal__system
A beginner-friendly Python ATM program that verifies a PIN, checks the available balance, and processes a withdrawal. It demonstrates nested if statements, user input, comparison operators, and conditional decision-making.
# Python ATM Withdrawal System

## 📌 Overview

The **Python ATM Withdrawal System** is a beginner-friendly program that simulates a simple ATM transaction.

The program first verifies the user's PIN. If the PIN is correct, it checks whether the account has sufficient balance for the requested withdrawal.

## ✨ Features

- PIN verification
- Balance input
- Withdrawal amount input
- Insufficient balance checking
- Remaining balance calculation
- Transaction status display

## 🛠️ Concepts Practiced

- `input()`
- Variables
- String comparison
- Integer conversion using `int()`
- `if` and `else`
- Nested `if` statements
- Comparison operators
- Basic arithmetic operations

## 💻 Source Code

```python
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
```

## ▶️ Example

### Successful Transaction

**Input:**
```text
Enter your PIN: 1234
Enter your balance: 5000
Enter your withdrawal amount: 1500
```

**Output:**
```text
Transaction successful
Remaining balance: 3500
```

### Insufficient Balance

**Input:**
```text
Enter your PIN: 1234
Enter your balance: 1000
Enter your withdrawal amount: 1500
```

**Output:**
```text
Insufficient balance
```

### Invalid PIN

**Input:**
```text
Enter your PIN: 5678
```

**Output:**
```text
Invalid PIN
```

## 📂 Project Structure

```text
Python-ATM-Withdrawal-System/
│
├── atm_withdrawal_system.py
└── README.md
```

## 🎯 Learning Objective

This project helps beginners understand nested conditional statements and how multiple conditions can be used together to build a simple decision-making system.

---

⭐ Part of my Python learning journey and beginner programming practice.
