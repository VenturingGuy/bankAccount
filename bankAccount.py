import random

def account_num(n):
    starting_range = 10**(n-1)
    ending_range = (10**n) - 1
    return str(random.randint(starting_range, ending_range))

class BankAccount():
  def __init__(self, full_name):
    self.full_name = full_name
    self.account_number = account_num(8)
    self.routing_number = "121000358"
    self.balance = 0
  

  def deposit(self, amount):
    self.balance += amount
    print("Amount Deposited: ${amount}")

  def withdraw(self, amount):
    if (self.balance < amount):
      print("Insufficient funds.")
      self.balance -= 10
    else:
      self.balance -= amount
      print(f"Amount Withdrawn: ${amount}")
  
  def get_balance(self):
    print(f"Account Balance: ${'%.2f' % self.balance}")

  def add_interest(self):
    interest = self.balance * 0.00083
    self.balance += interest

  def print_receipt(self):
    print(self.full_name)
    print(f"Account No.: ****{self.account_number[4:]}")
    print(f"Routing No.: {self.routing_number}")
    print(f"Balance: ${'%.2f' % self.balance}")
    
luis = BankAccount("Luis Ventura")

luis.print_receipt()

simon = BankAccount("Simon Belmont")

simon.deposit(100)

simon.get_balance()

simon.add_interest()

simon.withdraw(10)

simon.get_balance()

adrian = BankAccount("Adrian Tepes")

adrian.withdraw(10)

adrian.get_balance()