class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self._marks1 = 0  #protected variables
        self._marks2 = 0
        self._marks3 = 0
    
    """ 
    getters and setters
    """
    @property
    def marks1(self):
        return self._marks1
    
    @marks1.setter
    def marks1(self,val):
        self._marks1=val
        
    @property
    def marks2(self):
        return self._marks2
    
    @marks2.setter
    def marks2(self,val):
        self._marks2=val
    
    @property
    def marks3(self):
        return self._marks3

    @marks3.setter
    def marks3(self,val):
        self._marks3=val
        
    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("Marks entered------------- ")
        print("Marks 1 : " + str(self._marks1))
        print("Marks 2 : " + str(self._marks2))
        print("Marks 3 : " + str(self._marks3))

    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self._marks1+self._marks2+self._marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        return round((self._marks1+self._marks2+self._marks3)/3,2)

    """
    Method to get the result for the marks given
    """
    def get_result(self):
        if self._marks1 < 35 or self._marks2 < 35 or self._marks3 < 35:
            return "Fail"
        
        avg = self.get_average()

        if avg >= 80:
            return "First Class"
        elif avg >= 60:
            return "Second Class"
        elif avg >= 35:
            return "Pass"
        else:
            return "Fail"

