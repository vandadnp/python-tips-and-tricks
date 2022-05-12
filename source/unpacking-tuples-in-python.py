# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad

names = ["foo", "bar", "baz", "qux"]
# skip all values except for the first one
foo, *_ = names
# skip first value, read the one after, and skip everything after
_, bar, *_ = names
# skip everything until second to last, and skip last
*_, baz, _ = names
# skip all except the last value
*_, qux = names
# skip first value, read all values in between, and skip last value
_, *bar_and_baz, _ = names
# read al values, except last 2
*foo_and_bar, _, _ = names
# skip first two values and read the rest
_, _, *baz_and_qux = names
