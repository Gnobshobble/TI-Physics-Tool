# initalize a dictionary of menu options for navigation. Indexing to avoid clunky user input 
menu_options = {1: 'Atwoods', 2: 'Projectiles', 3: 'Newtonian Equations', 4: 'Energy', 5: 'Power and Work'}

# print the dictionary keys and entries by line so the user can select an option
for i, option in enumerate(menu_options):
    print(f'{i}: {option}')

# get user input
input = input('')

# Atwoods
# projectile motion
# constant accelleration newton equations
# conservation of energy for changing accelleration
# power and work calculator