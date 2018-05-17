class Robot:

    robots = []
    population = 0

    # Bot creation
    def __init__(self, name):
        self.name = name
        print("Инициализация {0}".format(self.name))

        Robot.robots.append(self.name)
        Robot.population += 1
        print("Состав роботов: ", end=' ')
        for i in Robot.robots:
            print(i, end=', ')

    # Bot decommissioning
    def __del__(self):
        print("{0} Выполнил свою работу и будет заменен более новым роботом.".format(self.name))

        Robot.population -= 1
        Robot.robots.remove(self.name)

        if Robot.population == 0:
            print('Последний выполнил работу, роботы отсутствуют.')
        else:
            print("Осталось {0:d} работающих роботов.".format(Robot.population))

    # Bot greetings
    def sayHi(self):
        print("Приветствую тебя, {0}. Рад, что ты принялся за работу.".format(self.name))




    def howMany():
        print("За работой {0:d} роботов.".format(Robot.population))

    howMany = staticmethod(howMany)


Robot.__del__(Robot("R2-D2"))


r1 = Robot("R2-D2")
Robot.howMany()
r2 = Robot("Arny")
Robot.howMany()
r1.sayHi()
r2.sayHi()
Robot.howMany()

print("\nРоботы в процессе работы...\n")


f = True
while f:
    n = int(input("Скольким роботам следует прекратить работу?"))
    if n > Robot.population:
        print("За работой сейчас {0} роботов. Введите другое количество".format(Robot.howMany()))

    elif n == Robot.population:
        print("Все роботы остановят работу.")
        del r1
        del r2
        Robot.population = 0
        f = False

    elif Robot.population >= n > 0:
        pass




