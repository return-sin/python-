class Animals():
    def __init__(self,species) -> None:
        self.species = species

class Dog(Animals):
    def __init__(self, species, name) -> None:
        super().__init__(species)
        self.name = name
sam = Dog("dog","sam")
print(sam.name)