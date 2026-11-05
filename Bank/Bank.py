def show_balance(balance):
  print(f"Your current balance is: ${balance:.2f}", flush=True)
def deposit():
  print("--------------------------------")
  amount = float(input("Enter amount to deposit: "))
  print("--------------------------------")
  if amount < 0:
    print("Transaction failed. Please enter a valid amount.")
    return 0
  else:
    return amount

def withdraw(balance):
  print("--------------------------------")
  amount = float(input("Enter amount to withdraw: "))
  print("--------------------------------")
  if amount > balance:
    print("Insufficient funds. Transaction failed.")
    return 0
  elif amount < 0:
    print("Amount must be greater than 0.")
    return 0
  else:
    return amount

def main():
  balance = 0
  is_running = True

  while is_running:
    print("****************************************")
    print("    Welcome to the Bank!  ")
    print("****************************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("****************************************")
    choice = input("Please choose an option: ")
    if choice == "1":
       show_balance(balance)
    elif choice == "2":
       balance += deposit()
    elif choice == "3":
       balance -= withdraw(balance)
    elif choice == "4":
       is_running = False
    else:
       print("***************************************")
       print("Invalid option. Please try again.")
       print("***************************************")

  print("Thank you for using the Bank! Have a great day!")

if __name__ == "__main__":
  main()