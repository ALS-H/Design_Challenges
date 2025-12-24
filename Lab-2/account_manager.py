class AccountManager:
    """
    Method to store account details into the account object passed
    """
    def fill_account_data(self, acc):
        #the bug is account details are not set but are being called in getters (Nonetype can't be concatenated)
        acc.acc_no="123456"
        acc.name="Haneela"
        acc.balance=5000.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print()
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))
