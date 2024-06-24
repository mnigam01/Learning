from enum import Enum
from abc import ABC, abstractmethod

class TransactionType(Enum):
    CASH_WITHDRAWAL = 1
    BALANCE_CHECK = 2




class BankAccount:
    def __init__(self):
        self.balance = 0

class Card:

    def __init__(self, bank_account=None, card_number=0, cvv=0, expiry_date=0, name=""):
        self.bank_account:BankAccount= bank_account
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.holder_name = name
        self.pin_number = 1234


    def is_correct_pin_entered(self, pin):
        return pin == self.PIN_NUMBER


    def deduct_account_balance(self, amount):
        self.bank_account.withdrawal_balance(amount)

class User:
    def __init__(self, card:Card = None, account:BankAccount = None):
        self.card = card
        self.account = account

    def set_card(self, card):
        self.card = card

    def get_card(self):
        return self.card


class ATMState(ABC):
    
    def insert_card(self, atm, card):
        print("Something went wrong")

    def authenticate_pin(self, atm, card, pin):
        print("Something went wrong")

    def select_operation(self, atm, card, transaction_type):
        print("Something went wrong")
        
    def cash_withdrawal(self, atm, card, amount):
        print("Something went wrong")

    def display_balance(self, atm, card):
        print("Something went wrong")

    def return_card(self):
        print("Something went wrong")

    def exit(self, atm):
        print("Something went wrong")





class ATM:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_atm_instance"):
            cls._atm_instance = super(ATM, cls).__new__(cls, *args, **kwargs)
        return cls._atm_instance

    def __init__(self):
        self.current_atm_state = IdleState()
        self.atm_balance:int = 0
        self.no_of_two_thousand_notes:int = 0
        self.no_of_five_hundred_notes:int = 0
        self.no_of_one_hundred_notes:int = 0

    def set_atm_balance(self, atm_balance, no_of_two_thousand_notes, no_of_five_hundred_notes, no_of_one_hundred_notes):
        self.atm_balance = atm_balance
        self.no_of_two_thousand_notes = no_of_two_thousand_notes
        self.no_of_five_hundred_notes = no_of_five_hundred_notes
        self.no_of_one_hundred_notes = no_of_one_hundred_notes

    def deduct_atm_balance(self, amount):
        self.atm_balance -= amount

    def deduct_two_thousand_notes(self, number):
        self.no_of_two_thousand_notes -= number

    def deduct_five_hundred_notes(self, number):
        self.no_of_five_hundred_notes -= number

    def deduct_one_hundred_notes(self, number):
        self.no_of_one_hundred_notes -= number

    def print_current_atm_status(self):
        print(f"Balance: {self.atm_balance}")
        print(f"2k Notes: {self.no_of_two_thousand_notes}")
        print(f"500 Notes: {self.no_of_five_hundred_notes}")
        print(f"100 Notes: {self.no_of_one_hundred_notes}")


class IdleState(ATMState):
    def insert_card(self, atm:ATM, card:Card):
        print("Card inserted")
        atm.current_atm_state = HasCardState()

class HasCardState(ATMState):


    def authenticate_pin(self, atm:ATM, card:Card, pin):
        if card.is_correct_pin_entered(pin):
            atm.current_atm_state = SelectOperationState()
        else:
            print("Invalid Pin")
            self.exit(atm)
    
    def return_card(self):
        print("Please collect your card")
    
    def exit(self, atm:ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited Atm") 

class SelectOperationState(ATMState):
    def select_operation(self, atm:ATM, card:Card, transaction_type:TransactionType):
        if transaction_type==TransactionType.CASH_WITHDRAWAL:
            atm.current_atm_state = CashWithdrawlState()
        elif transaction_type==TransactionType.BALANCE_CHECK:
            atm.current_atm_state = BalanceCheckState()
        else:
            print("Invalid Option")
            exit()

    def exit(self, atm:ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited Atm") 

    def return_card(self):
        print("Please collect your card")

    def show_operations():
        print("Please select one operation")
        print(TransactionType.show_all_transactions())


class CashWithdrawlState(ATMState):
    def __init__(self) -> None:
        print("please enter the amount need to withdraw")
    
    def cash_withdrawal(self, atm:ATM, card:Card, amount:int):
        if amount>atm.atm_balance:
            print("insufficient fund in atm")
            exit(atm)
        elif amount>card.account_balance:
            print("insufficient fund in you account")
        else:
            card.deduct_account_balance(amount)
            atm.deduct_atm_balance(amount)


            # chain of responsibility
            cash_withdrawl_processor = FiveHundredRupeeProcessor(HundredRupeeProcessor())
            cash_withdrawl_processor.withdraw(atm, amount)
            exit(atm)

    def exit(self, atm:ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited Atm") 

    def return_card(self):
        print("Please collect your card")

class BalanceCheckState(ATMState):

    def display_balance(self, atm:ATM, card:Card):
        print(card.account_balance)
        exit(atm)
    
    def exit(self, atm:ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited Atm") 

    def return_card(self):
        print("Please collect your card")







class ATMRoom:
    def __init__(self):
        self.atm = None
        self.user = None

    def initialize(self):
        self.atm = ATM.get_atm_object()
        self.atm.set_atm_balance(3500, 1, 2, 5)
        self.user = self.create_user()

    def create_user(self):
        user = User()
        user.set_card(self.create_card())
        return user

    def create_card(self):
        card = Card()
        card.set_bank_account(self.create_bank_account())
        return card

    def create_bank_account(self):
        bank_account = BankAccount()
        bank_account.balance = 3000
        return bank_account

    def main(self):
        self.initialize()
        self.atm.print_current_atm_status()
        self.atm.get_current_atm_state().insert_card(self.atm, self.user.get_card())
        self.atm.get_current_atm_state().authenticate_pin(self.atm, self.user.get_card(), 112211)
        self.atm.get_current_atm_state().select_operation(self.atm, self.user.get_card(), TransactionType.CASH_WITHDRAWAL)
        self.atm.get_current_atm_state().cash_withdrawal(self.atm, self.user.get_card(), 2700)
        self.atm.print_current_atm_status()


if __name__ == "__main__":
    atm_room = ATMRoom()
    atm_room.main()
