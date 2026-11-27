class Guest:
    def __init__(self, name, tickets):
        self.name = name
        self.__tickets = tickets

    def get_tickets(self):
        return self.__tickets

    def add_tickets(self, n):
        if n > 0:
            self.__tickets += n
        else:
            print("Invalid amount.")

    def __str__(self):
        return self.name + ": " + str(self.__tickets) + " tickets"

maya = Guest("Maya",8)
print(maya)
maya.add_tickets(-2)
print(maya.get_tickets())
maya.add_tickets(3)
print(maya)
