
class Transport:
    def __init__(self, speed=0):
        self.__speed = speed 

    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount

    def brake(self):
        raise NotImplementedError("brake() metodi qayta aniqlanishi kerak!")

    def get_speed(self):
        return self.__speed

    def _change_speed(self, amount):
        self.__speed += amount



class Car(Transport):
    def brake(self):
        if self.get_speed() >= 20:
            self._change_speed(-20)
            print("Car: Tezlik 20 km/h ga kamaytirildi.")
        else:
            self._change_speed(-self.get_speed())  
            print("Car: Mashina to‘xtadi.")



class Bicycle(Transport):
    def brake(self):
        if self.get_speed() >= 5:
            self._change_speed(-5)
            print("Bicycle: Tezlik 5 km/h ga kamaytirildi.")
        else:
            self._change_speed(-self.get_speed())
            print("Bicycle: To‘xtadi.")




vehicles = [
    Car(60),
    Bicycle(25),
    Car(15),
]

print("Boshlang‘ich tezliklar:")
for v in vehicles:
    print(v.get_speed(), "km/h")

print("\nBraking (hamma transportlar uchun polimorf):")
for v in vehicles:
    v.brake()
    print("Yangi tezlik:", v.get_speed())
    print("-" * 30)
