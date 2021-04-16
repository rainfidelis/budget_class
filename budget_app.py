import budget

budget_dict = {
    'Food': budget.Budget("Food"),
    'Clothing': budget.Budget("Clothing"),
    'Entertainment': budget.Budget("Entertainment"),
    'Health': budget.Budget("Health"),
    'Transport': budget.Budget("Transport")
}


def operations(budget_category):
    while True:
        
        try:
            operation = int(input("\nWhat would you like to do today? "
                "Enter: \n1 - Deposit \n2 - Withdrawal \n3 - Transfer \n"))
        except TypeError:
            raise TypeError("\nInvalid command! Try again...")
            continue
        
        if operation == 1:
            budget_category.deposit()
            break
        
        elif operation == 2:
            budget_category.withdraw()
            break
        
        elif operation == 3:
            receiver_name = input("\nEnter name of receiving account: ").strip().capitalize()
            receiver = budget_dict[receiver_name]
            budget_category.transfer(receiver)
            break
        
        else:
            print("\nInvalid command! Try again...")
            continue


def main():
    print("-----"*5)
    print("Rain Wallet")
    print("-----"*5)

    while True:
        print("\nExisting budget categories: ")
        
        for category in budget_dict:
            print(category)
        
        budget_to_run = input("\nEnter the name of the budget you wish to run or enter 1 to create a new budget category: ").strip().capitalize()

        if budget_to_run == '1':
            budget_to_create = input("\nEnter name of budget to create: ").strip().capitalize()
            
            if budget_to_create not in budget_dict:
                budget_dict[budget_to_create] = budget.Budget(budget_to_create)
                print(f"\nNew budget category created: {budget_to_create}")
                
            else:
                print(f"\n{budget_to_create} Budget Category already exists.")
            
            budget_to_run = budget_to_create  # Set the new budget category as budget_to_run so it runs immediately
            pass

        if budget_to_run not in budget_dict:
            print("\nYour selected category does not exist.")
            continue

        else:
            print(f"\n***{budget_to_run} Budget***")
            print(f"\n{budget_to_run} Balance: NGN {budget_dict[budget_to_run].balance}")
            operations(budget_dict[budget_to_run])
            run_again = input("\nWould you like to carry out another operation? \n[y/n]: ").lower()
            
            if run_again == 'y':
                continue
            else:
                print("\nSee you later!")
                break

if __name__ == '__main__':
    main()