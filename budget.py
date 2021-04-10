class Budget:
    """
    Creates and manages a category budget for the user. 
    Allows users deposit, withdraw, and check the balance of the 
    specific budget category they're dealing with.  
    Users will also be able to transfer funds between categories.
    
    Each instance of the budget creates a new budget category that 
    takes the name of the category as its single argument.
    """
    def __init__(self, category):
        self.category_name = category.capitalize()
        self.balance = 0  # Every new budget class begins from zero
 
    def deposit(self):
        print(f"{self.category_name} Budget Category")
        self.deposit_amount = int(input("\nEnter deposit amount: "))
        
        while True:
            confirm_deposit = input(f"\nDeposit {self.deposit_amount} in {self.category_name} budget? [y/n] ")
            if confirm_deposit not in ['y', 'n']:
                print("\nOoops! You've selected an invalid option.")
                continue
            elif confirm_deposit == 'y':
                self.balance += self.deposit_amount
                print("\n***Congratulations!!!***")
                print(f"\nYou have successfully deposited NGN {self.deposit_amount} in your {self.category_name} budget.")
                break
            else:
                print("\n***Transaction terminated!***")
                break
 
    def withdraw(self):
        print(f"{self.category_name} Budget Category")
        self.withdraw_amount = int(input("\nHow much would you like to withdraw? \n"))
        
        while True:
            confirm_withdraw = input(f"\nWithdraw NGN {self.withdraw_amount} from {self.category_name}? [y/n] ")
            if confirm_withdraw not in ['y', 'n']:
                print("\nOoops! You've selected an invalid option.")
                continue
            elif confirm_withdraw == 'y':
                self.balance -= self.withdraw_amount
                print(f"\nYou have successfully withdrawn NGN {self.withdraw_amount}")
                break
            else:
                print("\n***Transaction terminated!***")
                break
        
    def balance_check(self):
        print(f"{self.category_name} Budget Category")
        print(f"\nYour current {self.category_name} balance is: {self.balance}")
 
    def transfer(self, receiver):
        print(f"{self.category_name} Budget Category")
        self.transfer_amount = int(input(f"\nEnter amount to transfer to {receiver.category_name}: "))
        
        while True:
            confirm_transfer = input(f"\nTransfer NGN {self.transfer_amount} from {self.category_name} to {receiver.category_name}? [y/n] ")
            if confirm_transfer not in ['y', 'n']:
                print("\nOoops! You've selected an invalid option.")
                continue
            elif confirm_transfer == 'y':
                self.balance -= self.transfer_amount  # Remove transferred amount from the transfer category
                receiver.balance += self.transfer_amount  # Add transfer amount to receiving category
                print("\n***Congratulations!!!***")
                print(f"\nYou have successfully transferred {self.transfer_amount} from {self.category_name} to {receiver.category_name}")
                break
            else:
                print("\n***Transaction terminated!***")
                break
        
        
# Instantiating sample budgets using the budget class
        
food_budget = Budget("Food")
clothing_budget = Budget("Clothing")
ent_budget = Budget("Entertainment")
health_budget = Budget("Health")

# Testing out the budgets different functions
health_budget.deposit()
health_budget.transfer(food_budget)
food_budget.balance_check()
health_budget.balance_check()
health_budget.withdraw()
health_budget.balance_check()