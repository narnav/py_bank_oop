import json
from Client import VIP, Client
from Enums import clientActions


CLIENTS_FILE="Clients.json"

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
        userSelection=self.menu(clientActions)
        if userSelection == clientActions.DEPOSIT.value: self.bankClients[selected_user].deposit(int(input("amount 2 deposit")))
        if userSelection == clientActions.WITDRAW.value:print( self.bankClients[selected_user].withdraw(int(input("amount 2 withdraw"))))
    # display menu bank/client
    
    def menu(self,actions):
        for act in actions:
            print(f'{act.value} - {act.name}')
        return int( input("your selection"))