from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'

    def test_deposit(self):
        #negative, zero, positive
        pass

    def test_withdraw(self):
        #negative, zero, positive invalid, positive valid
        pass

