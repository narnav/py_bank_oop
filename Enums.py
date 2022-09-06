from enum import Enum
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