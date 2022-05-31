# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad


def print_union(value: int | float | dict[str, int]):
    value_type = {
        int: "Integer",
        float: "Float",
        dict: "Dictionary of String and Int",
    }[type(value)]
    print(f"Your value is of type {value_type}, = {value}")


print_union(10)
print_union(1.2)
print_union({"Hello": 10})
print_union("Hello") # Invalid
