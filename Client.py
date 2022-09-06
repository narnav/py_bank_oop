class Client:
    id=""
    name=""
    balance=0

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -=  amount
            return f'you just took {amount} amount'
        return "we know where u live!!"
        

    def getBalance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount

    def __init__(self,name,id,balance=0) :
        self.name=name
        self.balance=balance
        self.id=id

    def json_str(self) :
        return {"id":self.id, "name":self.name,"balance":self.balance,"type":type(self).__name__}

    def __str__(self) -> str:
        return f'id:{self.id}, name:{self.name},balance:{self.balance}'

class VIP(Client):
    credit =1000

    def withdraw(self,amount):
        if amount < self.balance+self.credit:
            self.balance -=  amount
            return f'you just took {amount} amount'
        return f'we apologize .....'

    def __str__(self) -> str:
        return f'id:{self.id}, name:{self.name},balance:{self.balance} , your credit {self.credit}'
