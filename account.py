class Account:
    def __init__(self, name: str) ->None:
        '''
        Function to set up account object
        :param name: Account name
        '''
        self.__name = name

    def deposit(self, amount: float) -> bool:
        '''
        Function to deposit into the users account
        :param amount: Currency amount
        :return: Boolean value
        '''
        pass

    def withdraw(self, amount: float) -> bool:
        '''
        Function ot withdraw money from the users account
        :param amount: Currency amount
        :return: Boolean value
        '''
        pass

    def get_balance(self):
        pass

    def get_name(self):
        pass

