
#################################################################################
# Name:       Benjamin Gomori
# Assignment: Bob's Bike Rental System 
# Abstract:   Project 2
# Due Date:   11/25/2019

 #Note:  For the family discount I give for up to 5 bickes for a rent transaction.
 #       If customer rents 10 bikes for example, than 5 will get 30 % off,
 #       the other five are full price. 
            
#################################################################################

import ShopClass as Shp
import CustomerClass as Cst

##################################################################
# Name:       ValadatePositiveInteger
# Abstract:   Valadates input is a positive integer
##################################################################
def ValidatePositiveInteger(strInput):

    try:
        blnReturn = False
        intInput = int(0)  

        intInput = int(strInput) 
        
        if intInput > 0: 
            blnReturn = True

    #ValueError - will catch errors if can not cast when 'intInput = int(strInput)'
    except ValueError as error:
        intInput = int(0)

    return blnReturn



##################################################################
# Name:       CollectPositiveInteger
# Abstract:   Collect positive integer from user
##################################################################
def CollectPositiveInteger(strMessage):

    blnIsPositiveInteger = False

    while(blnIsPositiveInteger == False):

        strInput = input(strMessage)
        
        blnIsPositiveInteger = ValidatePositiveInteger(strInput)

    return strInput



##################################################################
# Name:       CollectStringFromUser 
# Abstract:   Collects string from user
##################################################################
def CollectStringFromUser(strMessage):

    blnIsEmptyString = True

    while(blnIsEmptyString == True):

        strInput = input(strMessage)
        
        if strInput != "":
            blnIsEmptyString = False

    return strInput


##################################################################
# Name:       CollectRentTypeFromUser 
# Abstract:   Collects rent type from user
##################################################################
def CollectRentTypeFromUser():

    blnIsValidRentType = False
    strInput = ""
    strMessage = ""

    strMessage ="\tEnter the type of rent 'H', 'D' or 'W' (hourly, daily or weekly):\t"
    
    while(blnIsValidRentType == False):

        strInput = input(strMessage)
        
        if strInput == "H" or strInput == "h":
            blnIsValidRentType = True
        
        elif strInput == "D" or strInput == "d":
            blnIsValidRentType = True

        elif strInput == "W" or strInput == "w":
            blnIsValidRentType = True

    return strInput      


##################################################################
# Name:       FullRentTypeFromLetter
# Abstract:   creates FullRentTypeFromLetter, D -> Day
##################################################################
def FullRentTypeFromLetter(strLetter):

    strReturn = ""

    if strLetter == "H" or strLetter == "h":
        strReturn = "Hour"
    elif strLetter == "D" or strLetter == "d":
        strReturn = "Day"
    elif strLetter == "W" or strLetter == "w":
        strReturn = "Week"

    return strReturn  



##################################################################
# Name:       CollectTypeMultiplier 
# Abstract:   Collect Type Multiplier  from user
##################################################################
def CollectTypeMultiplier(strType):

    blnIsPositiveInteger = False
    strInput = ""
    strMessage = ""
    strFullType =""

    strFullType = FullRentTypeFromLetter(strType)


    strMessage ="\tEnter the amount of " + strFullType + "s you want to rent for:\t\t\t\t"
    
    while(blnIsPositiveInteger == False):

        strInput = input(strMessage)
        blnIsPositiveInteger = ValidatePositiveInteger(strInput)

    return strInput  



##################################################################
# Name: PrintIntroduction
# Abstract: introduce user to the application
##################################################################
def PrintIntroduction():
    print("##########################################################################################################")
    print("WELCOME to Bob's Bike Rental System application!")
    
    print("\nIn this application you can:")
    print("------------------------------")
    print("View shop information, create customers, connect to shops, rent bikes, return bikes and request reports.")
    print("The application enables each customer to rent multiple times and from multiple shops.")

    print("\n3 Most Important Menus  are\t=>Main Menu(M)\t=>Customer Menu(C)\t=>Shop Menu(S)")
    print("\nYou can switch between the menus by entering the letter M, C and S.")
    print("Each of the 5 menus will list all the commands available for that menu.")
    print("We hope you enjoy the experience.")

    print("##########################################################################################################")

    return



