from typing import List
class Bank:
# '''
# Simple banking system designed on the basis of the definitions given in the problem statement.
# Time Complexity: O(1)
# Space Complexity: O(1)
# '''
    def __init__(self, balance: List[int]):
        self.bal = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= len(self.bal) and account2 <= len(self.bal):
            if self.bal[account1-1] >= money:
                self.bal[account2-1] += money
                self.bal[account1-1] -= money
                return True
            else:
                return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= len(self.bal):
            self.bal[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= len(self.bal):
            if self.bal[account-1] >= money:
                self.bal[account-1] -= money
                return True
            return False
        return False