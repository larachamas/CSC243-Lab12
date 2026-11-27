class Hall:
    def __init__(self, name, seats):
        self.name = name
        self.__seats = seats

    def get_seats(self):
        return self.__seats

    def __has_seats(self):
        if self.__seats > 0:
            return True
        else:
            return False

    def has_seats(self):
        return self.__has_seats()

    def set_seats(self, n):
        if 0 <= n <= 100:
            self.__seats = n
        else:
            print("Invalid seats.")

    def __str__(self):
        return "Hall " + self.name + ": " + str(self.__seats) + " seats"

hall = Hall("A",40)
print(hall)
hall.set_seats(-5)
print(hall.get_seats())
hall.set_seats(150)
print(hall.get_seats())
hall.set_seats(0)
print(hall)