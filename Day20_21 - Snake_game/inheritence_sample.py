class Animal():

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):

    def __init__(self):
        # The call to super() in the initializer is recommended, but not strictly required.
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")

    def swim(self):
        print("Swimming underwater")


nemo = Fish()
print(f"Nemo has {nemo.num_eyes} eyes")
nemo.breathe()
