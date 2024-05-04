class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"



if __name__ == "__main__":
    car1 = Car("Mercedes", "Vito",2017)
    car2 = Car("BMW", "M5", 2019)

    print(car1.get_info())