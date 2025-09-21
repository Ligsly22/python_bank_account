class Account:
    """
    A simple Bank Account class with owner and balance attributes,
    and methods to deposit and withdraw money.
    """
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Deposit amount must be numeric")
        if amount <= 0:
            raise ValueError("Negative amounts dont work, silly goose.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Withdrawal amount must be numeric")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    acct = Account("Neo", 100)
    print(acct)

    print("\nDepositing 50...")
    print("New balance:", acct.deposit(50))

    try:
        acct.deposit("50")
    except Exception as e:
        print("Deposit error:", e)

    try:
        acct.deposit(-20)
    except Exception as e:
        print("Deposit error:", e)

    print("\nWithdrawing 30...")
    print("New balance:", acct.withdraw(30))

    try:
        acct.withdraw(1000)
    except Exception as e:
        print("Withdrawal error:", e)