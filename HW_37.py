from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class representing a vehicle."""

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    @abstractmethod
    def start(self):
        """Abstract method to start the vehicle."""
        pass

    @abstractmethod
    def stop(self):
        """Abstract method to stop the vehicle."""
        pass


class Car(Vehicle):
    """Class representing a car."""

    def __init__(self, brand, color, num_doors):
        super().__init__(brand, color)
        self.num_doors = num_doors

    def start(self):
        return f"The {self.brand} car with {self.num_doors} doors has started."

    def stop(self):
        return f"The {self.brand} car with {self.num_doors} doors has stopped."


class Bicycle(Vehicle):
    """Class representing a bicycle."""

    def __init__(self, brand, color):
        super().__init__(brand, color)

    def start(self):
        return f"The {self.brand} bicycle has started."

    def stop(self):
        return f"The {self.brand} bicycle has stopped."


# Создаем экземпляры классов и демонстрируем работу системы

car = Car("Toyota", "Red", 4)
print(car.start())  # Выводит "The Toyota car with 4 doors has started."

bicycle = Bicycle("Giant", "Blue")
print(bicycle.stop())  # Выводит "The Giant bicycle has stopped."
