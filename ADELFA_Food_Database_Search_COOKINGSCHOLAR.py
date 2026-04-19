import ADELFA_Food_Database_COOKINGSCHOLAR

def Search(allergen, UserIngredients):
    #the numbers could be strings because they are ingredients
    #the second element in their values is the points
    #3rd and 4th, allergen and ID
    recipes = {"Fish Fillet" : [["fish", "egg", "flour"],0, False, 1],
               "Fried Rice" : [["rice","soy sauce","onions"],0, False, 2],
               "Egg Sandwich" : [["egg","bread","dressing"],0, False, 3]}

    #This is the ingredients the client has
    ingredients = UserIngredients
        
    #This block adds a point for each recipe if the ingredients match
    for food in recipes.keys():
        for i in ingredients:
            if i.lower() in recipes[food][0]:
                if i.lower() in allergen:
                    recipes[food][2] = True  
                recipes[food][1] += 1
                
        recipes[food][1] = round(recipes[food][1]/len(recipes[food][0])*100, 2)
    #Sorts them in descending order so those that matches pop up first
    sortedRecipes = dict(sorted(recipes.items(), key=lambda item: item[1][1], reverse = True))

    #prints all of them
    print ("""

                """)
    for key, value in sortedRecipes.items():
        print(f"{key}: {value[1]}% matching ingredients, Contains Allergen: {value[2]}, ID: {value[3]}")
        
    
    recipe = int(input("What recipe do you want to cook(ID): "))
    
    for r, instructions in ADELFA_Food_Database_COOKINGSCHOLAR.Recipes.items():
        if r == recipe:
            print(f"{instructions}")
            food = instructions
    
    save = input("Would you like to save this recipe(Yes/No): ").lower()
    if save == "yes":
        return ["Saved Something", food]