def LogInOrSignUp():
    #what the function will return
    returnvalue = ""
    
    #LOGIN OR SIGN UP PART

    #The user database keeps user's main information for log-in
    userdatabase = {"ilovechickennuggies": "67lover","ihatechickens": "nonoword", "mylove4u": "neverending", "crushiecakes": "wowzers2themax"}

    #Options for logging in or signing in
    option = input("""  Welcome to the Log-in Page!!!

        Please input your choice:
    [L] for Log-in;   [S] for Sign-up
    [INPUT]: """).title()
    print("")

    #The code for the log-in part
    if option == "L":
        print("""
    (If you chose the wrong option, type "0" in the username area!)""")
        while True:
            user = input("Enter username: ")
            
            # Escape the program: the first 0 is lowercase the other is upper case
            if user == "0" or user == "0":
                returnvalue = "Escape"
                break
            
            pasw = input("Enter password: ")

            # For successful log-in:
            if user in userdatabase and userdatabase[user] == pasw:
                print("""
    Log-in successful! Welcome to Cooking Scholar!""")
                returnvalue = "Login"
                break

            
            # For unsuccessful log-in
            else:
                print("""
    Incorrect user or password! Please try again!
    """)

    #The code for the sign-up part
    elif option == "S":
        print("""
    (If you chose the wrong option, type "0" in the username area!)""")    
        while True:
            newuse = input("Enter a new username: ")
            
            # If user chose a username already taken
            if newuse in userdatabase:
                print("The username is already taken, change it to another one by restarting the program!")
                returnvalue = "Escape"
                break
            
            elif newuse == "0" or newuse == "0":
                returnvalue = "Escape"
                break
            
            pasw = input("Enter your chosen password: ")

            if newuse not in userdatabase:
                userdatabase[newuse] = pasw
                print(f"""
    Welcome, {newuse}! Thank you for using Cooking Scholar!""")
                returnvalue = "Signup"
                break

    else:
        print("Invalid option!")
    
    return returnvalue

