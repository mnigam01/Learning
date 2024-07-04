from abc import ABC, abstractmethod
from collections import defaultdict
from enum import Enum
from typing import List


class User:
    def __init__(self, userId, name, email, mobileNo) -> None:
        self.userId = userId
        self.name = name
        self.email = email
        self.mobileNo = mobileNo
        self.loan = defaultdict(int)

class ExpenseType(Enum):
    EQUAL = 1
    EXACT = 2
    PERCENT = 3

class Group:
    def __init__(self, groupId, admin) -> None:
        self.groupId = groupId
        self.users:List[User] = []
        self.admin:User = admin

class Print(ABC):
    @abstractmethod
    def printConsole(message):pass

class PrintConsole(Print):
    def printConsole(self, message):
        print(message)


    
if __name__=="__main__":
    printer= PrintConsole()
    users:List[User] = []
    user1 = User(1, 'User1','user1', 111)
    user2 = User(2, 'User2','user2', 222)
    user3 = User(3, 'User3','user3', 333)
    user4 = User(4, 'User4','user4', 444)
    users.append(user1)
    users.append(user2)
    users.append(user3)
    users.append(user4)


    def showAll():
        if len(users)==0:
            raise Exception("No users in the system")
        for user in users:
            show(user)
            # if len(user.loan)==0:
            #     printer.printConsole("No balance")
            # else:
            #     for key, value in user.loan.items():
            #         print(f'{user.name} owes {key.name}: {value}')
    


    def show(user:User):
        if user not in users:
            raise Exception("no such user in system")
        if len(user.loan)==0:
            printer.printConsole("No balance")
        else:
            for key, value in user.loan.items():
                if value==0:continue
                print(f'{user.name} owes {key.name}: {value}')
    
    def createExpense(user:User, expenseType:ExpenseType, amount, userList:List, distribution:List=[]):
        if expenseType==ExpenseType.EQUAL:
            paymentNeed = round(amount/len(userList),2)
            for _user in userList:
                if _user==user:
                    continue
                else:
                    paymentAdd(user, _user, paymentNeed)
        elif expenseType==ExpenseType.EXACT:
            if sum(distribution)!=amount:
                raise Exception("Distribution doesn't add up")
            if len(userList)!=len(distribution):
                raise Exception("Invalid input")
            for _user, paymentNeed in zip(userList, distribution):
                if _user==user:continue
                paymentAdd(user, _user, paymentNeed)
        elif expenseType==ExpenseType.PERCENT:
            if sum(distribution)!=100:
                raise Exception("given distribution doesn't add up to 100")
            if len(userList)!=len(distribution):
                raise Exception("Invalid input")
            for _user, percent in zip(userList, distribution):
                if _user==user:continue
                paymentAdd(user, _user, round(percent*amount/100,2))
        else:
            raise NotImplemented
             

    def paymentAdd(lender:User, owe:User, amount):
        extra = lender.loan[owe]
        if amount>=extra:
            lender.loan[owe] = 0
            amount -= extra

        owe.loan[lender]+=amount
        

    
    showAll()
    show(user1)

    createExpense(user1, ExpenseType.EQUAL, 1000, [user1, user2, user3, user4])
    # show(user4)
    showAll()
    createExpense(user1, ExpenseType.EXACT, 1250, [user2, user3], [370,880])
    showAll()
    createExpense(user4, ExpenseType.PERCENT, 1200, [user1, user2, user3, user4], [40,20,20,20])
    showAll()