##################################################################
# Name: Main Menu
# Abstract: provides user with categories of object to pick from
##################################################################
def  MainMenu(objShopA, objShopB, objShopC, aobjCustomers = None, objCurrentCustomer = None):
  
    try:

        blnLoop =True
        strCategoryChoice = ""
        blnIsPositive = False 

        print("\n\n")
        print("=>>Main Menu (M)")
        print("=======================")
        print("\n [Commands]\n")
        print("    S  =>\tShop Menu")
        print("    C  =>\tCustomer Menu") 

        print("")

        print("    E  => \tExit")
        print("\n")

        #User can conly redirect to other menu or exit program
        while(blnLoop):

            strCategoryChoice = input("Please enter your command:\t")
            
            if(strCategoryChoice == 'E' or strCategoryChoice == 'e'):
                raise Exception("\nSee you soon..")
           
            elif(strCategoryChoice == 'S' or strCategoryChoice == 's'):
                blnLoop = False
                ShopMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)
            
            elif(strCategoryChoice == 'C' or strCategoryChoice == 'c'):
                blnLoop = False
                CustomerMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)


    except Exception as error:
        print(error)
    return



##################################################################
# Name: Shop Menu
# Abstract: user can view the shops details
##################################################################
def  ShopMenu(objShopA, objShopB, objShopC, aobjCustomers = None, objCurrentCustomer = None):
    
    try:

        blnLoop =True
        strShopChoice = ""
        intShopchoice = int (0)
        blnIsPositive = False 

        print("\n\n")
        print("=>>Shop Menu (S)")
        print("=======================")
        print("\n [Commands]\n")
        print("    1  =>\tColumbus    (view details)")
        print("    2  =>\tCincinnati  (view details)")
        print("    3  =>\tCleveland   (view details)")

        print("")

        print("    M  => \tMain menu")
        print("    C  => \tCustomer menu")
        print("    E  => \tExit")
        print("\n")

        #User can conly redirect to other menu or exit program
        while(blnLoop):

            strShopChoice = input("Please enter your command:\t")

            if(strShopChoice == 'E' or strShopChoice == 'e'):
                raise Exception("See you soon..")

            elif(strShopChoice == 'M' or strShopChoice == 'm'):
                blnLoop = False
                MainMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)

            elif(strShopChoice == 'C' or strShopChoice == 'c'):
                blnLoop = False
                CustomerMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)

            #Validate                                    
            blnIsPositive = ValidatePositiveInteger(strShopChoice)

            if(blnIsPositive == True):
                intShopchoice = int(strShopChoice)

                if(intShopchoice == 1):
                    objShop1.PrintShopInformation(1)
                elif(intShopchoice == 2):
                    objShop2.PrintShopInformation(2)
                elif(intShopchoice == 3):
                    objShop3.PrintShopInformation(3)

    except Exception as error:
        print(error)
        
    return



