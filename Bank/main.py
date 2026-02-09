class BankAccount:
    
    account_counter = 1000 #class variable
    
    def __init__(self, holder_name:str, balance = 0):
        self.holder_name = holder_name,
        self.__balance = balance
        
        self.__transactions = []
        
        BankAccount.account_counter += 1
        self.account_no = BankAccount.account_counter
        
    # Getter Method
    def get_balance(self):
        return self.__balance
    
    def get_transactions(self):
        return self.__transactions
        
    # Deposite Method
    def deposit(self, amount:int):
        if amount < 0:
            return 'Deposite amount must be positive'
        
        self.__balance += amount
        self.__transactions.append(f"Deposite : {amount}")
        return f"{amount} deposited successfully"
    
    # Withdraw method
    def withdraw(self, amount:int):
        if amount < 0:
            return 'Withdraw must be positive'
        elif amount > self.__balance:
            return 'Insufficient balance'
        
        self.__balance -= amount
        
        self.__transactions.append(f"withdraw: {amount}")
        return f'{amount} withdraw successfully'
    
    def transfer(self, target_acc:str, amount:int):
        if amount < 0:
            return 'Transfer Amount must be Positive'
        
        if amount > self.__balance:
            return "Insufficient balance"
        
        self.__balance -= amount
        target_acc.__balance += amount
        
        
        self.__transactions.append(
            f"Transfered {amount} to {target_acc.account_no}"
        )
        target_acc.__transactions.append(
            f"Received {amount} from {self.account_no}"
        )
        
        return f'{amount} transfered successfully'
    

acc1 = BankAccount("Rahul", 10000)
acc2 = BankAccount("Amit", 5000)

print(acc1.deposit(2000))
print(acc1.withdraw(1500))
print(acc1.transfer(acc2, 3000))

print("Rahul Balance:", acc1.get_balance())
print("Amit Balance:", acc2.get_balance())

print("Rahul Transactions:", acc1.get_transactions())

