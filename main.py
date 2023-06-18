from User import User
from Bank import Bank
from Admin import Admin


def main():
    bank = Bank("Baper Bank", "Uganda")

    # adding user from bank
    user1 = User("Chan Mia", "chan@mia.com", "1234", 1000)
    bank.addAmountToAccount(user1)

    user2 = User("Kala Manik", "kala@manik.com", "45678", 5000)
    bank.addAmountToAccount(user2)

    # user can create account by themselves
    user3 = User("Kopa Samsu", "kopa@samsu.com", "adbdsc", 7000)
    user3.create_account(bank)

    # bank.list_accounts()
    print("#############################################\n")

    # user can deposit money
    user1.deposit_money(bank, 1070)
    user1.deposit_money(bank, 4000)
    user1.withdraw_money(bank, 1000)
    user1.withdraw_money(bank, 2000)
    user1.deposit_money(bank, 3000)
    user1.transfer_money(user2, 1000, bank.totalNumberBalance)

    bank.provide_loan(user3, 1400, 10, 2)

    # print("-------------- Transaction History --------------")
    # user1.get_transaction_history()
    # user2.get_transaction_history()

    bank.makeAdmin(user1)

    user4 = Admin("Yo Yo Kid", "yoyo@kid.com", "54967", 1000)
    user4.createAdminAccount(bank)

    print(f"Total Bank Balance: {user4.totalBankBalance(bank)}")
    # print(f"Total Bank Loan: {bank.totalNumberBalance}")
    print(f"Total Bank Loan: {user4.totalBankLoan(bank)}")
    # print(f"Total Bank Loan: {bank.totalLoan}")
    user4.changeLoanAvailability(bank, False)
    print(f"Is loan available: {bank.isLoanAvailable}")

    bank.list_accounts()


if __name__ == "__main__":
    main()
