# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad


from math import pi


class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    @property
    def area(self):
        return pi * self.radius * self.radius


print(Circle(10.0).area)  # 314.15
print(Circle(2.0).area)  # 12.56
print(Circle(4.0).area)  # 50.26
