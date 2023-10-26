class Fighter(object):

    print(object)
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile


    def attack(self):
        print(self.model + "출격!")


    def fire(self):
        print(self.missile + "발사!")


fighter = Fighter("F-22","공대공미사일")
fighter.attack()
fighter.fire()