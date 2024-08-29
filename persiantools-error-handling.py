from persiantools.jdatetime import JalaliDate, JalaliDateTime
class Person:
    def __init__(self, first_name: str, last_name: str, birth_year: int):
        """This is the constructor of the Person class.
        s
        Args:
            first_name (str): First Name of the Person
            last_name (str): Last Name of the Person
            birth_year (int): Birth Year of the Person
        """
        try:
            self.first_name = first_name
            self.last_name = last_name
        except:
            print("you must sent string ")    
        try:
            self.birth_year = birth_year
        except:
            print("Your birth year must be lunar")
            self.birth_year=int(self.birth_year)


        self.__private_str="test"

    def calculate_age(self) -> int:
        """This method calculates the age based on the birth year.

        Returns:
            int: age of the person
        """
        year=JalaliDateTime.now().strftime("%Y")
        return year - self.birth_year   
        

    def format_name(self) -> str:
        """This method formats the name of the person.

        Returns:
            str: formatted name
        """
        return f"{self.first_name.upper()} {self.last_name.upper()}"



class Student(Person):

    def __init__(self, first_name: str, last_name: str, birth_year: int):
        # supper refers to the parent class
        super().__init__(
            first_name=first_name, last_name=last_name, birth_year=birth_year
        )
        self.__student_id = None

    def set_student_id(self, student_id: int):
        """This method sets the student id.

        Args:
            student_id (int): student id
        """
        self.__student_id=student_id

    def validate_age(self,) -> bool:
        """Check if student is equal or older than 18

        Returns:
            bool: True if the student is equal or older than 18 else return False
        """
        try:
            age=self.calculate_age()
            return age>= 18
        except:
            age=int(age)

    def print_student_info(self) -> str:
        """This method prints the student information.
        You should use the format_name method of the parent class.
        Note that you should exactly print like the example.
        Example:
            "Student: Peyman Barjoueian, 1370"
        Returns:
            str: student information
        """
        return f"student:{self.format_name()},{self.birth_year}"
        

class Employee(Person):

    def __init__(self, first_name: str, last_name: str, birth_year: int):
        # supper refers to the parent class
        super().__init__(
            first_name=first_name, last_name=last_name, birth_year=birth_year,
        )
        self.__employee_id = None

    def set_employee_id(self, employee_id: int):
        """This method sets the employee id.

        Args:
            employee_id (int): employee id
        """
        self.__employee_id=employee_id

    def print_employee_info(self,) -> str:
        """This method prints the employee information.
        You should use the format_name method of the parent class.
        Note that you should exactly print like the example.
        Example:
            "Employee: Peyman Barjoueian, 1370"
        Returns:
            str: employee information
        """
        return f"student:{self.format_name()},{self.birth_year}"


        


