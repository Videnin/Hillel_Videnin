class DeliveryContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_cost(self, distance):
        return self.strategy.calculate_cost(distance)


class DeliveryStrategy:
    def calculate_cost(self, distance):
        pass


class PostalStrategy(DeliveryStrategy):
    def calculate_cost(self, distance):
        # Расчет стоимости доставки почтой
        return distance * 5


class CourierStrategy(DeliveryStrategy):
    def calculate_cost(self, distance):
        # Расчет стоимости доставки курьерской службой
        return distance * 10


class PickupStrategy(DeliveryStrategy):
    def calculate_cost(self, distance):
        # Расчет стоимости самовывоза
        return 0



