class Account:
    def __init__(self, name: str) ->None:
        '''
        Function to set up account object
        :param name: Account name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Function to deposit into the users account
        :param amount: Currency amount
        :return: Boolean value
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount: float) -> bool:
        '''
        Fuction to withdraw currency from the users account
        :param amount: Currecny amount
        :return: Boolean value
        '''
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self):
        '''
        Function to return the account balance
        :return: account balance
        '''
        return self.__account_balance

    def get_name(self):
        '''
        Function to return the account holders name
        :return: account holders name
        '''
        return self.__account_name