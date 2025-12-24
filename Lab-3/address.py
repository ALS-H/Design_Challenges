class Address:
    def __init__(self):
        self._addr1=None
        self._addr2=None
        self._city=None
        self._pincode=None
    
    """ 
    Properties for the fields
    """
    
    @property
    def addr1(self):
        return self._addr1
    
    @addr1.setter
    def addr1(self,value):
        self._addr1=value
    
    @property
    def addr2(self):
        return self._addr2
    
    @addr2.setter
    def addr2(self,value):
        self._addr2=value
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self,value):
        self._city=value
        
    @property
    def pincode(self):
        return self._pincode
    
    @pincode.setter
    def pincode(self,value):
        self._pincode=value
        
