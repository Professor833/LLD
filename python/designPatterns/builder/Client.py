from Student import Student


class Client:
    def main(self):
        s: Student = Student.Builder().setName('Lalit').setAge('23').setPsp('99%').setUniversityName('GU').setBatch('Apr22').setGradYear(2023).setPhoneNumber(
            '123456789').build()

        # loop through all the fields of student and print them
        for attr, value in s.__dict__.items():
            print(attr, ' >> ', value)


if __name__ == '__main__':
    Client().main()
