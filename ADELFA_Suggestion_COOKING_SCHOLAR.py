def Suggest():
    print("""Per aspera ad astra! Welcome to the Cooking Scholar (*-*)!

        """)

    print("""*RECIPES TO MAKE YOUR DAY*
    """) #Suggested daily recipes


    print("""
    o Tinola
    o Adobo 
    o Sinigang """)

    print()
    a = input("Would you like to select a recipe, type 'no' if none?  ").lower() #User selects recipe, otherwise browsing is continued
    if a.lower() == "no":
        print("Noted! You may continue browsing (*o*)!")
    elif a.lower() == "tinola":
        print("""
=== Tinola ===
1.Heat oil in a pot.
2.Sauté garlic, onion, and ginger. Add the ground black pepper.
3.When the onion starts to get soft, add the chicken. Cook for 5 minutes or until it turns light brown.
4.Pour the water. Let boil. Cover and then set the heat to low. Boil for 40 minutes.
5.Scoop and discard the scums and oil on the soup.
6.Add the Knorr chicken cube and chayote or papaya. Stir. Cover and cook for 5 minutes.
7.Put the malunggay and hot pepper leaves in the pot and pour the fish sauce in. Continue to cook for 2 minutes.
8.Transfer to a serving bowl. Serve.

source: https://panlasangpinoy.com/classic-tinolang-manok-recipe/
""")
    elif a.lower() == "adobo":
        print("""
=== Adobo ===
1.Combine chicken, 1/4 of the total amount of garlic, whole peppercorn, dried bay leaves, soy sauce, vinegar,
and water in a cooking pot. Cover and let boil. Stir and make sure that all ingredients are well blended.
2.Add Chicken Cube and sugar. Stir. Cover the pot and cook for 10 minutes.
3.Turn the chicken over and cook the opposite side for another 10 minutes. Set aside.
4.Heat oil in a clean pan. Saute remaining garlic until it turns light brown.
5.Pan fry the chicken for 1 minute per side. Pour the adobo sauce into the pan. Boil until it reduces to half.

source: https://panlasangpinoy.com/easy-chicken-adobo-recipe/
""")
    elif a.lower() == "sinigang":
        print("""
1.Rinse pork ribs and drain well.
2.In a pot over medium heat, combine pork and enough water to cover. Bring to a boil, skimming scum that accumulates on top.
3.Once broth clears, add tomatoes, onion, and fish sauce. Lower heat and simmer for
about 1 to 1 ½ hours or until meat is tender, adding more water as necessary to maintain about 8 cups.
4.Add gabi and cook for about 4 to 6 minutes or until tender.
5.Add chili peppers and radish. Continue to simmer for about 2 to 3 minutes.
6.Add long beans. Continue to cook for about 2 minutes.
7.Add eggplant and okra and cook for another 1 to 2 minutes.
8.If using packaged tamarind base, add to the pot and stir until completely dissolved.
9.Season with salt and pepper to taste.
10.Add bok choy and continue to cook for about 1 minute. Serve hot.
""")
