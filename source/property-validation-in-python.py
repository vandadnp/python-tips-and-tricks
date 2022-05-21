# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad


class PositiveInt:
    def __init__(self, value: int):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: int):
        if new_value >= 0:
            self._value = new_value
        else:
            raise ValueError("Value can only be a positive integer")

    def __str__(self) -> str:
        return f"Positive Integer, value = {self.value}"


positive = PositiveInt(10)
print(positive.value)

try:
    negative = PositiveInt(-1)
    print(negative.value)
except ValueError:
    print("Invalid positive value!")
