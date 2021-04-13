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
        deposit_amount = int(input("\nEnter deposit amount: "))
        
        while True:
            confirm_deposit = input(f"\nDeposit {deposit_amount} in {self.category_name} budget? \n[y/n]: ")
        
            if confirm_deposit not in ['y', 'n']:
                print("\nOoops! You've selected an invalid option.")
                continue
        
            elif confirm_deposit == 'y':
                self.balance += deposit_amount
                print("\n***Congratulations!!!***")
                print(f"\nYou have successfully deposited NGN {deposit_amount} in your {self.category_name} budget.")
                break
        
            else:
                print("\n***Transaction terminated!***")
                break
 

    def withdraw(self):
        withdraw_amount = int(input("\nHow much would you like to withdraw? \n"))
        
        while True:
            confirm_withdraw = input(f"\nWithdraw NGN {withdraw_amount} from {self.category_name}? \n[y/n]: ")
            
            if confirm_withdraw not in ['y', 'n']:
                print("\nOoops! You've selected an invalid option.")
                continue
            
            elif confirm_withdraw == 'y':
                if withdraw_amount > self.balance:
                    print("\nInsufficient balance")
                    break
                else:
                    self.balance -= withdraw_amount
                    print(f"\nYou have successfully withdrawn NGN {withdraw_amount}")
                    break

            else:
                print("\n***Transaction terminated!***")
                break
        

    def transfer(self, receiver):
        transfer_amount = int(input(f"\nEnter amount to transfer to {receiver.category_name}: "))
        
        while True:
            confirm_transfer = input(f"\nTransfer NGN {transfer_amount} from {self.category_name} to {receiver.category_name}? \n[y/n]: ")
            
            if confirm_transfer not in ['y', 'n']:
                print("\nOoops! You've selected an invalid option.")
                continue
            
            elif confirm_transfer == 'y':
                if transfer_amount > self.balance:
                    print(f"\nTransfer amount excedes existing balance in {self.category_name}")
                    break
                else:
                    self.balance -= transfer_amount  # Remove transferred amount from the transfer category
                    receiver.balance += transfer_amount  # Add transfer amount to receiving category
                    print("\n***Congratulations!!!***")
                    print(f"\nYou have successfully transferred {transfer_amount} from {self.category_name} to {receiver.category_name}")
                    break
            
            else:
                print("\n***Transaction terminated!***")
                break
        
