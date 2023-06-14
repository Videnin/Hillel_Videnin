class AttributePrinterMixin:
    def __str__(self):
        class_name = self.__class__.__name__
        properties = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        return f"{class_name}: {properties}"

    def __repr__(self):
        return self.__str__()

class A(AttributePrinterMixin):
    def __init__(self):
        self.public_field = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

a = A()
print(a)
