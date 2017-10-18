class Pin:
    OUT = 1

    def __init__(self, pin_number, mode):
        self.pin_number= pin_number
        self.mode = mode
        self.state = False

    def value(self, new=None):
        if new is not None:
            self.state = new
            print("LED is now:", new)
        return self.state

