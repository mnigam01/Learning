from enum import Enum
from abc import ABC, abstractmethod

class TransactionType(Enum):
    CASH_WITHDRAWAL = 1
    BALANCE_CHECK = 2


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

class Card:
    def __init__(self, bank_account=None, card_number=0, cvv=0, expiry_date=0, name=""):
        self.bank_account = bank_account
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.holder_name = name
        self.pin_number = 1234

    def is_correct_pin_entered(self, pin):
        return pin == self.pin_number

    def deduct_account_balance(self, amount):
        self.bank_account.balance -= amount

class User:
    def __init__(self, card=None, account=None):
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
        self.atm_balance = 0
        self.no_of_five_hundred_notes = 0
        self.no_of_one_hundred_notes = 0

    def set_atm_balance(self, atm_balance, no_of_two_thousand_notes, no_of_five_hundred_notes, no_of_one_hundred_notes):
        self.atm_balance = atm_balance
        self.no_of_five_hundred_notes = no_of_five_hundred_notes
        self.no_of_one_hundred_notes = no_of_one_hundred_notes

    def deduct_atm_balance(self, amount):
        self.atm_balance -= amount

    def deduct_five_hundred_notes(self, number):
        self.no_of_five_hundred_notes -= number

    def deduct_one_hundred_notes(self, number):
        self.no_of_one_hundred_notes -= number

    def print_current_atm_status(self):
        print(f"Balance: {self.atm_balance}")
        print(f"500 Notes: {self.no_of_five_hundred_notes}")
        print(f"100 Notes: {self.no_of_one_hundred_notes}")


class CashWithdrawProcessor(ABC):
    def __init__(self, processor=None) -> None:
        self.next_processor = processor

    def withdraw(self, atm, amount):
        if self.next_processor:
            self.next_processor.withdraw(atm, amount)
        else:
            raise Exception("Can't fulfill the request")


class FiveHundredRupeeProcessor(CashWithdrawProcessor):
    def __init__(self, processor=None) -> None:
        super().__init__(processor)

    def withdraw(self, atm: ATM, amount):
        no_of_notes = amount // 500
        can_fulfill = min(no_of_notes, atm.no_of_five_hundred_notes)
        atm.deduct_five_hundred_notes(can_fulfill)
        amount -= can_fulfill*500
        if amount>0:
            super().withdraw(atm, amount)
        # if no_of_notes <= atm.no_of_five_hundred_notes:
        #     atm.deduct_five_hundred_notes(no_of_notes)
        #     # atm.deduct_atm_balance(no_of_notes * 500)
        #     balance = amount%500
        #     if balance!=0:
        #         super().withdraw(atm,balance)
        # else:
        #     atm.deduct_five_hundred_notes(atm.no_of_five_hundred_notes)
        #     # atm.deduct_atm_balance(atm.no_of_five_hundred_notes * 500)
        #     amount -= atm.no_of_five_hundred_notes * 500
        #     super().withdraw(atm, amount)


class HundredRupeeProcessor(CashWithdrawProcessor):
    def __init__(self, processor=None) -> None:
        super().__init__(processor)

    def withdraw(self, atm: ATM, amount):
        no_of_notes = amount // 100
        can_fulfill = min(no_of_notes, atm.no_of_one_hundred_notes)
        atm.deduct_one_hundred_notes(can_fulfill)
        amount -= can_fulfill*500
        if amount>0:
            super().withdraw(atm, amount)

        # no_of_notes = amount // 100
        # if no_of_notes <= atm.no_of_one_hundred_notes:
        #     atm.deduct_one_hundred_notes(no_of_notes)
        #     # atm.deduct_atm_balance(no_of_notes * 100)
        # else:
        #     atm.deduct_one_hundred_notes(atm.no_of_one_hundred_notes)
        #     # atm.deduct_atm_balance(atm.no_of_one_hundred_notes * 100)
        #     amount -= atm.no_of_one_hundred_notes * 100
        #     super().withdraw(atm, amount)


class IdleState(ATMState):
    def insert_card(self, atm: ATM, card: Card):
        print("Card inserted")
        atm.current_atm_state = HasCardState()


class HasCardState(ATMState):
    def authenticate_pin(self, atm: ATM, card: Card, pin):
        if card.is_correct_pin_entered(pin):
            atm.current_atm_state = SelectOperationState()
            print("Card validated")
        else:
            print("Invalid Pin")
            self.exit(atm)

    def return_card(self):
        print("Please collect your card")

    def exit(self, atm: ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited ATM")


class SelectOperationState(ATMState):
    def select_operation(self, atm: ATM, card: Card, transaction_type: TransactionType):
        if transaction_type == TransactionType.CASH_WITHDRAWAL:
            atm.current_atm_state = CashWithdrawalState()
        elif transaction_type == TransactionType.BALANCE_CHECK:
            atm.current_atm_state = BalanceCheckState()
        else:
            print("Invalid Option")
            self.exit(atm)

    def exit(self, atm: ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited ATM")

    def return_card(self):
        print("Please collect your card")

    @staticmethod
    def show_operations():
        print("Please select one operation")
        for transaction in TransactionType:
            print(transaction.name)


class CashWithdrawalState(ATMState):
    def cash_withdrawal(self, atm: ATM, card: Card, amount: int):
        if amount > atm.atm_balance:
            print("Insufficient funds in ATM")
            self.exit(atm)
        elif amount > card.bank_account.balance:
            print("Insufficient funds in your account")
        else:
            card.deduct_account_balance(amount)
            atm.deduct_atm_balance(amount)

            # Chain of responsibility
            cash_withdraw_processor = FiveHundredRupeeProcessor(HundredRupeeProcessor())
            cash_withdraw_processor.withdraw(atm, amount)
            self.exit(atm)

    def exit(self, atm: ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited ATM")

    def return_card(self):
        print("Please collect your card")


class BalanceCheckState(ATMState):
    def display_balance(self, atm: ATM, card: Card):
        print(card.bank_account.balance)
        self.exit(atm)

    def exit(self, atm: ATM):
        self.return_card()
        atm.current_atm_state = IdleState()
        print("Exited ATM")

    def return_card(self):
        print("Please collect your card")


if __name__ == "__main__":
    account = BankAccount(100000)
    user = User(Card(account), account)
    atm = ATM()
    atm.set_atm_balance(16000, 0, 30, 10)
    atm.current_atm_state.insert_card(atm, user.card)
    atm.current_atm_state.authenticate_pin(atm, user.card, 1234)
    atm.current_atm_state.select_operation(atm, user.card, TransactionType.CASH_WITHDRAWAL)
    atm.current_atm_state.cash_withdrawal(atm, user.card, 16000)

    print(atm.atm_balance)
    print(atm.no_of_five_hundred_notes)
    print(atm.no_of_one_hundred_notes)
    print(user.card.bank_account.balance)
