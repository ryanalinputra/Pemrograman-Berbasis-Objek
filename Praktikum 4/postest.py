class Bank:
    def __init__(self, code, address):
        self.code = code
        self.address = address

    def getAccounts(self):
        print(f"Bank: {self.code}, Alamat: {self.address}")

class ATM:
    def __init__(self):
        self.location = ''
        self.managedby = ''

    def withdraw(self, acc, amount):
        self.withdraw(amount)

    def deposit(self, acc, amount):
        acc.deposit(amount)
    
    def checkBalance(self, acc):
        print(f"Saldo di ATM: {acc.balance}")

class Customer:
    def __init__(self, name='', address='', dob='', card_number=0, pin=0):
        self.name = name
        self.address = address
        self.dob = dob
        self.card_number = card_number
        self.pin = pin

    def verifyPassword(self, pin=10):
        return self.pin == pin

class Account:
    def __init__(self):
        self.number = 0
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def widraw(self, amount):
        self.withdraw(amount)

class ATM_Transaction:
    def __init__(self):
        self.transaction_id = 0
        self.date = ''
        self.type = ''
        self.amount = 0
        self.post_balance = ''

    def modifies(self, acc, amount):
        acc.withdraw(amount)
        self.post_balance = str(acc.balance)


# === Skenario Objek ===
bank = Bank(20, 'grogol')
bank.getAccounts()

cust1 = Customer("Ryan", "datengan", "", "997878", 2)
print("PIN Valid:", cust1.verifyPassword())

acount = Account()
acount.deposit(50000)
acount.widraw(20000)
print(f"Saldo: {acount.balance}")

atm = ATM()
atm.location = 'Kampus'
atm.checkBalance(acount)
atm.deposit(acount, 10000)
atm.withdraw(acount, 5000)

trx = ATM_Transaction()
trx.modifies(acount, 5000)
print(f"Saldo akhir transaksi: {trx.post_balance}")