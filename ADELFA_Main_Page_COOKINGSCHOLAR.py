import ADELFA_Food_Database_Search_COOKINGSCHOLAR
allergens = []
def MainPage():
    #Cooking Scholar Main Page

    print("""Per aspera ad astra! Welcome to the Cooking Scholar (*-*)!

    """)



    print("""*RECIPES TO MAKE YOUR DAY*
    """) #Suggested daily recipes


    print("""
    o Tinola
    o Champorado 
    o Sinigang """)

    print()
    a = input("Would you like to select a recipe, type 'no' if none?  ").lower() #User selects recipe, otherwise browsing is continued
    if a == "no":
        print("Noted! You may continue browsing (*o*)!")



    print("""

    *****COOKING SCHOLAR -- HOMEPAGE*****)

    """)

    print()
    print()

    hmpg = input("""HOMEPAGE INSTRUCTIONS:
    Please enter
    [1] To enter textbox,
    [2] For your saved recipes,
    [3] Exit.
    
    """)

    UserIngredients = []
    allergens = []
    savedRecipes = []
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
        print("You don't have any saved recipes.")
    elif hmpg == '3':
        return "Exit"
    else:
        print("Key does not exist")

        

