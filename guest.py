guest = ['Alex', 'Bob', 'Georg']
# print(f"Welcome to my home, {guest[0]}")
# print(f"Welcome to my home, {guest[1]}")
# print(f"Welcome to my home, {guest[2]}")

print(f"{guest[1]}, don`t want")

guest[1] = 'Peter'
# print(f"Welcome to my home, {guest[0]}")
# print(f"Welcome to my home, {guest[1]}")
# print(f"Welcome to my home, {guest[2]}")

print("Будет больше гостей")
guest.insert(0, 'Kitty')
guest.insert(2,'Max')
guest.append('Iwan')

print(guest)

print(len(guest))
for x in guest:
    print(f"Welcome to my home, {x}")

print("Стол не прибудет во время, место есть для двоих")

for x in range(4):
    print(f"Прости, {guest.pop()}, но я не смогу тебя принять")
# rm1 = guest.pop()
# print(f"Прости, {rm1}, но я не смогу тебя принять")
# rm2 = guest.pop()
# print(f"Прости, {rm2}, но я не смогу тебя принять")
# rm3 = guest.pop()
# print(f"Прости, {rm3}, но я не смогу тебя принять")
# rm4 = guest.pop()
# print(f"Прости, {rm4}, но я не смогу тебя принять")
#
# for x in guest:
#     print(f"Приглашение остается в силе, {x}")
#
# del guest[1]
# del guest[0]
#
# print(guest)