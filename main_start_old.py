from enum import Enum
import json

CLIENTS_FILE="Clients.json"

class BankActions(Enum):
    ADD_REGULAR =1
    ADD_VIP =2
    DELETE =3
    PRINT =4
    SEARCH =5
    CLIENT_ACTIONS =6
    EXIT=7

class clientActions(Enum):
    DEPOSIT =1
    WITDRAW =2
    GET_BALANCE =3
    GO_BACK= 4

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

class Bank:
    bankClients=[]
    bankName=""
    def __init__(self,name) :
        self.bankName=name

    def print_all_clients(self):
        for client in self.bankClients:
            print(client)
    
    def save_all_clients(self):
        arr_to_save=[]
        for client in self.bankClients:
            arr_to_save.append( client.json_str())
        
        with open(CLIENTS_FILE, "w") as f:
            json.dump(arr_to_save, f,indent=4)

    def load_all_clients(self):
        arr_clients=[]
                
        with open(CLIENTS_FILE, 'r') as data_file:
            arr_clients = json.load(data_file)
            
            for client in arr_clients:
                if client["type"] =="VIP":
                    self.bankClients.append(VIP(client["name"],len(self.bankClients),client["balance"]))
                else:
                    self.bankClients.append(Client(client["name"],len(self.bankClients),client["balance"]))
    
    def client_actions(self):
        print("my clients:")
        self.print_all_clients()
        
        selected_user=int(input("which client to abuse?"))
        print(f'u select:{self.bankClients[selected_user]} your balance is :-( {self.bankClients[selected_user].getBalance()}, this is bank {self.bankName} ' )
        userSelection=menu(clientActions)
        if userSelection == clientActions.DEPOSIT.value: self.bankClients[selected_user].deposit(int(input("amount 2 deposit")))
        if userSelection == clientActions.WITDRAW.value:print( self.bankClients[selected_user].withdraw(int(input("amount 2 withdraw"))))

# display menu bank/client
def menu(actions):
        for act in actions:
            print(f'{act.value} - {act.name}')
        return int( input("your selection"))

# def client_actions(bnk):
#         print("my clients:")
#         bnk.print_all_clients()
        
#         selected_user=int(input("which client to abuse?"))
#         print(f'u select:{bnk.bankClients[selected_user]} your balance is :-( {bnk.bankClients[selected_user].getBalance()}, this is bank {bnk.bankName} ' )
#         userSelection=menu(clientActions)
#         if userSelection == clientActions.DEPOSIT.value: bnk.bankClients[selected_user].deposit(int(input("amount 2 deposit")))
#         if userSelection == clientActions.WITDRAW.value: bnk.bankClients[selected_user].withdraw(int(input("amount 2 withdraw")))

def main():
    bnk=Bank("ganavim")
    bnk.load_all_clients()
    userSelection= menu(BankActions)
    while userSelection != BankActions.EXIT.value:
        if userSelection == BankActions.ADD_REGULAR.value:bnk.bankClients.append( Client(input("name?"),len(bnk.bankClients)))
        if userSelection == BankActions.ADD_VIP.value:bnk.bankClients.append( VIP(input("name?"),len(bnk.bankClients)))
        if userSelection == BankActions.PRINT.value: bnk.print_all_clients()
        if userSelection == BankActions.CLIENT_ACTIONS.value:
            bnk.client_actions()
            
        userSelection= menu(BankActions)
    bnk.save_all_clients()
if __name__ == "__main__":
    main()