from User import User


class Admin(User):
    def __init__(self, name, email, password, balance) -> None:
        super().__init__(name, email, password, balance)

    def createUserAccount(self, bank):
        bank.addAmountToAccount(self)

    def createAdminAccount(self, bank):
        bank.addAmountToAccount(self)
        self.role = "Admin"

    def makeAdmin(self, user):
        if self.role == "Admin":
            user.role = "Admin"
        else:
            print("401 Unauthorized")

    def totalBankBalance(self, bank):
        if self.role == "Admin":
            return bank.totalNumberBalance
        else:
            return "401 Unauthorized"

    def totalBankLoan(self, bank):
        return bank.totalLoan

    def changeLoanAvailability(self, bank, isLoanAvailable=True):
        bank.isLoanAvailable = isLoanAvailable
