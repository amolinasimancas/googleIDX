class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = float(price)
        self.isAvaliable = True
    
    def turn_unavaliable(self):
        if self.isAvaliable:
            self.isAvaliable = False
            print(f"{self.brand} {self.model} successfully sold")
        else:
            print(f"{self.brand} {self.model} not avaliable for selling")
    
    def turn_avaliable(self):
        self.isAvaliable = True
        print(f"{self.brand} {self.model} avaliable for selling")

class User:
    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = float(balance)
        self.user_cars = []
    
    def buy_car(self, car):
        if car.isAvaliable and self.balance >= car.price:
            car.turn_unavaliable()
            self.user_cars.append(car)
            self.balance -= car.price
            print(f"{self.name} successfully bought {car.brand} {car.model} for {car.price} and remaining balance is ${self.balance}")
        elif car.isAvaliable == False:
            print(f"{car.brand} {car.model} is not avaliable")
        elif self.balance < car.price:
            print("You don´t have enough credits to buy this car")
    
    def sell_car(self, car):
        if car in self.user_cars:
            car.turn_avaliable()
            self.user_cars.remove(car)
            self.balance += car.price
            print(f"You´ve successfully sold the {car.brand} {car.model} and your current balance is ${self.balance}")
        else:
            print("You don´t have that car in the garage!")

class Dealership:
    def __init__(self, subsidiary):
        self.subsidiary = subsidiary
        self.cars = []
        self.users = []

    def register_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} successfully registered")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"{user.name} successfully registered with the id #{user.id}")

    def show_avaliable_cars(self):
        print("Welcome, avaliable units at this dealership:")
        for car in self.cars:
            if car.isAvaliable:
                print(f"{car.brand} {car.model} ${car.price}")

# Create cars
car1 = Car("Chevrolet","Onix","10000")
car2 = Car("Chevrolet","S20","30000")
car3 = Car("Ford","Ranger","35000")
car4 = Car("Toyota","Corolla","20000")
car5 = Car("Fiat","Cronos","15000")

# Create users
user1 = User("Antonio","001","30000")
user2 = User("Liliana","002","40000")

# Create dealerships
dealer1 = Dealership("Norte")

# Add cars and users to dealerships
dealer1.register_car(car1)
dealer1.register_car(car2)
dealer1.register_car(car3)
dealer1.register_car(car4)
dealer1.register_car(car5)

dealer1.register_user(user1)
dealer1.register_user(user2)

dealer1.show_avaliable_cars()

# Buy cars
user1.buy_car(car3)
user1.buy_car(car4)
user2.buy_car(car2)
user2.buy_car(car1)
dealer1.show_avaliable_cars()

# Sell cars
user2.sell_car(car2)
dealer1.show_avaliable_cars()