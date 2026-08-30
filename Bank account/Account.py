#Encapsulation: _balance is shielded from direct external modification and accessed safely via the @property def balance(self) getter.
#Abstraction: Callers interact through high-level methods (deposit(), withdraw(), interest_calc()) without managing the internal arithmetic or property bindings themselves.
#Inheritance: SavingsAccount and CheckingAccount reuse base properties and logic from Account using super().__init__().
#Polymorphism: CheckingAccount provides its own specialized withdraw() method that handles overdraft limits while preserving the same method name and interface as Account.
class Account:

    def __init__(self, account_holder, account_number, initial_balance=0.0):    #here balance is written like that because its like param.____. this has nothing to do and will be destroyed

       self.account_holder = account_holder
       self.account_number = account_number
       self._balance = initial_balance

    def deposit(self, amount):
        if amount<0:
            print(f"please enter an amount greater than 0")

        else:
            self._balance += amount

    def withdraw(self, amount_with):
        if amount_with<0 or amount_with> self._balance:
           print(f"Please input a valid amount")

        else: 
           self._balance = self._balance - amount_with

    @property
    def balance(self):
        return self._balance


class SavingsAccount(Account):                                   #same as pega's saying that savingsaccount is a child of account class, this child can use all things of account

    def __init__(self, account_holder, account_number, initial_balance = 0.0, interest_rate=0.05):

        #over here instead of setting savingsaccount.accountnumber == accountnumber, we basically call the super dt and call all of them in single go.
        super().__init__(account_holder, account_number, initial_balance)  
        self.interest_rate = interest_rate

    def interest_calc(self):
           interest = self._balance * self.interest_rate
           self._balance += interest
           print(f"Applied interest of ${interest:.2f} at {self.interest_rate * 100:.1f}%. New Balance: ${self._balance:.2f}")


class CheckingAccount(Account):

    def __init__(self, account_holder, account_number, initial_balance = 0.0, overdraft_limit = 500.0):

        super().__init__(account_holder, account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount_with: float) -> bool:
        max_allowable = self._balance + self.overdraft_limit
        
        if amount_with <= 0 or amount_with > max_allowable:
            print(f"Withdrawal failed: Exceeds overdraft limit. Maximum allowed: ${max_allowable:.2f}")
            return False
        
        self._balance -= amount_with
        print(f"Withdrew ${amount_with:.2f}. New Balance: ${self._balance:.2f}")
        return True

if __name__ == "__main__":
    print("--- 1. Testing Standard Account ---")
    base_acc = Account("Vikhyat", "ACC-101", 1000.0)
    base_acc.deposit(200.0)
    base_acc.withdraw(500.0)
    base_acc.withdraw(800.0)  # Fails: balance is only $700.00

    print("\n--- 2. Testing Savings Account ---")
    savings = SavingsAccount("Vikhyat", "SAV-201", 2000.0, interest_rate=0.04)
    savings.interest_calc()   # Adds 4% ($80.00) -> $2080.00
    savings.withdraw(500.0)

    print("\n--- 3. Testing Checking Account (Overdraft) ---")
    checking = CheckingAccount("Vikhyat", "CHK-301", 200.0, overdraft_limit=300.0)
    checking.withdraw(400.0)  # Allowed: balance becomes -$200.00
    checking.withdraw(150.0)  # Fails: exceeds remaining limit ($100.00 left)
    print(f"Final checking balance: ${checking.balance:.2f}")