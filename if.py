# alien_color = 'red'
# if alien_color == 'green':
#     print("ты заработал 5 очков")
# if alien_color == 'red':
#     print("ты заработал 5 очков")


# alien_color = 'green'
# if alien_color == 'green':
#     print("ты заработал 5 очков")
# elif alien_color == 'yellow':
#     print("ты заработал 10 очков")
# elif alien_color == 'red':
#     print("ты заработал 15 очков")
#
# alien_color = 'yellow'
# if alien_color == 'green':
#     print("ты заработал 5 очков")
# elif alien_color == 'yellow':
#     print("ты заработал 10 очков")
# elif alien_color == 'red':
#     print("ты заработал 15 очков")
#
# alien_color = 'red'
# if alien_color == 'green':
#     print("ты заработал 5 очков")
# elif alien_color == 'yellow':
#     print("ты заработал 10 очков")
# elif alien_color == 'red':
#     print("ты заработал 15 очков")


# users = ['Alex', 'Bob', 'San', 'Vik', 'admin']
#
# for user in users:
#     if user == 'admin':
#         print(f'Hello, {user.title()}, would you like to see a status report')
#     else:
#         print(f'Hello, {user}')


# users = ['Bob']
# if users:
#     for user in users:
#         if user == 'admin':
#             print(f'Hello, {user.title()}, would you like to see a status report')
#         else:
#             print(f'Hello, {user}')
# else:
#     print("We need to ind some users!")


current_users = ['Alex', 'Bob', 'San', 'Vik', 'admin']
current_users_lower = []
for current_user_lower in current_users:
    current_users_lower.append(current_user_lower.lower())
# print(current_users_lower)
new_users = ['Pit', 'Sam', 'Bob', 'san']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry, but this name - {new_user} occupied, changed him')
    else:
        print(f'Add new user, {new_user}')

integer = []
for integ in range(1,10):
    integer.append(integ)
print(integer)

for int_value in integer:
    if int_value == 1:
        print(f'{int_value}st')
    elif int_value == 2:
        print(f'{int_value}nd')
    elif int_value == 3:
        print(f'{int_value}rd')
    else:
        print(f'{int_value}th')