##################################################################
# Name: Customer Menu
# Abstract: user can view the shops details
##################################################################
def  CustomerMenu(objShopA, objShopB, objShopC, aobjCustomers = None, objCurrentCustomer = None):
    
    try:

        blnLoop =True
        strCustomerPick = ""
        intCustomerPick = int (0)
        strInput = ""
        blnIsPositive = False 
        intCustomerCount = 0           
    
        print("\n\n")
        print("=>>Customer Menu (C)")
        print("=======================")

        #If there are customers
        if (len(aobjCustomers) != 0):
            print("\n [Commands]\n")
            for customer in aobjCustomers:
                intCustomerCount += 1
                print("    ", +intCustomerCount ," =>\tCustomer", intCustomerCount, ":", customer.strLastName, customer.strFirstName  )
        else:
            #No customers
            print("-No customers were created yet.")
            print("\n [Commands]\n")

        print("\n     N  => \tCreate New Customer")

        print("")

        print("     M  => \tMain menu")
        print("     S  => \tShop menu")
        print("     E  => \tExit")
        print("\n")

        while(blnLoop):

            strCustomerPick = input("Please choose a command\\customer:\t")

            if(strCustomerPick == 'E' or strCustomerPick == 'e'):
                raise Exception("See you soon..")
            elif(strCustomerPick == 'M' or strCustomerPick == 'm'):
                blnLoop = False
                MainMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)
 
            elif(strCustomerPick == 'S' or strCustomerPick == 's'):
                blnLoop = False
                ShopMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)

            elif(strCustomerPick == 'N' or strCustomerPick == 'n'):

                #When user clicks 'N'
                #Creating new customer
                print("\n\nCreating New Customer")
                print("===========================")
                print("\tCollecting personal data:")
                strLastName  = CollectStringFromUser("\tEnter the customer's last name:\t\t")
                strFirstName = CollectStringFromUser("\tEnter the customer's first name:\t")
                strEmail     = CollectStringFromUser("\tEnter the customer's email address:\t")
                strPhone     = CollectStringFromUser("\tEnter the customer's phone number:\t")
    
                #Creats new customer instcance
                objCurrentCustomer = Cst.Customer(strLastName, strFirstName, strEmail, strPhone)
       
                #Adds customer to list of customers
                aobjCustomers.append(objCurrentCustomer)

                #Recursive call - to reload with customer in list of options avaialble to user
                blnLoop = False
                CustomerMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)


            #Validate                                    
            blnIsPositive = ValidatePositiveInteger(strCustomerPick)

            if(blnIsPositive == True):

                intCustomerPick = int(strCustomerPick)

                #Checking if user entered an integer prisinted with as option
                #By making sure it (intCustomerPick - 1) is a valid index in the list[] of customers
                if(intCustomerPick >= 1 and intCustomerPick <= intCustomerCount):
                    
                    #assigning user pick to current customer 
                    objCurrentCustomer = aobjCustomers[intCustomerPick -1]

                    blnLoop = False
                    CustomerPickShopMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)

    except Exception as error:
            print(error)
        
    return



##################################################################
# Name: CustomerPickShopMenu
# Abstract: user picks shop to interatct with 
##################################################################
def  CustomerPickShopMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer):
    
    try:

        blnLoop =True
        strShopPick = ""
        intShopPick = int (0)
        blnIsPositive = False 

        print("\n\n")
        print("=>>Choose Shop Menu")
        print("=======================")
        print("Please choose a shop to do business with:")
        print("\n [Commands]\n")
        print("    1  => \tColumbus \t["  , objShopA.intBikesAvailable, " bikes available]")
        print("    2  => \tCincinnati\t[" , objShopB.intBikesAvailable, " bikes available]")
        print("    3  => \tCleveland\t["  , objShopC.intBikesAvailable, " bikes available]")

        print("")
        print("    M  => \tMain menu")
        print("    C  => \tCustomer menu")
        print("    E  => \tExit")
        print("\n")

        while(blnLoop):

            strShopPick = input("Please enter your command:\t")
    
            if(strShopPick == 'E' or strShopPick == 'e'):
                raise Exception("See you soon..")

            elif(strShopPick == 'M' or strShopPick == 'm'):
                blnLoop = False
                MainMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)
      
            elif(strShopPick == 'C' or strShopPick == 'c'):
                blnLoop = False
                CustomerMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)
        
            #Validate                                    
            blnIsPositive = ValidatePositiveInteger(strShopPick)

            if(blnIsPositive == True):
                
                intShopPick = int(strShopPick)

                if(intShopPick == 1):

                    objCurrentCustomer.objShopInterctingWith = objShop1
                    blnLoop = False
                    CustemerActionMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)

                elif(intShopPick == 2):
                    objCurrentCustomer.objShopInterctingWith = objShop2
                    blnLoop = False
                    CustemerActionMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)

                elif(intShopPick == 3):
                    objCurrentCustomer.objShopInterctingWith = objShop3
                    blnLoop = False
                    CustemerActionMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)

    except Exception as error:
            print(error)
        
    return



