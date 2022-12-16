# initalize a dictionary of menu options containg subdictionaries. Indexing to avoid clunky user input. 
# subdictionaries act as sudo objects, containing varyable feilds
menu_options = {
1: {'name': 'atwoods', 'accelleration': 9.8, 'mass1': 1, 'mass2': 2, 'tension': 10}, 
2: {'name': 'projectiles'}, 
3: {'name': 'newtonian equations'}, 
4: {'name': 'energy'}, 
5: {'name': 'power and work'}, 
}

# print the dictionary keys and entries by line so the user can select an option
for option_key in menu_options:
    print(f'{option_key}: {menu_options[option_key]["name"]}')

# get user input as an index and return the name of the type of problem as a string so it can be used 
# later for operations
def get_user_menu_option():
    inp = -1
    while inp not in list(menu_options.keys()):
        inp = int(input('Select an option by entering its number: '))
    return menu_options[inp]["name"]
selection = get_user_menu_option()

def determine_varyables(problem_type):
    if (problem_type == 'atwoods'):
        # make a list of the varyables to be used for the equaltions
        varyables = list(menu_options[1].keys())
        varyables.remove('name')
        # print out the user options with adjusted indexes for readability
        for i in range(len(varyables)):
            print(f'{i+1}: {varyables[i]}')
        # declare a varyable to store the unkown varyable
        solving_for = 'meaing of life'
        while solving_for not in varyables:
            try:
                solving_for = varyables[int(input('Solving for: '))-1]
            except:
                for i in range(len(varyables)):
                    print(f'{i+1}: {varyables[i]}')
                print(f"error, try again with a number 1-{len(varyables)}")
        print(f'solving: {solving_for}')
        # go through and set all unkown varyables. Alternate behavior for string entry.
        varyables.remove(solving_for)
        var_list = {}
        for varyable in varyables:
            var_list[varyable] = float(input(f"enter value for {varyable}: "))
        print(var_list)
        

def problem_solver(problem_type):
    # run a series of checks to determine first the type of probem and then the varyables involved 
    if (problem_type == 'atwoods'):
        varyables = determine_varyables(problem_type)
        
problem_solver(selection)