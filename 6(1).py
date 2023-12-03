# Абстрактний клас транспортного засобу
class Vehicle:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def move(self):
        raise NotImplementedError()


# Клас людини
class Human(Vehicle):
    def __init__(self, speed):
        super().__init__(speed, 1)


# Класи спадкоємців
class Car(Vehicle):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)

    def move(self):
        print("Автомобіль рухається зі швидкістю", self.speed)


class Bus(Vehicle):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)

    def move(self):
        print("Автобус рухається зі швидкістю", self.speed)


class Train(Vehicle):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)

    def move(self):
        print("Поїзд рухається зі швидкістю", self.speed)


# Клас транспортної мережі
class TransportNetwork:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def move_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.move()


# Клас маршруту
class Route:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def calculate_optimal_route(self, vehicle_type):
        # ...


# Логіка посадки та висадки пасажирів
def board_passengers(vehicle, passengers):
    for passenger in passengers:
        vehicle.capacity -= 1
        print("Пасажир", passenger, "засідає в транспортний засіб", vehicle)


def disembark_passengers(vehicle, passengers):
    for passenger in passengers:
        vehicle.capacity += 1
        print("Пасажир", passenger, "виходить з транспортного засобу", vehicle)


# Приклад використання
network = TransportNetwork()
network.add_vehicle(Car(100, 2))
network.add_vehicle(Bus(50, 50))
network.add_vehicle(Train(100, 1000))

route = Route("Київ", "Львів")

# Розрахунок оптимального маршруту для автомобіля
optimal_route_for_car = route.calculate_optimal_route("Car")

# Переміщення транспортних засобів
network.move_all_vehicles()

# Посадка пасажирів
board_passengers(network.vehicles[0], [1, 2, 3])

# Висадка пасажирів
disembark_passengers(network.vehicles[1], [4, 5, 6])