##################################################################
# Name: CustemerActionMenu
# Abstract: user can interatct with shop
##################################################################
def  CustemerActionMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer):
    
    try:
        blnLoop =True
        strActionPick = ""
        intActionPick = int (0)
        blnIsPositive = False 

        print("\n\n")
        print("\nCustomer '", objCurrentCustomer.strLastName, objCurrentCustomer.strFirstName,"' can now do business with the '", objCurrentCustomer.objShopInterctingWith.strShopName, "' shop") 

        print("\n=>>Action Menu")
        print("=======================")
        print("\n [Commands]\n")
        print("    1  => \tRent bikes")
        print("    2  => \tReturn bikes")
        print("    3  => \tOverall report")

        print("")
        print("    M  => \tMain menu")
        print("    C  => \tCustomer menu")
        print("    S  => \tShop menu")
        print("    E  => \tExit")
        print("\n")

        while(blnLoop):

            strCustomerCommandPick = input("Please enter your command:\t")

            if(strCustomerCommandPick == 'E' or strCustomerCommandPick == 'e'):
                raise Exception("See you soon..")

            elif(strCustomerCommandPick == 'M' or strCustomerCommandPick == 'm'):
                blnLoop = False
                MainMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)
      
            elif(strCustomerCommandPick == 'C' or strCustomerCommandPick == 'c'):
                blnLoop = False
                CustomerMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)
            
            elif(strCustomerCommandPick == 'S' or strCustomerCommandPick == 's'):
                blnLoop = False
                ShopMenu(objShopA, objShopB, objShopC, aobjCustomers, objCurrentCustomer)
            
                #Validate                                    
            blnIsPositive = ValidatePositiveInteger(strCustomerCommandPick)

            if(blnIsPositive == True):

                intCustomerCommandPick = int(strCustomerCommandPick)

                intAmountOfBike = 0
                strTypeOfRent = 0
                intTypeMultiplier = 0


                if(intCustomerCommandPick == 1):
                    print("")
                    print("\t!!!!DISCOUNT - Rent more than Two bikes and get 30% off on up to 5 bikes  !!!!")                  
                    print("\n\tTo rent bikes we need to collect some data:\n")                  

                    intAmountOfBike = CollectPositiveInteger("\tEnter the number of bikes you want to rent:\t\t\t\t")                    
                  
                    strTypeOfRent = CollectRentTypeFromUser()       
                    strTypeOfRent.capitalize()

                    intTypeMultiplier = CollectTypeMultiplier(strTypeOfRent)           
                    
                    objCurrentCustomer.RentBikes(intAmountOfBike, strTypeOfRent, intTypeMultiplier)
                    print("")

                elif(intCustomerCommandPick == 2):
                    print("")
                    objCurrentCustomer.ReturnBikes()
                    print("")

                elif(intCustomerCommandPick == 3):
                    print("")
                    objCurrentCustomer.RequestReports()
                    print("")

        
    except Exception as error:
            print(error)
        
    return



##################################################################
# Name:     Main
# Abstract: program starts here
##################################################################

PrintIntroduction()

#Create 3 shop instances 
objShop1 = Shp.Shop("Columbus Bikes", "Columbus@estrEmail.email", "11-222-222", "OH", "Columbus", "204 Main str.", "74110",)
objShop2 = Shp.Shop("Cincinnati Bikes", "cincibikes@estrEmail.email", "111-111-1111", "OH", "Cincinnati", "104 Elm str.", "45202",)
objShop3 = Shp.Shop("Cleveland Bikes", "clevbikes@estrEmail.email", "333-333-3333", "OH", "Cleveland", "204 Side str.", "32210",)
objShop1.AddBikes(15)
objShop2.AddBikes(7)
objShop3.AddBikes(8)

aobjCustomers = []
MainMenu(objShop1,objShop2,objShop3, aobjCustomers)

print("\n\n")
