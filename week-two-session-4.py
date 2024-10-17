class Wolverine:
    def __init__(self, armLength, legLength, numberOfEyes, tail, fur):
        self.armLength = armLength
        self.legLength = legLength
        self.numberOfEyes = numberOfEyes
        self.tail = tail
        self.fur = fur
    def displayInfo(self):
        print(self.armLength,"in")
        print(self.legLength,"in")
        print("Number of Eyes", self.numberOfEyes)
        print("Has Tail", self.tail)
        print("Has Fur", self.fur)

test = Wolverine(4.8, 4.9, 2, True, True)

test.displayInfo()