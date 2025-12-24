class Program:
    @staticmethod
    def main(args):
        number1 = 100
        number2 = 200

        Program.display_values("Before Swapping...", number1, number2)

        Program.swap_values(number1, number2)

        Program.display_values("After Swapping...", number1, number2)

        input()

    """
    Method to swap two numbers
    """
    @staticmethod
    def swap_values(number1, number2):
        #swapping is not possible here
        #number1 and number2 are immutable objects
        #python passes arguments by object reference
        #reassigning a parameter doesn't affect the caller's variable
        pass

    """
    Method to display the numbers before and after swapping
    """
    @staticmethod
    def display_values(str_msg, number1, number2):
        print(str_msg)
        print("Number 1 = " + str(number1))
        print("Number 2 = " + str(number2))


if __name__ == "__main__":
    Program.main([])
