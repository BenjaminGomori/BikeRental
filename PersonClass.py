##################################################################
# Class Name:  Person
# Abstract:    Blueprint for Person, properties and behaviors
##################################################################
class Person(object):
    """description of class"""

    ##################################################################
    # Name:     __init__
    # Abstract: Constructor - automatically called when instance of 
    #           class is created.
    ##################################################################
    def __init__(self, strLastName, strFirstName):
       
        self.strLastName    = strLastName
        self.strFirstName   = strFirstName




    ###############
    ##  PROPERTY ##
    ###############
    #######################################################################
    # Decoration: @property
    # Name:       strLastName
    # Abstract:   Returns value of the "encapsulated" __strLastName
    #######################################################################
    @property
    def strLastName(self):
        return self.__strLastName 


    #######################################################################
    # Decoration: @property
    # Name:       strFirstName
    # Abstract:   Returns value of the "encapsulated" __strFirstName
    #######################################################################
    @property
    def strFirstName(self):
        return self.__strFirstName



    ###############
    ##  SETTER   ##
    ############### 


    ##################################################################
    # Decoration: @strLastName.setter
    # Name:       strLastName
    # Abstract:   Sets the value of the "encapsulated" __strLastName
    ##################################################################
    @strLastName.setter
    def strLastName(self, strLastName):
        
        try:
       
            if (strLastName != ""):
                self.__strLastName = strLastName

            else:
                raise RuntimeError('Last name can not be an empty string.')
       
        except RuntimeError as error:

            print(error)



    ##################################################################
    # Decoration: @strFirstName.setter
    # Name:       strFirstName
    # Abstract:   Sets the value of the "encapsulated" __strFirstName
    ##################################################################
    @strFirstName.setter
    def strFirstName(self, strFirstName):
        
        try:
       
            if (strFirstName != ""):
                self.__strFirstName = strFirstName

            else:
                raise RuntimeError('First name can not be an empty string.')
       
        except RuntimeError as error:

            print(error)