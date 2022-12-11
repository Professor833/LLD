'''
Demonstrates the use of access modifiers and constructors in Python.
'''


class MyClass:
    # Class variable
    classVar = 0

    # Constructor
    def __init__(self):
        self.__privateVar = 0
        self._protectedVar = 0
        self.publicVar = 0

    # Class method
    def classMethod(self):
        self.__privateMethod()
        self._protectedMethod()
        self.publicMethod()

    # Private method
    def __privateMethod(self):
        print("This is a private method")

    # Protected method
    def _protectedMethod(self):
        print("This is a protected method")

    # Public method
    def publicMethod(self):
        print("This is a public method")
