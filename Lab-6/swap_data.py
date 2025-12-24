class SwapData:
    """
    Properties of the class
    """
    def __init__(self):
        self._number1 = 0 #protected variable
        self._number2 = 0 #protected variable

    """ 
    getters and setters 
    """
    @property
    def number1(self):
        return self._number1
    
    @number1.setter
    def number1(self,val):
        self._number1=val
        
    @property
    def number2(self):
        return self._number2
    
    @number2.setter
    def number2(self,val):
        self._number2=val
        
    """
    Method to swap numbers of the class
    """
    #here you are swapping the object state
    def swap_values(self):
        self._number1,self._number2=self._number2,self._number1

    """
    Method to display the numbers before and after swapping
    """
    def display_values(self, str_msg):
        print(str_msg)
        print("Number 1 = " + str(self._number1))
        print("Number 2 = " + str(self._number2))
