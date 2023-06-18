from User import TrxHistory, LoanDetails


class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.accounts = []
        self.totalNumberBalance = 0
        self.totalLoan = 0
        self.isLoanAvailable = True

    def addAmountToAccount(self, user):
        self.accounts.append(user)
        self.totalNumberBalance += user.balance
        self.totalLoan += user.loan
        obj = TrxHistory("own", user.balance, "Deposit")
        user.transaction_history.append(obj)

    def remove_account(self, user):
        self.accounts.remove(user)
        self.totalNumberBalance -= user.balance
        self.totalLoan -= user.loan

    def makeAdmin(self, user):
        user.role = "Admin"

    def deposit(self, user, amount):
        res = False
        if amount > 0:
            user.balance += amount
            self.totalNumberBalance += amount

            res = True
        else:
            print("Invalid amount")

        return res

    def withdraw(self, user, amount):
        res = False
        if user.balance >= amount:
            if self.totalNumberBalance >= amount:
                user.balance -= amount
                self.totalNumberBalance -= amount

                res = True
            else:
                print("Bank is bankrupt")
        else:
            print("Insufficient balance")

        return res

    def provide_loan(self, user, amount, interest, duration):
        if self.totalNumberBalance >= amount:
            if self.isLoanAvailable and amount <= 2 * user.balance:
                user.loan += amount
                user.balance += amount
                self.totalNumberBalance -= amount
                self.totalLoan += amount

                obj = LoanDetails(user.name, amount, interest, duration)
                user.loan_history.append(obj)
            else:
                print("Loan is not available")
        else:
            print("Bank is bankrupt")

    def get_totalNumberBalance(self):
        return self.totalNumberBalance

    def get_totalLoan(self):
        return self.totalLoan

    def list_accounts(self):
        print("\n-------------- All Accounts --------------------\n")
        for account in self.accounts:
            print(
                f"Name: {account.name} \nEmail: {account.email} \nBalance: {account.balance} \nLoan: {account.loan} \nRole: {account.role}"
            )
            print("--------------------------------------------------\n")
