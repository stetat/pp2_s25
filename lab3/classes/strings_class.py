class console:
    def __init__(self):
        pass

    def getstring(self):
        self.a = str(input("input string: "))

    def printstring(self):
        print((self.a).upper())

        

test = console()
test.getstring()
test.printstring()

