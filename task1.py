class Student():
    def __init__(self,name,last_name,year_of_entrance,department):
        self.name = name
        self.last_name=last_name
        self.year_of_entrance = year_of_entrance
        self.department = department

    #it's metod
    def generate_chocolate(self):
        print( f'Student-{self.name}--{self.last_name}-postupil na fakultet-{self.department}-v-{self.year_of_entrance}')
student1 = Student(
name = 'Vasya',
last_name = 'Ivanov',
department = 'Programmorovanie',
year_of_entrance = '2017'
)

student1.generate_chocolate()
