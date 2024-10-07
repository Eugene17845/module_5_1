class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors :
            print('Такого этажа не существует')
        else:
            for a in range(1, new_floor + 1):
                print(a)


h1 = House('ЖК Горский', 18)
h2 = House('Бабкина Гора', 3)
h1.go_to(15)
h2.go_to(4)

