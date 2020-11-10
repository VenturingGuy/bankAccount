class BankAccount():
  def __init__(self, full_name, account_number, routing_number, balance):
    self.full_name = full_name
    self.account_number = account_number
    self.routing_number = routing_number
    self.balance = balance

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
    print(f"Account Balance: ${self.balance}")

  def add_interest(self):
    interest = self.balance * 0.00083
    self.balance += interest

  def print_receipt(self):
    print(self.full_name)
    
