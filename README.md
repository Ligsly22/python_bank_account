# Bank Account Project

A simple Python class that simulates a bank account with deposit and withdrawal functionality, including input validation.

---

## Features
- Optional starting balance
- Deposit money into account
- Return updated account balance
- Withdraw money from account
- Update account balance after each transaction
- Handles `TypeError` and `ValueError` for invalid input

---

## How It Works (Step by Step)
1. Create an account with a name and (optional) starting balance  
2. Choose a deposit amount  
3. Choose a withdrawal amount  
4. See updated balance or error messages if input is invalid  

---

## Example Output  
```
Account owner: Neo  
Account balance: 100  

Depositing 50…  
New balance: 150  
Deposit error: Deposit amount must be numeric  
Deposit error: Negative amounts dont work, silly goose.  

Withdrawing 30…  
New balance: 120  
Withdrawal error: Insufficient funds
``` 

## How to Run
```bash
python bank_account.py
```

## Future Improvements
- Interest rates  
- Transaction history  
- Support for multiple accounts  
