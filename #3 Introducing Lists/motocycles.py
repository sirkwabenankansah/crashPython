# Modifying, Adding, and Removing Elements

# Modifying Elements in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[1])
print(motorcycles)

motorcycles[0] = 'ducati'  # modifying the first value in the List
print(motorcycles)

# Adding Elements to the List

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') # append or add to the end of the List
print(motorcycles)

motorcycles = []  # Use append method to build list dynamically

motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('suzuki')
motorcycles.append('yamaha')

print(motorcycles)


# Inserting Elements into a List

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ducati')
print(motorcycles)

# Removing Elements from a List using del statement

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
del motorcycles[3]
print(motorcycles)


# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)
print(f"The last motorcycle sold was {popped_motorcycle}.")
print(f"The last motorcycle sold was {popped_motorcycle.upper()}.")


# Popping Items from Any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
popped_motorcycle = motorcycles.pop(2)
print(popped_motorcycle)
print(motorcycles)
print(f"The last motorcycle sold was {popped_motorcycle}.")
print(f"The last motorcycle sold was {popped_motorcycle.upper()}.")


# Removing an item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('yamaha')
print(motorcycles)

# Use removed value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = "honda"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me. ")


Try It Yourself

guest_list = ['Asiedu', 'Ansah', 'Paul', 'William']
message = "You are invited to dinner on Saturday at 1800. "
print(message)
print(f"Hello {guest_list[0]}, {message}")
print(f"Hello {guest_list[1]}, {message}")
print(f"Hello {guest_list[2]}, {message}")


guest_list = ['Asiedu', 'Ansah', 'Paul', 'Willie']
message = "You are invited to dinner on Saturday at 1800. "
# absent_guest_list = ['Ansah']
print(guest_list.pop(1))
guest_list.append('Stewart')
print(guest_list)
guest_list.insert(0, 'Gyan')
guest_list.insert(2, 'Josh')
guest_list.append('Kwaku')
print(guest_list)

for guest in guest_list:
    print(f"Hello {guest}, {message}")


guest_list = ['Asiedu', 'Ansah', 'Paul', 'Willie', 'Benjamin']
message = "I'm sorry I wouldn't invite you for my dinner party on Saturday at 1800. "
# absent_guest_list = ['Ansah']
print(guest_list.pop())
print(guest_list.pop())
print(guest_list.pop())
print(guest_list)

for guest in guest_list:
    print(f"Hello {guest}, {message}")








