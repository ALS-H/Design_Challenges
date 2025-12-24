from salary_calculator import SalaryCalculator
from role_builder import RoleBuilder
from roles import Roles

class Employee:
    """
    Properties of the class
    """
    def __init__(self):
        self._emp_id = "" #protected variables
        self._name = ""
        self._basic = 0.0
        self._hra = 0.0
        self._allowance_percentage = 0.0
        self._role = 0

    @property
    def emp_id(self):
        return self._emp_id
    
    @emp_id.setter
    def emp_id(self,value):
        self._emp_id=value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name=value
    
    @property
    def basic(self):
        return self._basic
    
    @basic.setter
    def basic(self,value):
        self._basic=float(value)
    
    @property
    def hra(self):
        return self._hra
    
    @hra.setter
    def hra(self,value):
        self._hra=float(value)
        
    @property
    def allowance_percentage(self):
        return self._allowance_percentage
    
    @allowance_percentage.setter
    def allowance_percentage(self,value):
        self._allowance_percentage=float(value)
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self,value):
        self._role=int(value) 
        
        
    def get_allowance(self):
        """
        Delegates allowance calculation to SalaryCalculator
        """
        return SalaryCalculator.get_allowance(self)
    
    def get_salary(self):
        """
        Delegates salary calculation to SalaryCalculator
        """
        return SalaryCalculator.get_salary(self)
    
    def get_role_description(self):
        """
        Delegates role to Rolebuilder
        """
        return RoleBuilder.get_role_description(self._role)
    
    