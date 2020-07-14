import PersonClass as Prs

##################################################################
# Class Name:  Customer
# Abstract:    Blueprint for Customer, properties and behaviors
##################################################################
class Customer(Prs.Person):

    #Class variables
    _intCustomerCount = 0  

    ##################################################################
    # Name:     __init__
    # Abstract: Constructor - automatically called when instance of 
    #           class is created.
    ##################################################################
    def __init__(self, strLastName, strFirstName, strEmail, strPhone):

        Prs.Person.__init__(self, strLastName, strFirstName)
        self.strEmail       = strEmail
        self.strPhone       = strPhone
       
        self.dblDebt = float(0)

        
        #Parallel lists to store renting information
        self.__aintAmountRenting  = []             #list of amount of bikes  rentted
        self.__astrTypeRented     = []             #list of types per rent
        self.__aintRentsIDs       = []             #list of ID per rent
        self.__ashpShpsRentedFrom = []             #list of shops rentet from
        self.__ablnRenturned      = []             #list if rents were returned
        
        self.__objShopInterctingWith = None       #No business when created        

        self._AdjustCount()



    ###############
    ##  PROPERTY ##
    ###############



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
    # Name:       dblDebt
    # Abstract:   Returns value of the "encapsulated" __dblDebt
    #######################################################################
    @property
    def dblDebt(self):
        return self.__dblDebt



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
    # Name:       ashpShpsRentedFrom
    # Abstract:   Returns value of the "encapsulated" __ashpShpsRentedFrom
    #######################################################################
    @property
    def ashpShpsRentedFrom(self):
        return self.__ashpShpsRentedFrom


   
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
    # Name:       objShopInterctingWith
    # Abstract:   Returns value of the "encapsulated" __objShopInterctingWith
    #######################################################################
    @property
    def objShopInterctingWith(self):
        return self.__objShopInterctingWith



    ###############
    ##  SETTER   ##
    ############### 





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
    # Decoration: @objShopInterctingWith.setter
    # Name:       objShopInterctingWith
    # Abstract:   Sets the value of the "encapsulated" __objShopInterctingWith
    ##################################################################
    @objShopInterctingWith.setter
    def objShopInterctingWith(self, objShop):
        
        try:
              
            if type(objShop).__name__ == 'Shop':
                self.__objShopInterctingWith = objShop

            else:
                raise RuntimeError('Customer can only connect to shops.')
       
        except RuntimeError as error:

            print(error)


    ##################################################################
    # Decoration: @dblDebt.setter
    # Name:       dblDebt
    # Abstract:   Sets the value of the "encapsulated" __dblDebt
    ##################################################################
    @dblDebt.setter
    def dblDebt(self, strDebt):

        try:
            dblDebt = float(0)  

            dblDebt = float(strDebt) 
        
            if dblDebt >= 0: 
                self.__dblDebt = dblDebt   

            else:
                raise RuntimeError('Debt amount must be greater than 0.')


        #ValueError - will catch errors if can not cast when 'dblDebt = float(strDebt)'
        except ValueError as error:
            dblDebt = float(0)
            print("Debt must be a number.")


        #RuntimeError - will catch the raised error when Type price is not greater than 0 
        except RuntimeError as error:
            print(error)


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
    # Decoration: @ashpShpsRentedFrom.setter
    # Name:       ashpShpsRentedFrom
    # Abstract:   Sets the value of the "encapsulated" __ashpShpsRentedFrom
    ##################################################################
    @ashpShpsRentedFrom.setter
    def ashpShpsRentedFrom(self, objShopRentedFrom):
        
        try:
            if type(objShopRentedFrom).__name__ == 'Shop':

                intLength =  len(self.ashpShpsRentedFrom)
                self.__ashpShpsRentedFrom[intLength] = objShopRentedFrom
                   
            else:
                raise RuntimeError('Shop rented from must be of type shop.')

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


    #############################
    ##  Regular class Methods  ##
    ############################# 
    
    ##################################################################
    # Name:     _AdjustCount
    # Abstract: Adds one to Shops count
    ##################################################################
    def _AdjustCount(self):
        
        Customer._intCustomerCount += 1

        return


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
    # Name:       ValadateIsShop
    # Abstract:   Valadates object is of type Shop
    ##################################################################
    def  ValadateIsShop(self, objShop):

        blnReturn = False

        if type(objShop).__name__ == 'Shop':
            
            blnReturn =True


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
    # Name:     ConnectToShop
    # Abstract: Connect To Shop by getting its shopID
    ##################################################################
    def ConnectToShop(self, objShop):                                              
        try:

            blnIsShop = False
           
            blnIsShop = this.ValadateIsShop(objShop)

            if  blnIsShop == True:                               

                self.objShopInterctingWith = objShop

            else:
                raise RuntimeError('Intercting shop must be a shop object.')

        except RuntimeError as error:
            print(error)

        return


    ##################################################################
    # Name:     RentBikes 
    # Abstract: Rent Bikes from shop (already connected to)
    ##################################################################
    def RentBikes(self, strAmountOfBike, strTypeOfRent, strTypeMultiplier):                                              
        try:

            blnValidShop           = False
            blnValidRentType       = False
            blnValidAmount         = False
            blnValidTypeMultiplier = False

            intAmount         = int(0)
            intTypeMultiplier = int(0)


            #Validate Input
            blnValidShop     = self.ValadateIsShop(self.objShopInterctingWith)
            blnValidRentType = self.ValadateRentType(strTypeOfRent)
            blnValidAmount   = self.ValidatePositiveInteger(strAmountOfBike)
            blnValidTypeMultiplier   = self.ValidatePositiveInteger(strTypeMultiplier)

            #If valid
            if (blnValidShop == True) and (blnValidRentType ==True) and (blnValidAmount ==True) and(blnValidTypeMultiplier ==True):

                intAmount         = int(strAmountOfBike)
                intTypeMultiplier = int(strTypeMultiplier)
                                             
                self.objShopInterctingWith.RentBikes(self, intAmount, strTypeOfRent, intTypeMultiplier)
            
            #Not valid
            else:
                raise RuntimeError('Invalid arguments in customer rent bikes.')


        except RuntimeError as error:
            print(error)

        return

    
    ##################################################################
    # Name:     ReceiveRentData 
    # Abstract: Used by shop to send customer  
    ##################################################################
    def ReceiveRentData(self, objShop, intRentID):                                              
        try:
            
            blnValidShop           = False

            blnValidShop = self.ValadateIsShop(objShop)


            if (blnValidShop == True):                                           
                
                
               self.__aintRentsIDs.append(intRentID)
               self.__ashpShpsRentedFrom.append(objShop)
               self.__ablnRenturned.append(False)

               print("\n\tCustomer has rented the bikes successfully.")

            else:
                raise RuntimeError('Internal error - Shop object must be sent to ReceiveRentData().')


        except RuntimeError as error:
            print(error)

        return




    ##################################################################
    # Name:     ReturnBikes 
    # Abstract: Customer returns all bikes to shop connected to
    ##################################################################
    def ReturnBikes(self):                                              
        try:

            self.RequestBill()

            intIndex = 0
            intLength = 0 
            blnAllReturnedAlready = True

            intLength = len(self.aintRentsIDs)

            
            if( intLength > 0):

                for intIndex in range(intLength):
                    
                    #This if controls that only returns bikes to this shop
                    if(self.ashpShpsRentedFrom[intIndex] == self.objShopInterctingWith):
                    
                        intRentID = self.aintRentsIDs[intIndex]

                        if(self.ablnRenturned[intIndex] == False):
                        
                            blnAllReturnedAlready = False

                            self.ashpShpsRentedFrom[intIndex].ReciveBikeBack(intRentID)
                            self.ablnRenturned[intIndex] = True
                
            else:
                strMessage = "\tCustomer " + self.strLastName+ " " + self.strFirstName + " had not rented any bikes from this shop."
                raise RuntimeError(strMessage)

            if(blnAllReturnedAlready ==True):
                strError = "\tCustomer "+self.strLastName +" " + self.strFirstName + " has already returned all bikes to this shop."
                raise RuntimeError(strError)

            print("\t",self.strLastName, self.strFirstName, "has successfully returned all rented bikes from this shop ")

        #ValueError - will catch errors if can not cast when 'intLength = len(self.aintRentsIDs)'
        except ValueError as error:

            intLength = int(0)
            print("Internal error please contact support error:'ReturnRentedBike, len()'.")

        except RuntimeError as error:

            print(error)

        return

    
    
    
    
    
    ##################################################################
    # Name:     RequestReports 
    # Abstract: Gets and prints reports form all shops 
    ##################################################################
    def RequestBill(self):                                              
        try:
            intIndex = 0
            intLength = 0 
            blnAllReturnedAlready = True

            intLength = len(self.aintRentsIDs)

            
            if( intLength > 0):


                for intIndex in range(intLength):
                    
                    #This if controls that only returns bikes to this shop
                    if(self.ashpShpsRentedFrom[intIndex] == self.objShopInterctingWith):
                    
                        if(self.ablnRenturned[intIndex] == False):
                        
                            blnAllReturnedAlready = False
                

                if(blnAllReturnedAlready == False):

                    self.objShopInterctingWith.IssueBill(self)


        #ValueError - will catch errors if can not cast when 'intLength = len(self.aintRentsIDs)'
        except ValueError as error:

            intLength = int(0)
            print("Internal error please contact support error:'ReturnRentedBike, len()'.")


        return





    ##################################################################
    # Name:     RequestReports 
    # Abstract: Gets and prints reports form all shops 
    ##################################################################
    def RequestReports(self):                                              
        try:
            blnCustomerRentedFromThisShop = False
            intndex = 0     
            intLength = 0
            strMessage =""

            intLength = len(self.ashpShpsRentedFrom)
            
            #Customer 
            if(intLength > 0):

                for intIndex in range(intLength):
                    
                    #makng sure customer rented from this shop
                    if(self.ashpShpsRentedFrom[intIndex] == self.objShopInterctingWith):
                        
                        blnCustomerRentedFromThisShop = True
                        
                if(blnCustomerRentedFromThisShop == True):
                    self.objShopInterctingWith.PrintCustomerReport(self)
                
                else:
                    strMessage = "\tCustomer " + self.strLastName+ " " + self.strFirstName + " had not rented any bikes from this shop."
                    raise RuntimeError(strMessage)
            
            else:
                strMessage = "\tCustomer " + self.strLastName+ " " + self.strFirstName + " had not rented any bikes from this shop."
                raise RuntimeError(strMessage)

        except RuntimeError as error:

            print(error)

        return


    #Incase i want to return first name and last name in customer claas instead of person

    #######################################################################
    # Decoration: @property
    # Name:       strLastName
    # Abstract:   Returns value of the "encapsulated" __strLastName
    #######################################################################
    #@property
    #def strLastName(self):
    #    return self.__strLastName 
    ########################################################################
    ## Decoration: @property
    ## Name:       strFirstName
    ## Abstract:   Returns value of the "encapsulated" __strFirstName
    ########################################################################
    #@property
    #def strFirstName(self):
    #    return self.__strFirstName

        ##################################################################
    # Decoration: @strLastName.setter
    # Name:       strLastName
    # Abstract:   Sets the value of the "encapsulated" __strLastName
    ##################################################################
    #@strLastName.setter
    #def strLastName(self, strLastName):        
    #    try:       
    #        if (strLastName != ""):
    #            self.__strLastName = strLastName
    #        else:
    #            raise RuntimeError('Last name can not be an empty string.')       
    #    except RuntimeError as error:
    #        print(error)
    #@strFirstName.setter
    #def strFirstName(self, strFirstName):      
    #    try:      
    #        if (strFirstName != ""):
    #            self.__strFirstName = strFirstName
    #        else:
    #            raise RuntimeError('First name can not be an empty string.')      
    #    except RuntimeError as error:
    #        print(error)