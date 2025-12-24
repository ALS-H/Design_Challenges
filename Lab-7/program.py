from result_finder import ResultFinder

class Program:
    @staticmethod
    def main(args):
        # Accept the values from command line arguments
        marks1 = int(args[0])
        marks2 = int(args[1])
        marks3 = int(args[2])

        # Store the values entered in the object
        finder = ResultFinder()
        finder.marks1 = marks1  #setters are called here
        finder.marks2 = marks2
        finder.marks3 = marks3

        # Display all the information with the help of get and other methods
        finder.display_marks()
        print("Total : " + str(finder.get_total()))
        print("Average : " + str(finder.get_average()))
        print("Result : " + str(finder.get_result()))

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
