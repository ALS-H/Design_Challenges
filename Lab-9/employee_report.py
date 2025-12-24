from employee import Employee
from role_builder import RoleBuilder
from salary_calculator import SalaryCalculator

class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self):
        self._report_date = ""
    
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self,value):
        self._report_date=value

    """
    Method to print a line in a report
    """
    def print_line(self):
        print("---------------------------------------------------------------------------")

    """
    Method to display header information of the report
    """
    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self._report_date)
        self.print_line()

    """
    Method to display footer information in the report
    """
    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    """
    Method to display employees information
    """
    def display_employees(self, employees):
        self.display_header()

        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        
        self.print_line()
        
        for emp in employees:
            if emp is not None:
                print(
                    str(emp.emp_id)+"\t"+
                    emp.name + "\t" +
                    RoleBuilder.get_role_description(emp.role)+"\t"+
                    str(emp.basic)+"\t"+
                    str(emp.hra)+ "\t" +
                    str(SalaryCalculator.get_allowance(emp)) +"\t" +
                    str(SalaryCalculator.get_salary(emp))
                )

        # Placeholder for employee information printing
        # Original C# code does not include the loop for displaying details

        self.display_footer(len(employees))
