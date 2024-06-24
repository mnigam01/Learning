from abc import ABC, abstractmethod
from enum import Enum
import traceback

class Coin(Enum):
    PENNY = 1 
    NICKEL = 5
    DIME = 10
    QUARTER = 25

class ItemType(Enum):
    COKE = 1
    PEPSI = 2
    SODA = 3
    JUICE =4

class Item:
    def __init__(self, type, price) -> None:
        self.price:int = price
        self.type:ItemType = type
    
class ItemShelf:
    def __init__(self, code=0, soldOut=True, item=None) -> None:
        self.code = code
        self.soldOut = soldOut
        self.item = item

class Inventory:
    def __init__(self, no_of_items) -> None:
        # each item will occupy one row like pepsi on top shelf something like this
        self.shelfs:List[ItemShelf] = [None]*no_of_items
        self.initialize_shelf()
    
    def initialize_shelf(self):
        code = 101
        for i in range(len(self.shelfs)):
            self.shelfs[i] = ItemShelf(code)
            code+=1
    
    def add_item(self,item,code):
        
        for shelf in self.shelfs:
            if shelf.code!=code:
                continue
            else:
                if shelf.soldOut:
                    shelf.soldOut = False
                    shelf.item = item
                    return 
                else:
                    raise Exception("Already item is present, you cannot add item here")
        raise Exception("Invalid Code")
                
    def get_item(self, code):
        for shelf in self.shelfs:
            if shelf.code!=code:
                continue
            else:
                if shelf.soldOut:
                    Exception("Item already sold out")
                else:
                    return shelf.item
                
        raise Exception("Invalid Code") 
    
    def mark_sold_out(self, code):
        for shelf in self.shelfs:
            if shelf.code!=code:
                continue
            else:
                if shelf.soldOut:
                    raise Exception("Item already sold out")
                else:
                    shelf.soldOut = True
                    shelf.item = None
                    return 
        raise Exception("Invalid Code") 
        


class VendingMachine:
    def __init__(self, count):
        self.vending_machine_state = IdleState(self)
        self.inventory = Inventory(count)
        self.coin_list = []

    def add_coin(self, coin):
        self.coin_list.append(coin)

    def refund_all(self):
        total = sum(coin.value for coin in self.coin_list)
        self.coin_list = []
        return total
    
    def total_money(self):
        return sum(coin.value for coin in self.coin_list)

class State(ABC):
    @abstractmethod
    def click_on_insert_coin_button(self):pass
    @abstractmethod
    def insert_coin(self, coin:int):pass
    @abstractmethod
    def click_on_start_product_selection_button(self):pass
    @abstractmethod
    def choose_product(self, code:int):pass
    @abstractmethod
    def get_change(self, return_money:int):pass
    @abstractmethod
    def dispense_product(self, code:int):pass
    @abstractmethod
    def refund_full_money(self):pass
    @abstractmethod
    def add_to_inventory(self, item:Item, code:int):pass


class IdleState(State):

    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine

    def click_on_insert_coin_button(self):
        self.machine.vending_machine_state = HasMoneyState(self.machine)

    def insert_coin(self, coin: int):
        raise NotImplementedError

    def click_on_start_product_selection_button(self):
        raise NotImplementedError

    def choose_product(self, code: int):
        raise NotImplementedError

    def get_change(self, return_money: int):
        raise NotImplementedError

    def dispense_product(self, code: int):
        raise NotImplementedError

    def refund_full_money(self):
        raise NotImplementedError

    def add_to_inventory(self, item: Item, code: int):
        self.machine.add_to_inventory(item, code)

class HasMoneyState(State):

    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine
        

    def click_on_insert_coin_button(self):
        return 

    def insert_coin(self, coin: int):
        self.machine.add_coin(coin)
        print("coin added")

    def click_on_start_product_selection_button(self):
        self.machine.vending_machine_state = Selection(self.machine)

    def choose_product(self, code: int):
        raise NotImplementedError

    def get_change(self, return_money: int):
        raise NotImplementedError

    def dispense_product(self, code: int):
        raise NotImplementedError

    def refund_full_money(self):
        print("Returned the full amount back in the Coin Dispense Tray")
        self.machine.vending_machine_state = IdleState(self.machine)
        return self.machine.refund_all()

    def add_to_inventory(self, item: Item, code: int):
        raise NotImplementedError

