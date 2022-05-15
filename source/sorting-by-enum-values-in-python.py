# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad


from enum import Enum, auto


class ItemPrio(Enum):
    LOW = auto()
    MID = auto()
    HIGH = auto()


class TodoItem:
    def __init__(self, title: str, prio: ItemPrio):
        self.name = title
        self.prio = prio

    def __repr__(self):
        return f"Todo item, title = {self.name}, prio = {self.prio}"


items = [
    TodoItem("Wash closes", ItemPrio.MID),
    TodoItem("Water plants", ItemPrio.HIGH),
    TodoItem("Buy a pair of jeans", ItemPrio.LOW),
]

sorted = sorted(items, key=lambda item: item.prio.value, reverse=True)
