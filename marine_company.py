"""
Docstring for marine_company
Classes:
1. MarineCompany
2. Ship (abstract class)
3. CargoShip
4. CruiseShip
5. Customer
6. Booking
"""

#Class Customer
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


#Class Booking
class Booking:
    def __init__(self, customer, ship, amount):
        self.customer = customer
        self.ship = ship
        self.amount = amount
        ship.add_booking(self)

#Class Ship (abstract)
from abc import ABC, abstractmethod

class Ship(ABC):
    def __init__(self, ship_id, route):
        self.ship_id = ship_id
        self.route = route
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def get_total_amount(self):
        return sum(b.amount for b in self.bookings)

    @abstractmethod
    def get_type(self):
        pass

#Class CruiseShip
class CruiseShip(Ship):
    def get_type(self):
        return "Cruise"


#Class CargoShip
class CargoShip(Ship):
    def get_type(self):
        return "Cargo"

#Class MarineCompany
class MarineCompany:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    # Question 1
    def total_amount_collected(self):
        return sum(ship.get_total_amount() for ship in self.ships)
    
    #Question 2
    def total_amount_per_ship(self):
        return [(ship.ship_id, ship.get_type(), ship.get_total_amount())
            for ship in self.ships]


#Question 3 : question specific logic stays outside the entity: SRP
#safety check if Cargo ship passed
def listCustomersForCruiseShip(cruise_ship):
    if not isinstance(cruise_ship, CruiseShip):
        raise TypeError("Customers can only be listed for Cruise Ships")
    return [b.customer for b in cruise_ship.bookings]


if __name__ == "__main__":
    company = MarineCompany("Blue Ocean Marine")

    cs1 = CruiseShip(1, "Mumbai → Goa")
    cg1 = CargoShip(2, "Chennai → Singapore")

    company.add_ship(cs1)
    company.add_ship(cg1)

    c1 = Customer(101, "Alice")
    c2 = Customer(102, "Bob")
    c3 = Customer(103, "Charlie")

    Booking(c1, cs1, 5000)
    Booking(c2, cs1, 7000)
    Booking(c3, cg1, 12000)

    print("Total amount collected:", company.total_amount_collected())

    print("\nAmount per ship:")
    for sid, stype, amt in company.total_amount_per_ship():
        print(stype, sid, amt)

    #customers can only exist for cruise ship
    print("\nCustomers for Cruise Ship:")
    for cust in listCustomersForCruiseShip(cs1):
        print(cust.name)
    