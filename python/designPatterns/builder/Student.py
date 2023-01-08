# from Builder import Builder

class Student:
    def __init__(self) -> None:
        self.__name: str = None
        self.__age: str = None
        self.__psp: str = None  # problem Solving Percentage
        self.__universityName: str = None
        self.__batch: str = None
        self.__id: str = None
        self.__gradYear: int = None
        self.__phoneNumber: str = None

    # setters
    def setName(self, name: str) -> None:
        self.__name = name

    def setAge(self, age: str) -> None:
        self.__age = age

    def setPsp(self, psp: str) -> None:
        self.__psp = psp

    def setUniversityName(self, universityName: str) -> None:
        self.__universityName = universityName

    def setBatch(self, batch: str) -> None:
        self.__batch = batch

    def setGradYear(self, gradYear: int) -> None:
        self.__gradYear = gradYear

    def setPhoneNumber(self, phoneNumber: str) -> None:
        self.__phoneNumber = phoneNumber

    @staticmethod
    def getBuilder() -> 'Builder':
        return Student.Builder()

    # make Builder class as static inner class
    @staticmethod
    class Builder:
        def __init__(self) -> None:
            # initialize all the fields
            self.__name: str = None
            self.__age: str = None
            self.__psp: str = None  # problem Solving Percentage
            self.__universityName: str = None
            self.__batch: str = None
            self.__id: str = None
            self.__gradYear: int = None
            self.__phoneNumber: str = None

        # setters
        def setName(self, name: str) -> 'Builder':
            self.__name = name
            return self

        def setAge(self, age: str) -> 'Builder':
            self.__age = age
            return self

        def setPsp(self, psp: str) -> 'Builder':
            self.__psp = psp
            return self

        def setUniversityName(self, universityName: str) -> 'Builder':
            self.__universityName = universityName
            return self

        def setBatch(self, batch: str) -> 'Builder':
            self.__batch = batch
            return self

        def setGradYear(self, gradYear: int) -> 'Builder':
            self.__gradYear = gradYear
            return self

        def setPhoneNumber(self, phoneNumber: str) -> 'Builder':
            self.__phoneNumber = phoneNumber
            return self

        def build(self) -> 'Student':
            # validate all the fields
            if self.__gradYear > 2023:
                raise ValueError('Graduation year must be less than 2023')

            s: Student = Student()
            s.setName(self.__name)
            s.setAge(self.__age)
            s.setPsp(self.__psp)
            s.setUniversityName(self.__universityName)
            s.setBatch(self.__batch)
            s.setGradYear(self.__gradYear)
            s.setPhoneNumber(self.__phoneNumber)
            return s
