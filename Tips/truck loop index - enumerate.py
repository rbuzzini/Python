names = ['Corey', 'Chris', 'Dave', 'Travis']

# Bad practice:
index = 0
for name in names:
    print(index, name)
    index += 1

# Good practice with enumerate function:
for index, name in enumerate(names):
    print(index, name)


# Tip to loop through multiple lists:
names2 = ['Peter Parker', 'Clark Kent', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Batman']

# Bad practice:
for index, name in enumerate(names2):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# Good practice: use zip function to initially unpack the lists:
universes = ['Marvel', 'DC', 'DC']
for name, hero, universe in zip(names2, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')