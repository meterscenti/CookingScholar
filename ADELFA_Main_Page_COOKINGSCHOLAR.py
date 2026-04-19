import ADELFA_Food_Database_Search_COOKINGSCHOLAR
allergens = []
savedRecipes = []
def MainPage():
    #Cooking Scholar Main Page

    print("""

    *****COOKING SCHOLAR -- HOMEPAGE*****)

    """)

    hmpg = input("""HOMEPAGE INSTRUCTIONS:
    Please enter
    [1] To enter textbox,
    [2] For your saved recipes,
    [3] Exit.
    
    """)

    UserIngredients = []
    allergens = []
    if hmpg == '1':
        while True:
            ingredient = input("Please Enter 1 ingredient, type 'done' to stop: ")
            if ingredient == 'done':
                break
            UserIngredients.append(ingredient)
        while True:
            allergy = input("Please Enter 1 allergen that you have, type 'done' to stop: ")
            if allergy == 'done':
                break
            allergens.append(allergy)
        
        returned = ADELFA_Food_Database_Search_COOKINGSCHOLAR.Search(allergens, set(UserIngredients))
        if returned[0] == "Saved Something":
                savedRecipes.append(returned[1])
    elif hmpg == '2':
        print("***SAVED RECIPES***")
        for food in savedRecipes:
            print(food)
    elif hmpg == '3':
        return "Exit"
    else:
        print("Key does not exist")

        