class Selection(State):

    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine

    def click_on_insert_coin_button(self):
        raise NotImplementedError

    def insert_coin(self, coin: int):
        raise NotImplementedError

    def click_on_start_product_selection_button(self):
        return 
    
    def choose_product(self, code: int):
        item = self.machine.inventory.get_item(code)
        if item.price>self.machine.total_money():
            self.refund_full_money()
            raise Exception("Insufficient Balance")
        else:
            change = self.machine.total_money() - item.price
            if change>0:
                self.get_change(change)
                DispenseState(self.machine, code)
                # self.machine.vending_machine_state = DispenseState(self.machine, code)


    def get_change(self, return_extra_money: int):
        print(f"Returned the change in the Coin Dispense Tray: {return_extra_money}")
        return return_extra_money

    def dispense_product(self, code: int):
        raise NotImplementedError

    def refund_full_money(self):
        print("Returned the full amount back in the Coin Dispense Tray")
        self.machine.vending_machine_state = IdleState(self.machine)
        return self.machine.refund_all()

    def add_to_inventory(self, item: Item, code: int):
        raise NotImplementedError

class DispenseState(State):

    def __init__(self, machine:VendingMachine, code) -> None:
        self.machine = machine
        self.dispense_product(code)

    def click_on_insert_coin_button(self):
        raise NotImplementedError

    def insert_coin(self, coin: int):
        raise NotImplementedError

    def click_on_start_product_selection_button(self):
        raise NotImplementedError

    def choose_product(self, code: int):
        raise NotImplementedError

    def get_change(self, return_money: int):
        raise NotImplementedError

    def dispense_product(self, code: int):
        item = self.machine.inventory.get_item(code)
        self.machine.inventory.mark_sold_out(code)
        self.machine.vending_machine_state = IdleState(self.machine)
        print("Product has been dispensed")
        return item

    def refund_full_money(self):
        raise NotImplementedError

    def add_to_inventory(self, item: Item, code: int):
        raise NotImplementedError

class VendingMachineManager:
    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine
        
    def add_item(self,item, code):
        self.machine.inventory.add_item(item, code)
    
    def display_all_items(self):
        # print(self.machine.inventory.shelfs)
        for shelf in self.machine.inventory.shelfs:
            if shelf.item:
                print(shelf.code, shelf.item.type.name, shelf.item.price, "available ",not shelf.soldOut)
    
if __name__=="__main__":
    try:
        machine = VendingMachine(10)
        manager = VendingMachineManager(machine)

        # add items
        manager.add_item(Item(ItemType.COKE, 12), 101)
        manager.add_item(Item(ItemType.COKE, 12), 102)
        manager.add_item(Item(ItemType.COKE, 12), 103)
        manager.add_item(Item(ItemType.COKE, 12), 104)
        manager.add_item(Item(ItemType.PEPSI, 9), 105)
        # manager.add_item(Item(ItemType.PEPSI, 9), 105)
        manager.add_item(Item(ItemType.JUICE, 13), 106)
        manager.add_item(Item(ItemType.JUICE, 13), 107)
        manager.add_item(Item(ItemType.SODA, 19), 108)
        manager.add_item(Item(ItemType.SODA, 19), 109)
        manager.add_item(Item(ItemType.SODA, 19), 110)

        manager.display_all_items()
        machine.vending_machine_state.click_on_insert_coin_button()
        machine.vending_machine_state.insert_coin(Coin.NICKEL)
        machine.vending_machine_state.insert_coin(Coin.QUARTER)

        machine.vending_machine_state.click_on_start_product_selection_button()
        machine.vending_machine_state.choose_product(102)
        manager.display_all_items()

        machine.vending_machine_state.click_on_insert_coin_button()
        machine.vending_machine_state.insert_coin(Coin.QUARTER)

        machine.vending_machine_state.click_on_start_product_selection_button()
        machine.vending_machine_state.choose_product(109)
        # machine.vending_machine_state.refund_full_money()
        manager.display_all_items()

        

        
    except Exception as e:
        print(e)
        print(traceback.format_exc())


"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

class ItemType(Enum):
    PEPSI = 1
    COKE = 2
    JUICE = 3
    SODA = 4

class Item:
    def __init__(self, price:int=-1, type:ItemType=None) -> None:
        self.price:int = price
        self.type:ItemType = type

