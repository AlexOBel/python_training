# friend = {
#     'first_name': 'Max',
#     'last_name': 'Stamet',
#     'age': '27',
#     'city': 'Ekb',
#     }
#
# print(friend['first_name'])
# print(friend['last_name'])
# print(friend['age'])
# print(friend['city'])
#############################################

# like_numbers = {
#     'Lisa': '25',
#     'Ben': '12',
#     'Vik': '72',
#     'Pit': '13',
#     'Max': '1',
# }
# # print(like_numbers)
#
# # for key, value in like_numbers.items():
# #     print(f'Diar friend {key}, like {value} number')
# # for name in like_numbers.keys():
# #     print(name)
# # for name in sorted(like_numbers.keys()):
# #     print(name.title())

# rivers = {
#     'Russia': 'Amur',
#     'Brazil': 'Amazonka',
#     'Ukraine': 'Dnepr',
#     }
#
# for country, river in rivers.items():
#     print(f'The {river} runs in {country}')
#
# for river in rivers.values():
#     print(f"\n{river}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ('bob', 'bill', 'jen', 'sarah', 'edward', 'phil', 'pit')
for name in people:
    if name in favorite_languages:
        print(f'{name} опрос пройден!')
    else:
        print(f'{name} пройди опрос!')