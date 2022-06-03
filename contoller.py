from db import bikes, bills, rented_bikes, available_bikes, users
from model import Client, Partner, User, Bike


class RegisterController:
    def __init__(self):
        self.users = users

    def register(self, user):
        self.users.append(user)


class BillController:
    def __init__(self):
        self.bills = bills

    def get_bill_for_client(self, client):
        return next(bill for bill in self.bills if bill.client == client)

    def get_bill_for_partner(self, partner):
        return next(bill for bill in self.bills if bill.partner == partner)

    def pay_partner(self, partner):
        bill = self.get_bill_for_partner(partner)
        partner.balance += ((bill.total + 2) // 3)
        partner.payed = True

    def list_bills(self):
        return [bill for bill in self.bills]

    def pay_bill(self, client):
        bill = self.get_bill_for_client(client)
        print(bill.total)
        bill.status = "Closed"


class BikeController:
    def __init__(self):
        self.bikes = bikes
        self.available_bikes = available_bikes
        self.rented_bikes = rented_bikes

    def add_bike(self, bike):
        self.bikes.append(bike)

    def remove_bike(self, bike):
        self.bikes.remove(bike)

    def change_bike_status(self, bike_):
        bike_.status = "Unavailable"
        for bike in self.bikes:
            if bike == bike_:
                self.rented_bikes.append(bike)

    def get_bike(self, type_=None, manufacturer=None, year=None):
        return next(bike for bike in self.bikes if
                    bike.type_ == type_ or bike.manufacturer == manufacturer or bike.year == year)

    def get_available_bikes(self):
        for bike in self.bikes:
            if bike.status == "Available":
                self.available_bikes.append(bike)
        return self.available_bikes


class RentController:
    def __init__(self, client_controller, partner_controller, bike_controller, bill_controller):
        self.bill_controller = bill_controller
        self.available_bikes = available_bikes
        self.client_controller = client_controller
        self.partner_controller = partner_controller
        self.bike_controller = bike_controller
        self.rented_bikes = rented_bikes

    def rent(self, chosen_bike):
        client_key = input('please provide your Secret_key:')
        (self.client_controller.get_client(key=client_key)).rented_bike = chosen_bike
        chosen_bike.status = "Unavailable"
        self.rented_bikes.append(chosen_bike)

    def return_bike(self):
        client_key = input('please provide your Secret_')
        (self.client_controller.get_client(key=client_key)).rented_bike.status = "Available"
        self.available_bikes.append((self.client_controller.get_client(key=client_key)).rented_bike)
        self.rented_bikes.remove((self.client_controller.get_client(key=client_key)).rented_bike)
        (self.client_controller.get_client(key=client_key)).rented_bike = None

    def bike_list(self):
        return self.bike_controller.get_available_bikes()

    def bill_list(self):
        return self.bill_controller.list_bills()

    def pay_your_bill(self, client):
        self.bill_controller.pay_bill(client)


class UserController:
    def __init__(self):
        self.users = users

    def add_user(self, username, email):
        user = User(username, email)
        self.users.append(user)

    def remove_user(self, client):
        self.users.remove(client)

    def list_users(self):
        return self.users

    def get_user(self, username):
        return next(user for user in self.users if user.username == username)

    def get_secret_key(self, user_):
        return next(user.secret_key for user in self.users if user == user_)

    def get_user_by_secret_key(self, key):
        return next(user for user in self.users if user.secret_key == key)


class ClientController:
    def __init__(self):
        self.clients = users

    def add_client(self, username, email, address):
        self.clients.append(Client(username, email, address))

    def remove_client(self, client):
        self.clients.remove(client)

    def get_client(self, username=None, email=None, key=None):
        return next(client for client in self.clients if client.username == username or
                    client.email == email or str(client.id)[0:5] == key)

    def get_client_id(self):
        return next(client.id for client in self.clients if client == self)

    def display_clients(self):
        for client in self.clients:
            return client


class PartnerController:
    def __init__(self):
        self.partners = []

    def add_partner(self, username, email, bike):
        self.partners.append(Partner(username, email, bike))

    def remove_partner(self, username):
        self.partners.remove(self.get_partner_by_username(username))

    def get_partner_by_username(self, username):
        return next(partner for partner in self.partners if partner.username == username)

    def get_partner_by_email(self, email):
        return next(partner for partner in self.partners if partner.email == email)

    def get_partner_by_bikes(self, bike):
        next(partner for partner in self.partners if partner.bike == bike)

    def display_partners(self):
        for partner in self.partners:
            return partner
