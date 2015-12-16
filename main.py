from shop import Shop, Customer, Transaction
import random

NB_SHOP = 10
NB_CLIENTS = 30
FRAUDULENT_SHOP_RATE = 0.1
FRAUDULENT_CLIENT_RATE = 0.1
AVERAGE_NUMBER_OF_TRANSACTION = 10


def generate_shops(nb_shop, fraudulent_shop_rate):
    listOfShops = []
    for shop_id in range(0,nb_shop):
        if (random.uniform(0.0, 1.0) < fraudulent_shop_rate):
            #Creation of a fraudulent shop
            listOfShops.append(Shop(True,shop_id))
        else:
            #Creation of a normal shop
            listOfShops.append(Shop(False,shop_id))
    return listOfShops

def generate_clients(nb_clients, fraudulent_client_rate):
    listOfClients = []
    for client_id in range(0,nb_clients):
        if (random.uniform(0.0, 1.0) < fraudulent_client_rate):
            #Creation of a fraudulent client
            listOfClients.append(Customer(True,client_id))
        else:
            #Creation of a normal client
            listOfClients.append(Customer(False,client_id))
    return listOfClients

def generate_transaction(listOfClients, listOfShops, numberOfTransaction):
    listOfTransaction = []
    for client in listOfClients:
        for i in range(0, numberOfTransaction):
            if client.isFraudulent():
                #Return a random fraudulent shop
                shop = random.choice([x for x in listOfShops if x.isFraudulent()])
            else:
                #Return a normal shop
                shop = random.choice([x for x in listOfShops if not(x.isFraudulent())])
            listOfTransaction.append(Transaction(client.isFraudulent(), int(str(client.getId())+str(i)), client, shop))
    return listOfTransaction

clients = generate_clients(NB_CLIENTS, FRAUDULENT_CLIENT_RATE)
shops = generate_shops(NB_SHOP, FRAUDULENT_SHOP_RATE)
transactions = generate_transaction(clients, shops, AVERAGE_NUMBER_OF_TRANSACTION)

for transaction in transactions:
    print transaction
