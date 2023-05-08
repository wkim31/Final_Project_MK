class Coffee:
    def _init_(self, initialspeed = 2):
        self.speed = initialspeed

    def use(self):
        self.speed = self.speed + 2
        print ("Coffee consumed. Speed increased to (self.speed)")

class Banana:
    def _init_(self, initialspeed = 2):
        self.speed = initialspeed

    def use(self):
        self.speed = self.speed - 2
        print ("Banana consumed. Speed decreased to (self.speed)")
