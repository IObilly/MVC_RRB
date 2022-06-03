from uuid import uuid4
from datetime import datetime


class Bike:
    def __init__(self, type_, manufacturer, year):
        self.type_ = type_
        self.manufacturer = manufacturer
        self.year = year
        self.status = "AVAILABLE"

    def __str__(self):
        return f"{self.manufacturer.capitalize()} Bike of type '{self.type_}' with {self.year} years of using "

    def __repr__(self):
        return f"Bike{self.type_, self.manufacturer, self.year}"


class Bill:
    def __init__(self, client, partner, payment_method):
        self.client = client
        self.payment_method = payment_method
        self.partner = partner
        self.date = datetime
        self.total = 0
        self.status = "PENDING"


class User:
    def __init__(self, username, email):
        self.id = uuid4()
        self.username = username
        self.email = email
        self.secret_key = str(self.id)[0: 5]

    def __repr__(self):
        return f"User{self.username, self.email}"


class Client(User):
    def __init__(self, username, email, address):
        super().__init__(username, email)
        self.address = address
        self.rented_bike = None

    def __repr__(self):
        return f"Client{self.username, self.email, self.address}"


class Partner(User):
    def __init__(self, username, email, bike):
        super().__init__(username, email)
        self.bike = bike
        self.balance = 0
        self.payed = False

    def __repr__(self):
        return f"Partner{self.username, self.email, self.bike}"
