# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad

string = "Foo Bar Baz Qux"
# Foo (from index 0, to 3rd char)
print(string[:3])
# Foo (explicitly specify index 0)
print(string[0:3])
# Bar (from index 4, up to and including index 7)
print(string[4:7])
# Bar (from end go 11 steps back, and end at 8 steps back)
print(string[-11:-8])
# Baz (from beginning at index 8, until and including index 11)
print(string[8:11])
# Baz (7 items back from the end until 4 items back from the end)
print(string[-7:-4])
# Qux (from index 12 up to and including index 15)
print(string[12:15])
# Qux (3 items back from end and continue to the end (no end index))
print(string[-3:])
# FBBQ (from start to the end, and jump forward 4 steps every iteration)
print(string[::4])
# xuQ zaB raB ooF (from start to end, jump back one step, reversing)
print(string[::-1])
# zaB raB ooF (index 5 from end, continue to beginning in reverse)
print(string[-5::-1])
# Foo Bar Baz Qux (shallow copy the list)
print(string[:])
