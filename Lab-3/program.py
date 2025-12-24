from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        emp.emp_id="EMP123456"
        emp.emp_name="Haneela"
        emp.emp_gender="Female"

        addr=Address()
        addr.addr1="Flat 101"
        addr.addr2="MG Road"
        addr.city="Bangalore"
        addr.pincode="500001"
        emp.address=addr

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        print("Employee Id : "+emp.emp_id)
        print("Employee Name : "+emp.emp_name)
        print("Employee Gender : "+emp.emp_gender)

        print("Employee Address : --------------")
        print("Address 1 : "+emp.address.addr1)
        print("Address 2 : "+emp.address.addr2)
        print("City : "+emp.address.city)
        print("PinCode : "+emp.address.pincode)
        print("----------------------------------")

if __name__ == "__main__":
    Program.main([])
