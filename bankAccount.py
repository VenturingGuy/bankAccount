class BankAccount():
  def __init__(self, full_name, account_number, routing_number, balance):
    self.full_name = full_name
    self.account_number = account_number
    self.routing_number = routing_number
    self.balance = balance

  def deposit(amount):
    balance += amount
    print("Amount Deposited: ${amount}")

  def withdraw(amount):
    if (balance < amount):
      print("Insufficient funds.")
      balance -= 10
    else:
      balance -= amount
      print(f"Amount Withdrawn: ${amount}")
  
  def get_balance():
    print(f"Account Balance: ${balance}")

  def add_interest():
    interest = balance * 0.00083
    balance += interest

  def print_receipt():
    print(self.full_name)
    
