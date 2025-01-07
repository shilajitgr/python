import datetime
import pytz


class Account:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]

    def __str__(self):
        return f"Account owner: {self._name}\nAccount balance: Rs. {self.__balance}"

    def deposit(self, dep_amt):
        self.__balance += dep_amt
        print("Deposit Accepted")
        self.show_balance()
        self._transaction_list.append((Account._current_time(), dep_amt))

    def withdraw(self, wd_amt):
        if self.__balance >= wd_amt:
            self.__balance -= wd_amt
            print("Withdrawal Accepted")
            self._transaction_list.append((Account._current_time(), -wd_amt))
        else:
            print("Funds Unavailable!")
        self.show_balance()
    
    def show_balance(self):
        print(f"Balance: {self.__balance}")
        
    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount:6} {tran_type} on {date.astimezone(pytz.timezone('Asia/Kolkata'))}")
            
    @staticmethod
    def _current_time():
        utc_time = pytz.utc.localize(datetime.datetime.now())
        return utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
            
if __name__ == "__main__":
    # 1. Instantiate the class
    shilz = Account("Shilajit", 100)
    shilz.show_balance()
    
    shilz.deposit(50)
    shilz.withdraw(5)
    shilz.withdraw(500)
    shilz.show_transactions()
    
    # every object has its own namespace and a static method is not part of it but
    # since the static method is part of the parent's namespace, it can be accessed by the object
    
    # Hence, accessing a static method from an object is slightly inefficient since, 
    # it resolution will be first attempted in the instances namespace and the class' namespace
    shilz.__balance = 1000000   
    # This will not change the balance of the object as balance is a private attribute
    # and its name has been mangled to _Account__balance by python interpreter
    shilz.show_balance()
    print(shilz.__dict__)
    shilz._Account__balance = 1000000   # This will change the balance of the object
    shilz.show_balance()
    