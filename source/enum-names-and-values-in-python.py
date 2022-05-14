# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad


import enum


class AnimalType(enum.Enum):
    DOG = "Dog"
    CAT = "Cat"
    RABBIT = "Rabbit"


class Animal:
    def __init__(self, name: str, type: AnimalType):
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return f"""Animal, 
        name = {self.name}, 
        type value = {self.type.value},
        type name = {self.type.name}
        """


print(Animal("Fluffers", AnimalType.CAT))
print(Animal("Woofson", AnimalType.DOG))
print(Animal("Earton", AnimalType.RABBIT))