class ItemShelf:
    def __init__(self, item:Item=None, isSoldOut:bool=True, code:int=-1) -> None:
        self.item:Item = item
        self.isSoldOut:bool = isSoldOut
        self.code:int = code

class Inventory:
    def __init__(self, item_shelf_count:int) -> None:
        self.item_shelf_count:int = item_shelf_count
        self.initialise_inventory()
    
    def initialise_inventory(self) -> None:
        # self.shelfs = []
        self.shelfs: List[ItemShelf] = []
        code = 101
        for _ in range(self.item_shelf_count):
            self.shelfs.append(ItemShelf(code=code))
            code+=1
        
    def add_item(self,item:Item, code:int) -> None:
        for shelf in self.shelfs:
            if shelf.code==code:
                if shelf.isSoldOut:
                    shelf.item = item
                    shelf.isSoldOut = False
                    return
                else:
                    raise Exception("Item already present")
        raise Exception("Invalid code")
    
    def get_item(self, code) -> Item:
        for shelf in self.shelfs:
            if shelf.code==code:
                if not shelf.isSoldOut:
                    return shelf.item
                else:
                    raise Exception("Item already sold out")
        raise Exception("Invalid code")

    def mark_sold_out(self, code):
        for shelf in self.shelfs:
            if shelf.code==code:
                if shelf.isSoldOut:
                    raise Exception("Already sold out")
                else:
                    shelf.isSoldOut = True
                    shelf.item = None
                    return
        raise Exception("Invalid Code")

class VendingMachine:
    def __init__(self, shelf_count) -> None:
        self.inventory = Inventory(shelf_count)
        self.coins = []
        self.current_state = IdleState(self)





class State(ABC):
    @abstractmethod
    def press_to_insert_coin(self):
        pass
    @abstractmethod
    def insert_coin(self, coin:Coin):
        pass
    @abstractmethod
    def press_to_choose_product(self):
        pass
    @abstractmethod
    def choose_product(self, code):
        pass
    @abstractmethod
    def get_change(self, extra_money)->int:
        pass
    @abstractmethod
    def refund_money(self) -> List[Coin]:
        pass
    @abstractmethod
    def dispense_product(self, code)->Item:
        pass
    @abstractmethod
    def add_item(self, item, code):
        pass

        
class IdleState(State):
    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine

    def press_to_insert_coin(self):
        self.machine.current_state = HasMoneyState(self.machine)

    def insert_coin(self, coin: Coin):
        raise NotImplementedError

    def press_to_choose_product(self):
        raise NotImplementedError

    def choose_product(self, code):
        raise NotImplementedError

    def get_change(self, extra_money) -> int:
        raise NotImplementedError

    def refund_money(self) -> List[Coin]:
        raise NotImplementedError

    def dispense_product(self, code) -> Item:
        raise NotImplementedError

    def add_item(self, item, code):
        self.machine.inventory.add_item(item,code)


class HasMoneyState(State):
    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine

    def press_to_insert_coin(self):
        return

    def insert_coin(self, coin: Coin):
        self.machine.coins.append(coin)

    def press_to_choose_product(self):
        self.machine.current_state = SelectionState(self.machine)

    def choose_product(self, code):
        raise NotImplementedError

    def get_change(self, extra_money) -> int:
        raise NotImplementedError

    def refund_money(self) -> List[Coin]:
        coins = self.machine.coins
        self.machine.coins = []
        self.machine.current_state = IdleState(self.machine)
        return coins

    def dispense_product(self, code) -> Item:
        raise NotImplementedError

    def add_item(self, item, code):
        raise NotImplementedError


class SelectionState(State):
    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine

    def press_to_insert_coin(self):
        raise NotImplementedError

    def insert_coin(self, coin: Coin):
        raise NotImplementedError

    def press_to_choose_product(self):
        return

    def choose_product(self, code):
        item = self.machine.inventory.get_item(code)
        total_amount = sum(coin.value for coin in self.machine.coins)
        # print(total_amount, item.price)
        if item.price>total_amount:
            # return self.refund_money()
            self.refund_money()
        else:
            extra_money = total_amount-item.price
            self.get_change(extra_money)
            # self.machine.current_state
            DispensingState(self.machine, code)


    def get_change(self, extra_money) -> int:
        print("TAke your money from tray ", extra_money)
        return extra_money
    
    def refund_money(self) -> List[Coin]:
        coins = self.machine.coins
        self.machine.coins = []
        self.machine.current_state = IdleState(self.machine)
        print(coins)
        # return coins

    def dispense_product(self, code) -> Item:
        raise NotImplementedError

    def add_item(self, item, code):
        raise NotImplementedError


