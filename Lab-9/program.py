from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 4

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            emp = Employee()
            print("Employee No : " + str(i+1))
            print("Id : ")
            emp.emp_id = input()

            print("Name : ")
            emp.name = input()

            print("Basic : ")
            emp.basic = input()

            print("HRA : ")
            emp.hra = input()

            print("Percentage of Allowance : ")
            emp.allowance_percentage = input()

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            emp.role = input()

            # Note: Original C# code does not assign Employee object to Employees array
            employees[i]=emp    # Store employee object in array
        
        report = EmployeeReport()

        print("Enter the date of the report (dd/mm/yyyy) : ")
        report.report_date = input() #setter is called 
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
