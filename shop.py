import random
import math
import datetime
import time

class Shop:

    def isFraudulent(self):
        return self.fraudulent

    #The random location is related to Paris area
    def __init__(self, fraudulent, Id):
        self.id = Id
        self.latitude = "48." + str(random.randint(835847, 897980))
        self.longitude = "2." + str(random.randint(257810, 393409))
        self.fraudulent = fraudulent

    def __str__(self):
        return "Shop %d at latitude %s, longitude %s fraudulent = %s" %(self.id, self.latitude, self.longitude, self.fraudulent)


class Customer:

    def getId(self):
        return self.id

    def isFraudulent(self):
        return self.fraudulent

    def __init__(self, fraudulent, Id):
        self.id = Id
        self.fraudulent = fraudulent

    def __str__(self):
        return "Customer %d, fraudulent : %s" %(self.id, self.fraudulent)

class Transaction:

    #Define a random amount for a Transaction which is not following Benford's law
    def amountNonBenford(self, maxi):
        return random.randint(0,maxi)

    #Define an amount following the Benford's law
    def amountBenford(self, maxi):
        multiplier = math.log(maxi)
        return int(math.exp(multiplier * random.random()))

    def __init__(self, fraudulent, Id, customer, shop):
        self.id = Id
        if fraudulent:
            self.amount = self.amountNonBenford(1000)
        else:
            self.amount = self.amountBenford(1000)
        self.customer = customer
        self.shop = shop
        self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return "Transaction %d, amount : %d | %s | Client = %s | Shop = %s" %(self.id, self.amount, self.timestamp, self.customer, self.shop)
