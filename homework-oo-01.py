class Person:
    def __init__(self, first_name: str, last_name: str, birth_year: int):
        """This is the constructor of the Person class.

        Args:
            first_name (str): First Name of the Person
            last_name (str): Last Name of the Person
            birth_year (int): Birth Year of the Person
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.__private_str = "Test Private Attribute Inheritance"

    def calculate_age(self) -> int:
        """This method calculates the age based on the birth year.

        Returns:
            int: age of the person
        """
        age: int = 1403 - self.birth_year
        print(age)
        return age

    def format_name(self) -> str:
        """This method formats the name of the person.

        Returns:
            str: formatted name
        """
        formatted_name: str = f"{self.first_name.upper()} {self.last_name.upper()}"
        print(formatted_name)
        return formatted_name


class Student(Person):

    def __init__(self, first_name: str, last_name: str, birth_year: int):
        # supper refers to the parent class
        super().__init__(
            first_name=first_name, last_name=last_name, birth_year=birth_year
        )
        self.__student_id = None

    def set_student_id(self, student_id: int):
        # Setter Method
        """This method sets the student id.

        Args:
            student_id (int): student id
        """
        self.__student_id = student_id

    def validate_age(self) -> bool:
        """Check if student is equal or older than 18

        Returns:
            bool: True if the student is equal or older than 18 else return False
        """
        age: int = self.calculate_age()
        result: bool = age >= 18
        print(result)
        return result

    def print_student_info(self) -> str:
        """This method prints the student information.
        You should use the format_name method of the parent class.
        Note that you should exactly print like the example.
        Example:
            "Student: PEYMAN BARJOUEIAN, 1370"
        Returns:
            str: student information
        """
        student_info: str = f"Student: {self.format_name()}, {self.birth_year}"
        print(student_info)
        return student_info


class Employee(Person):

    def __init__(self, first_name: str, last_name: str, birth_year: int):
        # supper refers to the parent class
        super().__init__(
            first_name=first_name, last_name=last_name, birth_year=birth_year
        )
        self.__employee_id = None

    def set_employee_id(self, employee_id: int):
        """This method sets the employee id.

        Args:
            employee_id (int): employee id
        """
        self.__employee_id = employee_id

    def print_employee_info(self) -> str:
        """This method prints the employee information.
        You should use the format_name method of the parent class.
        Note that you should exactly print like the example.
        Example:
            "Employee: PEYMAN BARJIUEIAN, 1370"
        Returns:
            str: employee information
        """
        employee_info: str = f"Employee: {self.format_name()}, {self.birth_year}"
        print(employee_info)
        return employee_info


person = Person("Peyman", "Barjoueian", 1370)
person.calculate_age()
person.format_name()

st1 = Student(first_name="Nima", last_name="Ahmadi", birth_year=1380)
st1.set_student_id(student_id=12345)
st1.validate_age()
st1.print_student_info()

emp1 = Employee(first_name="Nima", last_name="Ahmadi", birth_year=1380)
emp1.set_employee_id(employee_id=12345)
emp1.print_employee_info()
