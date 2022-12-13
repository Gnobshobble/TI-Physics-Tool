# initalize a dictionary of menu options for navigation. Indexing to avoid clunky user input 
menu_options = {1: 'Atwoods', 2: 'Projectiles', 3: 'Newtonian Equations', 4: 'Energy', 5: 'Power and Work'}

# print the dictionary keys and entries by line so the user can select an option
for option_key in menu_options:
    print(f'{option_key}: {menu_options[option_key]}')

# get user input
def get_user_menu_option():
    inp = -1
    while inp not in menu_options_keys:
        inp = int(input('Select an option: '))
    return inp
selection = get_user_menu_option()

# Atwoods
# projectile motion
# constant accelleration newton equations
# conservation of energy for changing accelleration
# power and work calculator