import sys


# units of ingredients
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '', '', '']

# names of ingredients 
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']

# list of ingredients available
pantry = {}

# recipes
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2, 0, 0]
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 0, 0, 3]
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 0, 5, 0]
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0, 0, 0]
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 0, 0.5, 1]

# list of recipes
# menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]


# list with the name of the recipes
# menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]

##################################################################################################################################################

with open("recipe.txt", 'r') as file: #opens file
    menu_list=[] #creates an empty list in the variable memu_List
    menu=[] # creates an empty list in the variable menu
    ingredients_dict={} # creates an empty dictionary in the variable ingredients_dict
    for line in file: # iterates through the file by line
        linex=line.strip("\n") # removes the new line character in the line
        if line[0].isdigit(): # checks if the line starts with a number or not.
            line_list=line.strip("\n").split(" ",1) # puts line into list so that i can access the individual part such as the number and the ingredient.
            ingredients_dict[line_list[1]]=float(line_list[0]) # puts into a dict the ingredient as a key and the amount as the value inside that key
        else: # if line doesnt start with a number, which means its the start of a recipe so this would be the recipe name.
            menu_list.append(linex) # adds recipe name to the list
            if ingredients_dict: # asks if the dict is filled with something so that it can add it to the list, this happens when all the ingredients have already been added.
                menu.append(ingredients_dict) # adds dict to list
                ingredients_dict={} # empties the dict for the next recipe's ingredients
    menu.append(ingredients_dict) # adds dict to list

#####################################################################################################################################################
def if_recipes_has_enoguh_ingredients(): #My new function that returns a list of recipes that you can cook
    the_recipe=None #Throwaway value to change later
    new_menu_list=[] # the empty list that Imma add the available recipes to.
    for i in range(len(menu_list)): # iterates through the values of menu list
        for key in menu[i]:

            if float(menu[i][key]) * servings <= pantry[key]: # checks if the ingredient times servings is less than the number in pantry so that we know if it has enough of this ingredient to make the asked for amount
                the_recipe=True #if it passed then the recipe is true
            else:
                the_recipe=False # if the ingredient doesnt pass then the recipe is false and it breaks to check the nect interation in the menu list, whcih means the next recipe.
                break
        if the_recipe==True: #if the recipe is still true after that whole loop it means that the recipe is cookable so I add it to the list
                new_menu_list.append(menu_list[i])
    return new_menu_list #returns the list of available recipes




# ask for ingredients available
def pantry_ingredients(units, ingredients): # This whole function is used to ask how many ingredients you have to enter it into the pantry and use it later on.                                                                                                                                    #change
    for i in range(len(units)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = input(f'How many {unit}{ingredient} do you have? ')
        pantry[unit + ingredient]=float(item) #adds to pantry which is a dict: ingredient as the key and the amount as the value
    global servings #I moved global servings here so that it asks after inputing the amount ingredients you have.
    servings = int(input("How many servings? "))  
    


# show the ingredients of an exisiting pantry
def show_pantry():  #This functions is used to show whats in the pantry in the format number .... ingredient                                                                                                                                                                                                     #dont change
    for key in pantry:
        print(f'{pantry[key]} {key}')
    global servings #added the servings here too so it asks after it shows pantry
    servings = int(input("How many servings? "))

    
 

# show the menu options
def recipe_menu():  #This function is used as the recipe book and shows the options you have, then it asks you to select an option                                                                                   
    
    
    
                                                                                      
    print("What would you like to cook? Here's the recipe book:")
    global new_menu_list2 #makes the list global so i can use it everywhere
    new_menu_list2=(if_recipes_has_enoguh_ingredients())# assigns the fucntion to a variable so I can access it outside of the functiom
    if len(new_menu_list2) >=1: #checks if list empty or not
        for i in range(len(new_menu_list2)): # prints all the available recipes
            print(i+1, ". ", new_menu_list2[i], sep="") # two ways i can do it, use a new list for the print, or print menu_list if function turns out true
    
    # add new recipe
    
    print(len(new_menu_list2)+1, ". Add new recipe.", sep="") # used len(new_menu_list2)+1 so that it always prints after the the list is printed

    # exit program 
    print(len(new_menu_list2)+2, ". Nevermind, I don't want to cook anything (Exit).", sep="") #used len(new_menu_list2)+2 so that it always prints after add new recipe
    
    option = int(input("Select an option by typing its number here:"))
    
    # if new recipe selected
    if option == len(new_menu_list2)+1: #use my new menu list instead of old one so that it works
      new_recipe_name = input("Name of the new recipe: ")
      menu_list.append(new_recipe_name)
    

      new_recipe = {} # new_recipe is a dict
      for i in range(len(units)):
          unit = units[i]
          if unit:
              unit += ' of '
          ingredient = ingredients[i]
          item = input(f'How many {unit}{ingredient} are required? ')
          new_recipe[unit + ingredient]=float(item) #adds new recipe to a dict like the other recipes, in the same format
      menu.append(new_recipe) # adds the dict into menu so that it is in the same place as the other recipes


      with open("recipe2update.txt", 'a') as file: #opens file in append mode
        file.write(new_recipe_name + '\n') #writes new recipe name to file
        
        for key in new_recipe: #writes to file the ingredients of that new recipe
            file.write(str(new_recipe[key]) + " " + str(key))
            file.write("\n")






    #return option selected
    return option

# check valid option
def valid_option(option): #This function is used to to execute the option you selected in the past function
    while True:
      # valid option
      if option in range(1,len(new_menu_list2)+1): #change menu_list to my new menu list2
          recipe= menu[menu_list.index(new_menu_list2[option-1])] #finds the index in the old menu list than option-1 so that the recipe is the correct one
          break

      # exit program
      elif option == len(new_menu_list2)+2: #changes it to my new menu list2 so that the exit works
          print('See you later!')
          sys.exit(0)

      # invalid option
      else:
          print('Please select a valid option')
          option = recipe_menu()
    return recipe

# update pantry
def pantry_update(): #This function is used to update your pantry by substacting the ingredients used in the recipe that you cooked
    for key in pantry:
        leftover = pantry[key] - float(recipe[(key)])*servings # changed recipe[key] to float so that the equation works since it was previous in str
        if leftover < 0: 
            # if not enough ingredients
            return False
        pantry[key]=(leftover) #Adds to pantry the new values aka the leftovers
    
    # if enough ingredients
    return True


# ask user to input ingredients available
pantry_ingredients(units, ingredients) #This function does a lot of things, it prints the selected option, checks if the option is valid, and cooks it and prints out a message and the remainder of the pantry, but if you dont have enough ingredients, it prints a message and you have to update the pantry.


cook = True

# initialize servings to 1
while cook:
    # ask user what they'd like to make (from options)
    option = recipe_menu()
    print(f'You selected option {option}')
    
    # verify the selected option is valid
    recipe = valid_option(option)
    
    # if the option is valid and want to cook
    
    # while not enough ingredients
    while not pantry_update(): 
      print('Not enough ingredients!')
      print("Update the ingredients.")
      pantry_ingredients(units, ingredients)
    
    # enough ingredients.
    print('Great choice. That was delicious!')
    print("Here's what's left in the pantry: ")
    show_pantry()