class DispensingState(State):
    def __init__(self, machine:VendingMachine, code) -> None:
        self.machine = machine
        self.dispense_product(code)

    def press_to_insert_coin(self):
        raise NotImplementedError

    def insert_coin(self, coin: Coin):
        raise NotImplementedError

    def press_to_choose_product(self):
        raise NotImplementedError

    def choose_product(self, code):
        raise NotImplementedError

    def get_change(self, extra_money) -> int:
        raise NotImplementedError

    def refund_money(self) -> List[Coin]:
        raise NotImplementedError

    def dispense_product(self, code) -> Item:
        item = self.machine.inventory.get_item(code)
        self.machine.inventory.mark_sold_out(code)
        self.machine.current_state = IdleState(self.machine)
        print("product dispensed")
        return item

    def add_item(self, item, code):
        raise NotImplementedError

class VendingMachineManager:
    def __init__(self, machine:VendingMachine) -> None:
        self.machine = machine
    
    def add_item(self,item, code):
        self.machine.inventory.add_item(item, code)
    
    def display_all_items(self):
        for shelf in self.machine.inventory.shelfs:
            if shelf.item:
                print(shelf.code, shelf.item.type.name, shelf.item.price, "isAvailable? : ",not shelf.isSoldOut)
            else:
                print(shelf.code, "isAvailable? :         ", not shelf.isSoldOut)


if __name__=="__main__":
    machine = VendingMachine(10)
    manager = VendingMachineManager(machine)
    # manager.add_item(Item(12, ItemType.COKE), 101)
    # manager.add_item(Item(12, ItemType.COKE), 102)
    # manager.add_item(Item(12, ItemType.COKE), 103)
    # manager.add_item(Item(12, ItemType.COKE), 104)
    # manager.add_item(Item(12, ItemType.COKE), 105)
    # manager.add_item(Item(12, ItemType.COKE), 106)
    # manager.add_item(Item(12, ItemType.COKE), 107)
    # manager.add_item(Item(12, ItemType.COKE), 108)
    # manager.add_item(Item(12, ItemType.COKE), 109)
    # manager.add_item(Item(12, ItemType.COKE), 110)

    # machine.current_state.press_to_insert_coin()
    # machine.current_state.insert_coin(Coin.DIME)
    # # machine.current_state.insert_coin(Coin.DIME)
    # machine.current_state.insert_coin(Coin.PENNY)
    # machine.current_state.insert_coin(Coin.PENNY)
    # machine.current_state.insert_coin(Coin.PENNY)
    # # print("-"*20,machine.current_state)

    # machine.current_state.press_to_choose_product()
    # # machine.current_state.refund_money()


    # machine.current_state.choose_product(101)

    # manager.display_all_items()
    manager.add_item(Item(type=ItemType.COKE, price = 12), 101)
    manager.add_item(Item(type=ItemType.COKE, price = 12), 102)
    manager.add_item(Item(type=ItemType.COKE, price = 12), 103)
    manager.add_item(Item(type=ItemType.COKE, price = 12), 104)
    manager.add_item(Item(type=ItemType.PEPSI,price =  9), 105)
    # manager.add_item(Item(ItemType.PEPSI, 9), 105)
    manager.add_item(Item(type=ItemType.JUICE,price =  13), 106)
    manager.add_item(Item(type=ItemType.JUICE,price =  13), 107)
    manager.add_item(Item(type=ItemType.SODA, price = 19), 108)
    manager.add_item(Item(type=ItemType.SODA, price = 19), 109)
    manager.add_item(Item(type=ItemType.SODA, price = 19), 110)

    manager.display_all_items()

    machine.current_state.press_to_insert_coin()
    machine.current_state.insert_coin(Coin.NICKEL)
    machine.current_state.insert_coin(Coin.QUARTER)

    machine.current_state.press_to_choose_product()
    machine.current_state.choose_product(102)

    manager.display_all_items()



        

"""