# initalize a dictionary of menu options containg subdictionaries. Indexing to avoid clunky user input. 
# subdictionaries act as sudo objects, containing varyable feilds
menu_options = {1: {'name': 'atwoods'}, 
2: {'name': 'projectiles'}, 
3: {'name': 'newtonian equations'}, 
4: {'name': 'energy'}, 
5: {'name': 'power and work'}}

# print the dictionary keys and entries by line so the user can select an option
for option_key in menu_options:
    print(f'{option_key}: {menu_options[option_key]["name"]}')

# get user input
def get_user_menu_option():
    inp = -1
    while inp not in list(menu_options.keys()):
        inp = int(input('Select an option: '))
    return menu_options[inp]["name"]
selection = get_user_menu_option()

print(selection)

# Atwoods
# projectile motion
# constant accelleration newton equations
# conservation of energy for changing accelleration
# power and work calculator