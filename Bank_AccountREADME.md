{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "989409d0-32ae-4c0d-9111-c7a3abe5b672",
   "metadata": {},
   "source": [
    "# Bank Account Project\n",
    "\n",
    "A simple Python class that simulates a bank account with deposit and withdrawal functionality, including input validation.\n",
    "\n",
    "---\n",
    "\n",
    "## Features\n",
    "- Optional starting balance  \n",
    "- Deposit money into account  \n",
    "- Withdraw money from account  \n",
    "- Updates account balance after each transaction  \n",
    "- Handles `TypeError` and `ValueError` for invalid input  \n",
    "\n",
    "---\n",
    "\n",
    "## How It Works (Step by Step)\n",
    "1. Create an account with a name and (optional) starting balance  \n",
    "2. Choose a deposit amount  \n",
    "3. Choose a withdrawal amount  \n",
    "4. See updated balance or error messages if input is invalid  \n",
    "\n",
    "---\n",
    "\n",
    "## Example Output\n",
    "```\n",
    "Account owner: Neo\n",
    "Account balance: 100\n",
    "\n",
    "Depositing 50…\n",
    "New balance: 150\n",
    "Deposit error: Deposit amount must be numeric\n",
    "Deposit error: Negative amounts dont work, silly goose.\n",
    "\n",
    "Withdrawing 30…\n",
    "New balance: 120\n",
    "Withdrawal error: Insufficient funds\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc414af1-18b1-4194-a3f8-41f9e43b8de2",
   "metadata": {},
   "source": [
    "---\n",
    "\n",
    "## Future Improvements\n",
    "- Interest rates  \n",
    "- Transaction history  \n",
    "- Support for multiple accounts  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39b3ada5-d609-4052-baab-93e3349e0352",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
