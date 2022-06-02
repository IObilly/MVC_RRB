import sys
import time

from contoller import UserController, RentController, ClientController, PartnerController, BikeController, \
    BillController
from db import users


class RegisterView:
    def __init__(self):
        self.users = users
        self.controller = UserController()

    def main_menu(self):
        username = input("Entre your desired username: ")
        for user in self.users:
            while username == getattr(user, 'username'):
                username = input("{username} is already taken, please choose another one")
        email = input("Set a Password: ")
        self.controller.add_user(username, email)
        user = self.controller.get_user(username)
        print(f"//{self.controller.get_secret_key(user)}// This is your Secret Key, please keep it where you can "
              f"remember it and DO NOT share it with anyone")
        ClientView().main_menu()


class LoginView:
    def __init__(self):
        self.users = users
        self.controller = UserController()

    def login(self):
        username = input("Entre your username: ")
        email = input("Enter your email address: ")
        c = 0
        while c < 4:
            if self.controller.get_user(username) is not None and (self.controller.get_user(username)).email == email:
                print(f"Welcome Back {username}")
                ClientView()

                break
            else:
                print("Couldn't login, username or email is wrong")
                c += 1
        else:
            raise Exception("Too many Failed attempts to login, try again after 25 minutes")


class SectionView:
    def __init__(self):
        self.interface = None

    def directing(self):
        print("Welcome To RBB")
        print("1~ Login\n"
              "2~ Signup for Free")
        choice = int(input(">>"))
        if choice == 1:
            LoginView().login()
        elif choice == 2:
            RegisterView().main_menu()
        else:
            raise Exception("Invalid choice")


class ClientView:
    def __init__(self):
        self.user_controller = UserController()

        self.rent_controller = RentController(ClientController(), PartnerController(),
                                              BikeController(), BillController())

    def main_menu(self):
        print("1~Rent a Bike\n"
              "2~Return a Bike\n"
              "3~Delete your account\n"
              "4~Pay a Bill\n"
              "0~Logout")
        choice = int(input(">>> "))
        if choice == 1:
            for i in range(len(self.rent_controller.bike_list())):
                print(f"{i} > {self.rent_controller.bike_list()[i]}")
            bike_choice = int(input("Pick your Desired Bike"))
            while bike_choice not in range(len(self.rent_controller.bike_list())):
                bike_choice = int(input("invalid Choice , please try again!.."))
            chosen_bike = self.rent_controller.bike_list()[bike_choice]
            self.rent_controller.rent(chosen_bike)
        elif choice == 2:
            self.rent_controller.return_bike()
        elif choice == 3:
            username = input("please enter your username")
            key = input("please enter your secret_key")
            if (self.user_controller.get_user(username)).username == username and (
                    self.user_controller.get_user(username)).secret_key == key:
                self.user_controller.remove_user(self.user_controller.get_user(username))
                print("Your account has been removed. You was a good Customer")
        elif choice == 4:
            key = input("please enter your secret key: ")
            self.rent_controller.pay_your_bill(self.user_controller.get_user_by_secret_key(key))
        elif choice == 0:
            print("See YOU Soon ^_^")
            time.sleep(3)
            sys.exit()
