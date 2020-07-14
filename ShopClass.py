##################################################################
# Class Name:  Shop
# Abstract:    Blueprint for Shop, properties and behaviors
##################################################################
class Shop(object):

    #Class variables
    _strCompanyName = "Bike Rental LLC"
    _intShopCount   = 0 
    _dblHourlyRate  = float(5.00)  
    _dblDailyRate   = float(20.00)
    _dblWeeklyRate  = float(60.00) 
    _dblFamilyDiscountRate = float(0.3)  #Family Discount starts at a rent of 3 bikes



    ##################################################################
    # Name:     __init__
    # Abstract: Constructor - automatically called when instance of 
    #           class is created.
    ##################################################################
    def __init__(self, strShopName, strEmail, strPhone, strState, strCity, strAddress, strZipCode):
        
        self.strShopName = strShopName

        self.strEmail   = strEmail
        self.strPhone   = strPhone
        self.strState   = strState
        self.strCity    = strCity
        self.strAddress = strAddress
        self.strZipCode = strZipCode

        self.dblIncome          = 0.00
        self.intBikesAvailable  = 0
        self.intBikesTotalCount = 0
        
        #Parallel lists to store renting information
        self.__aintAmountRenting  = []             #list of amount of bikes  rentted
        self.__astrTypeRented     = []             #list of types per rent
        self.__aintTypeMultiplier = []             #list of types per rent
        self.__aintRentsIDs       = []             #list of ID per rent
        self.__acstRenters        = []             #list of coustomers who rentet
        self.__ablnRenturned      = []             #list if rents were returned
        self.__adblRentsTotals    = []             #list iof total for each rent


        self. _AdjustCount()


    ###############
    ##  PROPERTY ##
    ###############

    

    #######################################################################
    # Decoration: @property
    # Name:       strShopName
    # Abstract:   Returns value of the "encapsulated" __strShopName
    #######################################################################
    @property
    def strShopName(self):
        return self.__strShopName


    #######################################################################
    # Decoration: @property
    # Name:       strEmail
    # Abstract:   Returns value of the "encapsulated" __strEmail
    #######################################################################
    @property
    def strEmail(self):
        return self.__strEmail 


    #######################################################################
    # Decoration: @property
    # Name:       strPhone
    # Abstract:   Returns value of the "encapsulated" __strPhone
    #######################################################################
    @property
    def strPhone(self):
        return self.__strPhone



    #######################################################################
    # Decoration: @property
    # Name:       strState
    # Abstract:   Returns value of the "encapsulated" __strState
    #######################################################################
    @property
    def strState(self):
        return self.__strState



    #######################################################################
    # Decoration: @property
    # Name:       strCity
    # Abstract:   Returns value of the "encapsulated" __strCity
    #######################################################################
    @property
    def strCity(self):
        return self.__strCity



    #######################################################################
    # Decoration: @property
    # Name:       strAddress
    # Abstract:   Returns value of the "encapsulated" strAddress
    #######################################################################
    @property
    def strAddress(self):
        return self.__strAddress



    #######################################################################
    # Decoration: @property
    # Name:       strZipCode
    # Abstract:   Returns value of the "encapsulated" __strZipCode
    #######################################################################
    @property
    def strZipCode(self):
        return self.__strZipCode


    #######################################################################
    # Decoration: @property
    # Name:       dblIncome
    # Abstract:   Returns value of the "encapsulated" __dblIncome
    #######################################################################
    @property
    def dblIncome(self):
        return self.__dblIncome


    
    #######################################################################
    # Decoration: @property
    # Name:       intBikesAvailable
    # Abstract:   Returns value of the "encapsulated" __intBikesAvailable
    #######################################################################
    @property
    def intBikesAvailable(self):
        return self.__intBikesAvailable


    #######################################################################
    # Decoration: @property
    # Name:       intBikesTotalCount
    # Abstract:   Returns value of the "encapsulated" __intBikesTotalCount
    #######################################################################
    @property
    def intBikesTotalCount(self):
        return self.__intBikesTotalCount



    #######################################################################
    # Decoration: @property
    # Name:       intBikesTotalCount
    # Abstract:   Returns value of the "encapsulated" __aintTypeMultiplier
    #######################################################################
    @property
    def aintTypeMultiplier(self):
        return self.__aintTypeMultiplier



    #######################################################################
    # Decoration: @property
    # Name:       aintAmountRenting
    # Abstract:   Returns value of the "encapsulated" __aintAmountRenting
    #######################################################################
    @property
    def aintAmountRenting(self):
        return self.__aintAmountRenting



    #######################################################################
    # Decoration: @property
    # Name:       astrTypeRented
    # Abstract:   Returns value of the "encapsulated" __astrTypeRented
    #######################################################################
    @property
    def astrTypeRented(self):
        return self.__astrTypeRented



    #######################################################################
    # Decoration: @property
    # Name:       aintRentsIDs
    # Abstract:   Returns value of the "encapsulated" __aintRentsIDs
    #######################################################################
    @property
    def aintRentsIDs(self):
        return self.__aintRentsIDs


    
    #######################################################################
    # Decoration: @property
    # Name:       acstRenters
    # Abstract:   Returns value of the "encapsulated" __acstRenters
    #######################################################################
    @property
    def acstRenters(self):
        return self.__acstRenters


   
    #######################################################################
    # Decoration: @property
    # Name:       ablnRenturned
    # Abstract:   Returns value of the "encapsulated" __ablnRenturned
    #######################################################################
    @property
    def ablnRenturned(self):
        return self.__ablnRenturned



    
    #######################################################################
    # Decoration: @property
    # Name:       adblRentsTotals
    # Abstract:   Returns value of the "encapsulated" __adblRentsTotals
    #######################################################################
    @property
    def adblRentsTotals(self):
        return self.__adblRentsTotals



    ###############
    ##  SETTER   ##
    ############### 

    ##################################################################
    # Decoration: @strShopName.setter
    # Name:       strShopName
    # Abstract:   Sets the value of the "encapsulated" __strShopName
    ##################################################################
    @strShopName.setter
    def strShopName(self, strShopName):
        
        try:
       
            if (strShopName != ""):
                self.__strShopName = strShopName

            else:
                raise RuntimeError('Shop name can not be an empty string.')
       
        except RuntimeError as error:

            print(error)




    ##################################################################
    # Decoration: @strEmail.setter
    # Name:       strEmail
    # Abstract:   Sets the value of the "encapsulated" __strEmail
    ##################################################################
    @strEmail.setter
    def strEmail(self, strEmail):
        
        try:
       
            if (strEmail != ""):
                self.__strEmail = strEmail

            else:
                raise RuntimeError('Email can not be an empty string.')
       
        except RuntimeError as error:

            print(error)



    ##################################################################
    # Decoration: @strPhone.setter
    # Name:       strPhone
    # Abstract:   Sets the value of the "encapsulated" __strPhone
    ##################################################################
    @strPhone.setter
    def strPhone(self, strPhone):
        
        try:
       
            if (strPhone != ""):
                self.__strPhone = strPhone

            else:
                raise RuntimeError('Phone can not be an empty string.')
       
        except RuntimeError as error:

            print(error)



    ##################################################################
    # Decoration: @strPhone.setter
    # Name:       strState
    # Abstract:   Sets the value of the "encapsulated" __strState
    ##################################################################
    @strState.setter
    def strState(self, strState):
        
        try:
       
            if (strState != ""):
                self.__strState = strState

            else:
                raise RuntimeError('State may not be an empty string.')
       
        except RuntimeError as error:

            print(error)




    ##################################################################
    # Decoration: @strCity.setter
    # Name:       strCity
    # Abstract:   Sets the value of the "encapsulated" __strCity
    ##################################################################
    @strCity.setter
    def strCity(self, strCity):
        
        try:
       
            if (strCity != ""):
                self.__strCity = strCity

            else:
                raise RuntimeError('City may not be an empty string.')
       
        except RuntimeError as error:

            print(error)




    ##################################################################
    # Decoration: @strAddress.setter
    # Name:       strAddress
    # Abstract:   Sets the value of the "encapsulated" __strAddress
    ##################################################################
    @strAddress.setter
    def strAddress(self, strAddress):
        
        try:
       
            if (strAddress != ""):
                self.__strAddress = strAddress

            else:
                raise RuntimeError('Address may not be an empty string.')
       
        except RuntimeError as error:

            print(error)




    ##################################################################
    # Decoration: @strZipCode.setter
    # Name:       strZipCode
    # Abstract:   Sets the value of the "encapsulated" __strZipCode
    ##################################################################
    @strZipCode.setter
    def strZipCode(self, strZipCode):
        
        try:
       
            if (strZipCode != ""):
                self.__strZipCode = strZipCode

            else:
                raise RuntimeError('ZipCode may not be an empty string.')
       
        except RuntimeError as error:

            print(error)


    ##################################################################
    # Decoration: @dblIncome.setter
    # Name:       dblIncome
    # Abstract:   Sets the value of the "encapsulated" __dblIncome
    ##################################################################
    @dblIncome.setter
    def dblIncome(self, strIncome):
        
        try:
            dblIncome = float(0)  
            dblIncome =  float(strIncome)

            if dblIncome >= 0: 
                self.__dblIncome = dblIncome   

            else:
                raise RuntimeError('Shop income may not be nagative.')
       
        #ValueError - will catch errors if can not cast when 'dblIncome =  int(strIncome)'
        except ValueError as error:
            dblIncome = float(0)
            print("Shop income must be a number.")

        except RuntimeError as error:

            print(error)

        return




    ##################################################################
    # Decoration: @intBikesAvailable.setter
    # Name:       intBikesAvailable
    # Abstract:   Sets the value of the "encapsulated" __intBikesAvailable
    ##################################################################
    @intBikesAvailable.setter
    def intBikesAvailable(self, strBikesAvailable):
        
        try:
            intBikesAvailable = int(0)  
            intBikesAvailable =  int(strBikesAvailable)

            if intBikesAvailable >= 0: 
                self.__intBikesAvailable = strBikesAvailable   

            else:
                raise RuntimeError('Bike available count may not be nagative.')
       
        #ValueError - will catch errors if can not cast when 'intBikesAvailable =  int(strBikesAvailable)'
        except ValueError as error:
            intBikesAvailable = int(0)
            print("Bike available count must be a whole number.")

        except RuntimeError as error:

            print(error)

        return




    ##################################################################
    # Decoration: @intBikesTotalCount.setter
    # Name:       intBikesTotalCount
    # Abstract:   Sets the value of the "encapsulated" __intBikesTotalCount
    ##################################################################
    @intBikesTotalCount.setter
    def intBikesTotalCount(self, strBikesTotalCount):
        
        try:
            intBikesTotalCount = int(0)  
            intBikesTotalCount =  int(strBikesTotalCount)

            if intBikesTotalCount >= 0: 
                self.__intBikesTotalCount = intBikesTotalCount   

            else:
                raise RuntimeError('Bike total count may not be nagative.')
       
        #ValueError - will catch errors if can not cast when 'intBikesTotalCount =  int(strBikesTotalCount)'
        except ValueError as error:
            intBikesTotalCount = int(0)
            print("Bike total count must be a whole number.")

        except RuntimeError as error:

            print(error)

        return



    ##################################################################
    # Decoration: @aintAmountRenting.setter
    # Name:       aintAmountRenting
    # Abstract:   Sets the value of the "encapsulated" __aintAmountRenting
    ##################################################################
    @aintAmountRenting.setter
    def aintAmountRenting(self, strAmountRenting):
        
        try:
            intAmountRenting = int(0)  
            intLength =  len(self.aintAmountRenting)
            intAmountRenting = int(strAmountRenting) 
            if intAmountRenting > 0: 
                self.__aintAmountRenting[intLength] = intAmountRenting   

            else:
                raise RuntimeError('Amount rentted amount must be greater than 0.')


        #ValueError - will catch errors if can not cast when 'intAmountRenting = int(strAmountRenting)'
        except ValueError as error:
            intAmountRenting = int(0)
            print("The amount rentted must be a whole number.")

        except RuntimeError as error:

            print(error)

    
       

    ##################################################################
    # Decoration: @acstRenters.setter
    # Name:       acstRenters
    # Abstract:   Sets the value of the "encapsulated" __acstRenters
    ##################################################################
    @acstRenters.setter
    def acstRenters(self, objCustomerRenter):
        
        try:
            if type(objCustomerRenter).__name__ == 'Customer':

                intLength =  len(self.acstRenters)
                self.__acstRenters[intLength] = objCustomerRenter
                   
            else:
                raise RuntimeError('Renter must be of type Customer.')

        except RuntimeError as error:

            print(error)

    

    ##################################################################
    # Decoration: @aintRentsIDs.setter
    # Name:       aintRentsIDs
    # Abstract:   Sets the value of the "encapsulated" __aintRentsIDs
    ##################################################################
    @aintRentsIDs.setter
    def aintRentsIDs(self, strRentID):
        
        try:
            intRentID = int(0)  
            intLength =  len(self.aintRentsIDs)

            intRentID = int(strRentID) 
            if intRentID > 0: 
                self.__aintRentsIDs[intLength] = intRentID   

            else:
                raise RuntimeError('Rent ID must be greater than 0.')


        #ValueError - will catch errors if can not cast when 'intAmountRenting = int(strAmountRenting)'
        except ValueError as error:
            intRentID = int(0)
            print("Rent ID rentted must be a whole number.")

        except RuntimeError as error:

            print(error)

    



    ##################################################################
    # Decoration: @aintTypeMultiplier.setter
    # Name:       aintTypeMultiplier
    # Abstract:   Sets the value of the "encapsulated" __aintTypeMultiplier
    ##################################################################
    @aintTypeMultiplier.setter
    def aintTypeMultiplier(self, strTypeMultiplier):
        
        try:
            intTypeMultiplier = int(0)  
            intLength =  len(self.aintTypeMultiplier)


            intTypeMultiplier = int(strTypeMultiplier) 

            if intTypeMultiplier > 0: 
                self.__aintTypeMultiplier[intLength] = intTypeMultiplier   

            else:
                raise RuntimeError('Type multiplier must be greater than 0.')


        #ValueError - will catch errors if can not cast when 'intTypeMultiplier = int(strTypeMultiplier)'
        except ValueError as error:
            intTypeMultiplier = int(0)
            print("Type multiplier must be a whole number.")

        except RuntimeError as error:

            print(error)
         

    ##################################################################
    # Decoration: @astrTypeRented.setter
    # Name:       astrTypeRented
    # Abstract:   Sets the value of the "encapsulated" __astrTypeRented
    ##################################################################
    @astrTypeRented.setter
    def astrTypeRented(self, strTypeRented):
        
        try:
       
            if (strTypeRented =="H" or strTypeRented =="D" or strTypeRented =="W" ): 
                intLength =  len(self.astrTypeRented)
                self.__astrTypeRented[intLength] = strTypeRented

            else:
                raise RuntimeError('Rent type can only be "H", "D" or "W" only.')
       
        except RuntimeError as error:

            print(error)

        return

    ##################################################################
    # Decoration: @ablnRenturned.setter
    # Name:       ablnRenturned
    # Abstract:   Sets the value of the "encapsulated" __ablnRenturned
    ##################################################################
    @ablnRenturned.setter
    def ablnRenturned(self, blnRenturned):
        
        try:
       
            if (blnRenturned == True or blnRenturned == False): 
                intLength =  len(self.ablnRenturned)
                self.ablnRenturned[intLength] = blnRenturned

            else:
                raise RuntimeError('Return status can only be True or False.')
       
        except RuntimeError as error:

            print(error)

        return

    
    ##################################################################
    # Decoration: @adblRentsTotals.setter
    # Name:       adblRentsTotals
    # Abstract:   Sets the value of the "encapsulated" __adblRentsTotals
    ##################################################################
    @adblRentsTotals.setter
    def adblRentsTotals(self, strRentsTotal):
        
        try:
            dblRentTotal = float(0)  
            intLength =  len(self.adblRentsTotals)

            dblRentTotal = float(strRentsTotal) 

            if dblRentTotal >= 0: 
                self.__adblRentsTotals[intLength] = dblRentTotal   

            else:
                raise RuntimeError('Rent total can not be nagative.')


        #ValueError - will catch errors if can not cast when 'intAmountRenting = int(strAmountRenting)'
        except ValueError as error:
            dblRentTotal = float(0)
            print("Rent total must be a number.")

        except RuntimeError as error:

            print(error)

        return
 

    #############################
    ##  Regular class Methods  ##
    ############################# 

    ##################################################################
    # Name:     _AdjustCount
    # Abstract: Adds one to Shops count
    ##################################################################
    def _AdjustCount(self):
        
        Shop._intShopCount += 1

        return


    ##################################################################
    # Name:     _CheckAvailability
    # Abstract: Check if amount of bike are availabe
    ##################################################################
    def _CheckAvailability(self, intAmountRequested):

        blnAvailabe = False

        if (self.intBikesAvailable >= intAmountRequested ):
            
            blnAvailabe = True

        return blnAvailabe


    ##################################################################
    # Name:       ValadatePositiveInteger
    # Abstract:   Valadates input is a positive integer
    ##################################################################
    def ValidatePositiveInteger(self, strInput):

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
    # Name:       ValadateRentType
    # Abstract:   Valadates rent's type
    ##################################################################
    def  ValadateRentType(self, strLetter):

        blnReturn = False

        if strLetter == "H" or strLetter == "h":
            blnReturn = True

        elif strLetter == "D" or strLetter == "d":
            blnReturn = True

        elif strLetter == "W" or strLetter == "w":
            blnReturn = True


        return blnReturn 

   

    ##################################################################
    # Name:       ValadateIsRentID
    # Abstract:   Valadates RentID is in list aintRentsIDs
    ##################################################################
    def  ValadateIsRentID(self, strRentID):

        blnReturn = False

        for rentID in self.aintRentsIDs:
            
            if (strRentID == rentID):
            
                blnReturn =True
                

        return blnReturn 


    ##################################################################
    # Name:       ValadateIsCustomer
    # Abstract:   Valadates object is of type Customer
    ##################################################################
    def  ValadateIsCustomer(self, objCustomer):

        blnReturn = False

        if type(objCustomer).__name__ == 'Customer':
            
            blnReturn =True


        return blnReturn 



    ##################################################################
    # Name:     AddBikes
    # Abstract: Add Bikes to shpo's inventory
    ##################################################################
    def AddBikes(self, strAmount):
        
        blnPositiveInteger = False
        intAmont = int(0)

        #Validate Input
        blnPositiveInteger = self.ValidatePositiveInteger(strAmount)

        if(blnPositiveInteger == True):

            intAmont =int(strAmount)                                            
            self.intBikesAvailable += intAmont
            self.intBikesTotalCount += intAmont

        return



    ##################################################################
    # Name:     RentBikes
    # Abstract: Check if amount of bike are availabe
    ##################################################################
    def RentBikes(self, objCustomer, strAmountRequested, strTypeOfRent, strTypeMultiplier):
        try:

            blnValidCustomer       = False
            blnValidRentType       = False
            blnValidAmount         = False
            blnValidTypeMultiplier = False
            
            intRentID         = int(0)
            intAmount         = int(0)
            intTypeMultiplier = int(0)
            blnAvailable      = False

            #Validate Input
            blnValidCustomer = self.ValadateIsCustomer(objCustomer)
            blnValidRentType = self.ValadateRentType(strTypeOfRent)
            blnValidAmount   = self.ValidatePositiveInteger(strAmountRequested)
            blnValidAmount   = self.ValidatePositiveInteger(strTypeMultiplier)


            #If valid
            if (blnValidCustomer == True) and (blnValidRentType ==True) and (blnValidAmount ==True) and(blnValidAmount ==True):

                intAmount         = int(strAmountRequested)
                intTypeMultiplier = int(strTypeMultiplier)

                blnAvailable = self._CheckAvailability(intAmount)

                if (blnAvailable ==True):

                    #This is the acctual Rent Processes
                    intLength =  len(self.aintRentsIDs)                
                    intRentID = intLength + 1                          # => RentIDs will be [1,2,3,4..]
                    self.intBikesAvailable -= intAmount             
                    self.aintRentsIDs.append(intRentID)          
                    self.acstRenters.append(objCustomer)        
                    self.astrTypeRented.append(strTypeOfRent)  
                    self.aintTypeMultiplier.append(intTypeMultiplier)  
                    self.aintAmountRenting.append(intAmount)  
                    self.ablnRenturned.append(False)    
                    self.adblRentsTotals.append(self._CalculateRentTotal(intAmount, strTypeOfRent, intTypeMultiplier))

                    objCustomer.ReceiveRentData(self, intRentID)

                else:
                    print("\n\tThe amount requested is not avaialable, the shop currently only has ", self.intBikesAvailable, "bikes available")

            #Not valid
            else:
                raise RuntimeError('Arguments sent to RentBikes are not valid.')



        #ValueError - will catch errors if can not cast when 'intAmount = int(strAmount)'
        except ValueError as error:
            intAmount = int(0)
            print("Amount of bikes to be rented must be a whole number.")


        except RuntimeError as error:
            print(error)

        return  



    ##################################################################
    # Name:     _CalculateRentTotal
    # Abstract: Calculate Rent Total at rent time and stores data
    ##################################################################
    def _CalculateRentTotal(self, strAmount, strTypeOfRent, strTypeMultiplier):
                                                                                                
        blnValidRentType       = False
        blnValidAmount         = False
        blnValidTypeMultiplier = False
                                                                                                
        dblRentTotal =      float(0)
        dblFamilyDiscountMultiplier = float(1.00)
        intAmount =         int(0)
        intAmountWithDiscount = int(0)
        intTypeMultiplier = int(0)

        #Validate Input
        blnValidRentType = self.ValadateRentType(strTypeOfRent)
        blnValidAmount   = self.ValidatePositiveInteger(strAmount)
        blnValidAmount   = self.ValidatePositiveInteger(strTypeMultiplier)


        #If valid
        if  (blnValidRentType ==True) and (blnValidAmount ==True) and(blnValidAmount ==True):

            intAmount         = int(strAmount)
            intTypeMultiplier = int(strTypeMultiplier)

            #Family Discount starts at 3 bikes but max out at 5: "•	Family Rental, a promotion that can include from 3 to 5 rentals"
            if(intAmount >= 3):                                     #"rentals (of any type) with a discount of 30% of the total price. "
                dblFamilyDiscountMultiplier = 1 - Shop._dblFamilyDiscountRate
                if(intAmount > 5):
                    intAmount -=  5
                    intAmountWithDiscount = 5
                else:
                    intAmountWithDiscount = intAmount
                    intAmount =  0


            if strTypeOfRent =='H'or strTypeOfRent =='h':
                                #Amount No Discount                                     #Amount with Discount
                dblRentTotal = (intAmount * Shop._dblHourlyRate * intTypeMultiplier) + (intAmountWithDiscount * Shop._dblHourlyRate * intTypeMultiplier)* dblFamilyDiscountMultiplier

            elif strTypeOfRent =='D' or strTypeOfRent =='d':
                dblRentTotal = (intAmount * Shop._dblDailyRate * intTypeMultiplier) + (intAmountWithDiscount * Shop._dblDailyRate * intTypeMultiplier)* dblFamilyDiscountMultiplier
                #dblRentTotal = intAmount * Shop._dblDailyRate * intTypeMultiplier  * dblFamilyDiscountMultiplier

            elif strTypeOfRent =='W' or strTypeOfRent =='w':
                dblRentTotal = (intAmount * Shop._dblWeeklyRate * intTypeMultiplier) + (intAmountWithDiscount * Shop._dblWeeklyRate * intTypeMultiplier)* dblFamilyDiscountMultiplier
                #dblRentTotal = intAmount * Shop._dblWeeklyRate * intTypeMultiplier * dblFamilyDiscountMultiplier

        #Not valid
        else:
            raise RuntimeError('Arguments sent from RentBikes are not valid.')

        return dblRentTotal



    ##################################################################
    # Name:     ReciveBikeBack
    # Abstract: ReciveBikeBack from customer
    ##################################################################
    def ReciveBikeBack(self, intRentID):

        blnValidRentID = self.ValadateIsRentID(intRentID)

        #If valid
        if(blnValidRentID == True):
            intIndex =  self.aintRentsIDs.index(intRentID)
        
            self.ablnRenturned[intIndex] = True 
            self.intBikesAvailable += self.aintAmountRenting[intIndex]


        #Not valid
        else:
            print("Bikes returned have invalid Rent ID or have not returned from a Customer")

        return 



    ##################################################################
    # Name:       FullRentTypeFromLetter
    # Abstract:   creates FullRentType string, (e.g D to Day )
    ##################################################################
    def FullRentTypeFromLetter(self, strLetter):

        strReturn = ""

        if strLetter == "H" or strLetter == "h":
            strReturn = "Hour"
        elif strLetter == "D" or strLetter == "d":
            strReturn = "Day"
        elif strLetter == "W" or strLetter == "w":
            strReturn = "Week"


        return strReturn 



    ##################################################################
    # Name:     PrintShopDetails
    # Abstract: Print Shop Details
    ##################################################################
    def PrintShopInformation(self, intNumber = ""):

        print("\n\n========================================================================")
        print("",intNumber ,"Shop: ", self.strShopName)
        print("========================================================================")
        print("Contact Information:\t\t\t\tLocation:")
        print("--------------------\t\t\t\t---------")
        print("Email:\t", self.strEmail,"\t\tState:\t", self.strState)
        print("Phone:\t", self.strPhone,"\t\t\t\tCity:\t", self.strCity)
        print("\t\t\t\t\t\tAddress:", self.strAddress)
        print("\t\t\t\t\t\tZip Code:", self.strZipCode)
        print("Available Bikes:\t",self.intBikesAvailable)
        print("")
        return 



    ##################################################################
    # Name:     PrintCustomerReport
    # Abstract: Print Customer Report
    ##################################################################
    def PrintCustomerReport(self, objCustomer):

        intCount  = 0;
        intLength = 0
        intIndex  = 0
        dblTotalRentsDue = 0
        dblTotalRents = 0
        intLength = len(self.aintRentsIDs)
        strFullType = ""
        strReturned =""

        print("\n")
        print("\t||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("\t||")
        print("\t||\tCustomer all Transactions Report ")
        print("\t||\t-----------------------------------------")
        
        print("\t||")
        print("\t||\tCustomer:\t\t\tShop:")
        print("\t||\t---------\t\t\t-------")
        print("\t||\tLast Name:  ",objCustomer.strLastName, "\t\tName:",self.strShopName)
        print("\t||\tFirst Name: ",objCustomer.strFirstName, "\t\tState:",self.strState)
        print("\t||\tEmail:      ",objCustomer.strEmail, "\t\tCity:",self.strCity)
        print("\t||\tPhone:      ",objCustomer.strPhone, "\tAddress:",self.strAddress)
        print("\t||\t\t\t",                      "\t\tEmail:",self.strEmail)
        print("\t||\t\t\t",                      "\t\tPhone:",self.strPhone)
        print("\t||\n\t||")


        strReturned ="\t(Bikes Returned)"

        for intIndex in range(intLength):
               
            #Only rents for this customer
            if(self.acstRenters[intIndex] == objCustomer):
                                    
                if(self.ablnRenturned[intIndex] == False ):
                    strReturned = ""
                    dblTotalRentsDue += self.adblRentsTotals[intIndex]

                intCount += 1
                strFullType = self.FullRentTypeFromLetter(self.astrTypeRented[intIndex]) +"s"

                print("\t||\t",intCount, ".", self.aintAmountRenting[intIndex], "bikes for", self.aintTypeMultiplier[intIndex], strFullType, " =\t ",self.adblRentsTotals[intIndex], strReturned)
                dblTotalRents += self.adblRentsTotals[intIndex]

                strReturned = "\t(Bikes Returned)"

        print("\t||")
        print("\t||\t\t\t\t\t --------")
        print("\t||\t\tTotal Transactions:\t$",dblTotalRents)
        print("\t||\t\t\tTotal Due:\t$",dblTotalRentsDue)
        print("\t|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("")
        
        return 


    ##################################################################
    # Name:     IssueBill
    # Abstract: IssueBill from customer
    ##################################################################
    def IssueBill(self, objCustomer):

        intCount  = 0;
        intLength = 0
        intIndex  = 0
        dblTotalRents = 0
        strFullType = ""
        strTitle = ""

        intLength = len(self.aintRentsIDs)


        print("\n")


        print("\t||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("\t||")
        print("\t||\tCustomer Bill:")
        print("\t||\t--------------")

        print("\t||")
        print("\t||\tCustomer:\t\t\tShop:")
        print("\t||\t---------\t\t\t-------")
        print("\t||\tLast Name:  ",objCustomer.strLastName, "\t\tName:",self.strShopName)
        print("\t||\tFirst Name: ",objCustomer.strFirstName, "\t\tState:",self.strState)
        print("\t||\tEmail:      ",objCustomer.strEmail, "\t\tCity:",self.strCity)
        print("\t||\tPhone:      ",objCustomer.strPhone, "\tAddress:",self.strAddress)
        print("\t||\t\t\t",                      "\t\tEmail:",self.strEmail)
        print("\t||\t\t\t",                      "\t\tPhone:",self.strPhone)
        print("\t||\n\t||")

        for intIndex in range(intLength):
               
            #Only rents for this customer
            if(self.acstRenters[intIndex] == objCustomer):

                if(self.ablnRenturned[intIndex] == False ):
                
                    intCount += 1
                    strFullType = self.FullRentTypeFromLetter(self.astrTypeRented[intIndex]) +"s"

                    print("\t||\t",intCount,". ",self.aintAmountRenting[intIndex], "bikes for", self.aintTypeMultiplier[intIndex], strFullType, " =\t ",self.adblRentsTotals[intIndex])
                    dblTotalRents += self.adblRentsTotals[intIndex]
    

        print("\t||")
        print("\t||\t\t\t --------")
        print("\t||\t\t\tTotal Due:\t$",dblTotalRents)
        print("\t|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("")
        
        return 
