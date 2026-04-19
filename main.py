#All functions and made modules will happen here

import ADELFA_Tutorial_COOKINGSCHOLAR
import ADELFA_Log_In_Page_COOKINGSCHOLAR
import ADELFA_Main_Page_COOKINGSCHOLAR
import ADELFA_Suggestion_COOKING_SCHOLAR

#Gives a quick tutorial to the user
while True:
    match ADELFA_Log_In_Page_COOKINGSCHOLAR.LogInOrSignUp():
        case "Signup":
            print("    Since you are new, have a quick tutorial")
            ADELFA_Tutorial_COOKINGSCHOLAR.Tutorial()
            break
        case "Login":
            break

ADELFA_Suggestion_COOKING_SCHOLAR.Suggest()
while True:
    if ADELFA_Main_Page_COOKINGSCHOLAR.MainPage() == "Exit":
        break

print("Closing Program...")





        
        
    
     
    




