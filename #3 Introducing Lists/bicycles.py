# Introducing Lists

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Accessing Elements in a List
print(bicycles[-1].upper())
print(bicycles[1])
print(bicycles[3])

# Using Individual Values from a List

bicycles = ["trek", "cannondale", "redline", "specialized"]
message = f"My first bicycle was a {bicycles[1].upper()}."
text = f"{bicycles[2].title()} was my first bicycle. "
print(message)
print(text)

# Try It Yourself

friends = ["William", "Gyan", "Rebecca", "Ama", "Pamela", "Ascona"]
print(friends[1])
print(friends[1], friends[3])
