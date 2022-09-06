import json 
from Enums import BankActions,clientActions
from Client import Client,VIP
from Bank import Bank

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
    userSelection= bnk.menu(BankActions)
    while userSelection != BankActions.EXIT.value:
        if userSelection == BankActions.ADD_REGULAR.value:bnk.bankClients.append( Client(input("name?"),len(bnk.bankClients)))
        if userSelection == BankActions.ADD_VIP.value:bnk.bankClients.append( VIP(input("name?"),len(bnk.bankClients)))
        if userSelection == BankActions.PRINT.value: bnk.print_all_clients()
        if userSelection == BankActions.CLIENT_ACTIONS.value:
            bnk.client_actions()
            
        userSelection= bnk.menu(BankActions)
    bnk.save_all_clients()
if __name__ == "__main__":
    main()