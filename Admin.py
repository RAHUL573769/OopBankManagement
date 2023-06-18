from User import User


class Admin(User):
    def __init__(self, name, email, password, balance) -> None:
        super().__init__(name, email, password, balance)

    def createUserAccount(self, bank):
        bank.add_account(self)

    def createAdminAccount(self, bank):
        bank.add_account(self)
        self.role = "Admin"

    def makeAdmin(self, user):
        if self.role == "Admin":
            user.role = "Admin"
        else:
            print("401 Unauthorized")

    def totalBalance(self, bank):
        if self.role == "Admin":
            return bank.total_balance
        else:
            return "401 Unauthorized"

    def totalBankLoan(self, bank):
        return bank.total_loan

    def changLoan(self, bank, is_loan_available=True):
        bank.is_loan_available = is_loan_available
