character = {
    'name': 'Hanzo',
    'ultimate': 'Tickling Dragons',
    'role': 'Defense Damage',
    'weapon': 'Bow and Arrows',
    'brother': 'Genji',
    'hates': 'Payload',
    'endorsment_level': '1'
}
# read a value by key 
print(character['weapon'])

# loop through dictionary items
for x, y in character.items():
    print('{}: {}'.format(x, y))

# printed keys and values seperetly 
print(character.keys())
print(character.values())

# add another pair to dictionary
character['toxicity'] = 'very high'

# delete a pair from the dictionary
del character['brother']

# modify a key
character['enemy'] = character['hates']
del character['hates']

print(character)