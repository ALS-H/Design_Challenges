from address import Address
"""
Class to represent employee information
"""
class Employee:
    def __init__(self):
        self._emp_id=None
        self._emp_name=None
        self._emp_gender=None
        self._address=Address() #composition
    
    """ 
    Properties 
    """
    
    @property
    def emp_id(self):
        return self._emp_id
    
    @emp_id.setter
    def emp_id(self,value):
        self._emp_id=value
        
    @property
    def emp_name(self):
        return self._emp_name
    
    @emp_name.setter
    def emp_name(self,value):
        self._emp_name=value
        
    @property
    def emp_gender(self):
        return self._emp_gender
    
    @emp_gender.setter
    def emp_gender(self,value):
        self._emp_gender=value
        
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self,value):
        self._address=value
    